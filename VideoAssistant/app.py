from shiny.express import input, render, ui
from shinymedia import input_video_clip, audio_spinner
from query import chat

input_video_clip("clip")

messages = []


# Show the chat response
@render.ui
def response():
    with ui.Progress() as p:
        p.set(message="Chatting...")
        response_audio = chat(input.clip(), messages, p)
    return audio_spinner(src=response_audio)
