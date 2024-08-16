# # Multimodal demo
#
# This is an example of how to simulate a video- and audio-aware model using existing LLM vision models (that take text and images as input, and generate text as output).

import os
from pathlib import Path
from typing import Any

import dotenv
from openai import AsyncOpenAI
from ollama import AsyncClient as AsyncOllamaClient
from shiny import ui

from media_extractor import split_video
import datauri


# Load OpenAI API key from .env file
dotenv.load_dotenv()
if os.environ.get("OPENAI_API_KEY") is None:
    raise ValueError("OPENAI_API_KEY not found in .env file")

SYSTEM_PROMPT = (Path(__file__).parent / "system_prompt.txt").read_text()

client = AsyncOpenAI()
client_ollama = AsyncOllamaClient()


class OpenAIStrategy:
    def __init__(self, client: AsyncOpenAI):
        self.client = client

    async def chat(
        self, model: str, user_prompt: str, image_uris: list[str], messages: list[Any]
    ) -> str:
        messages.append(
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": user_prompt},
                    *[
                        {
                            "type": "image_url",
                            "image_url": {"url": image_uri, "detail": "auto"},
                        }
                        for image_uri in image_uris
                    ],
                ],
            }
        )

        resp = await self.client.chat.completions.create(
            model=model,
            messages=[
                *messages,
                {"role": "system", "content": SYSTEM_PROMPT},
            ],
        )
        messages.append(resp.choices[0].message)

        return resp.choices[0].message.content


class OllamaStrategy:
    def __init__(self, client: AsyncOllamaClient):
        self.client = client

    async def chat(
        self, model: str, user_prompt: str, image_uris: list[str], messages: list[Any]
    ) -> str:
        messages.append(
            {
                "role": "user",
                "content": user_prompt,
                "images": [datauri.parse(img)[0] for img in image_uris],
            }
        )

        resp = await self.client.chat(
            model=model,
            messages=[
                *messages,
                {"role": "system", "content": SYSTEM_PROMPT},
            ],
        )
        messages.append(resp["message"])
        return resp["message"]["content"]


openai_strategy = OpenAIStrategy(client)
ollama_strategy = OllamaStrategy(client_ollama)

# This is the input video that we'll turn into the user prompt.


async def chat(
    model: str, video_file: str, messages: list[Any], progress: ui.Progress
) -> str:
    # At the time of this writing, the GPT-4o API doesn't directly support video or audio input. Instead, we'll decode the video into frames and feed them to the model as images, and decode the audio into text and feed it to the model as text.

    progress.set(detail="Splitting video into audio and images...", value=0)
    audio_uri, image_uris = split_video(video_file)

    # Decode the audio file into text, using OpenAI's `whisper-1` model. The result will serve as the text prompt for the LLM.

    progress.set(detail="Transcribing audio...", value=0.1)
    with datauri.as_tempfile(audio_uri) as audio_file:
        transcription = await client.audio.transcriptions.create(
            model="whisper-1", file=Path(audio_file)
        )

    user_prompt = transcription.text

    # We're ready to talk to the LLM: use the text and images as input, and get generated text back.

    if model == "llava:7b":
        chat_client = ollama_strategy
    else:
        chat_client = openai_strategy

    progress.set(detail="Chatting...", value=0.2)
    response_text = await chat_client.chat(model, user_prompt, image_uris, messages)

    # Use OpenAI's text-to-speech model to turn the generated text into audio.

    progress.set(detail="Synthesizing audio...", value=0.8)
    audio = await client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=response_text or "",
        response_format="mp3",
    )
    response_audio_uri = datauri.from_bytes(audio.read(), "audio/mpeg")
    return response_audio_uri
