import os
from moviepy import AudioFileClip, ImageClip

audio_path = os.path.join("output", "instrumental_new.mp3")
image_path = os.path.join("output", "background.png")
output_path = os.path.join("output", "submission_video.mp4")

if not os.path.exists(audio_path):
    print(f"Error: {audio_path} not found")
    exit(1)

audio = AudioFileClip(audio_path)
image = ImageClip(image_path).set_duration(audio.duration)
video = image.set_audio(audio)

video.write_videofile(output_path, fps=24)
print(f"Success! Video created at: {os.path.abspath(output_path)}")
