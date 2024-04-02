from moviepy.editor import VideoFileClip

def extract_audio_from_mp4(input_file, output_file):
    try:
        video_clip = VideoFileClip(input_file)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(output_file)
        print("Audio extracted successfully!")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    input_file = "core-team2023-11-031815.mp4"  # Replace with the path to your input MP4 file
    output_file = "output_audio.mp3"  # Replace with the desired output audio file format (e.g., .mp3, .wav)

    extract_audio_from_mp4(input_file, output_file)
