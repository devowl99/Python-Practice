pip install spleeter pydub ffmpeg-python

import ffmpeg

def extract_audio(video_path, audio_path):
    ffmpeg.input(video_path).output(audio_path).run()

from spleeter.separator import Separator

def separate_audio(audio_path, output_path):
    separator = Separator('spleeter:2stems')  # 2 stems: vocals and accompaniment
    separator.separate_to_file(audio_path, output_path)

from pydub import AudioSegment

def remove_vocals(input_path, output_path):
    # Load the separated tracks
    vocals = AudioSegment.from_file(f"{input_path}/vocals.wav")
    accompaniment = AudioSegment.from_file(f"{input_path}/accompaniment.wav")

    # Save the accompaniment (background music and effects) as the new audio track
    accompaniment.export(output_path, format="wav")

def combine_audio_video(video_path, audio_path, output_path):
    input_video = ffmpeg.input(video_path)
    input_audio = ffmpeg.input(audio_path)
    ffmpeg.output(input_video, input_audio, output_path, vcodec='copy', acodec='aac', strict='experimental').run()