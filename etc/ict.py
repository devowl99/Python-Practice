import ffmpeg
from spleeter.separator import Separator
from pydub import AudioSegment
import tkinter as tk
from tkinter import filedialog, messagebox

# 영상 파일에서 음성 트랙 추출
def extract_audio(video_path, audio_path):
    ffmpeg.input(video_path).output(audio_path).run()

# 음성 트랙에서 성우의 음성 분리
def separate_audio(audio_path, output_path):
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(audio_path, output_path)

# 분리된 음성에서 성우의 음성 제거
def remove_vocals(input_path, output_path):
    accompaniment = AudioSegment.from_file(f"{input_path}/accompaniment.wav")
    accompaniment.export(output_path, format="wav")

# 원본 영상과 새로운 음성 트랙 통합
def combine_audio_video(video_path, audio_path, output_path):
    input_video = ffmpeg.input(video_path)
    input_audio = ffmpeg.input(audio_path)
    ffmpeg.output(input_video, input_audio, output_path, vcodec='copy', acodec='aac', strict='experimental').run()

# 파일 업로드 함수
def upload_file():
    file_path = filedialog.askopenfilename()
    return file_path

# 파일 저장 함수
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])
    return file_path

# 영상 처리 함수
def process_video():
    video_path = upload_file()
    if video_path:
        audio_path = "extracted_audio.wav"
        extract_audio(video_path, audio_path)
        separate_audio(audio_path, "output")
        remove_vocals("output", "no_vocals.wav")
        output_path = save_file()
        if output_path:
            combine_audio_video(video_path, "no_vocals.wav", output_path)
            messagebox.showinfo("Success", "Video processed successfully!")

# GUI 설정
root = tk.Tk()
root.title("Audio Removal Tool")

upload_button = tk.Button(root, text="Upload Video", command=process_video)
upload_button.pack()

root.mainloop()