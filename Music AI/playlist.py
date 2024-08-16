from pydub import AudioSegment
import os

def combine_audio(clips, output_file):
    combined = AudioSegment.empty()
    for clip in clips:
        if not os.path.isfile(clip):
            print(f"File not found: {clip}")
            continue
        try:
            audio = AudioSegment.from_file(clip)
            combined += audio
        except Exception as e:
            print(f"An error occurred while processing {clip}: {e}")
            continue
    combined.export(output_file, format="mp3")
    print(f"Playlist saved as {output_file}")

if __name__ == "__main__":
    # List of audio clips with absolute paths
    audio_clips = [
        r'\WhispersintheForest.mp3', #Please replace with your current path
        r'\ForestCanvas.mp3', #Please replace with your current path
        r'\ChasingtheDawn.mp3', #Please replace with your current path
        r'\RiseandShine.mp3' #Please replace with your current path

    ]

    # Output playlist file with absolute path
    output_playlist = r'\playlist.mp3' #Please replace with your current path

    # Combine audio files into a playlist
    combine_audio(audio_clips, output_playlist)
