#
# This python function uses the transformers library to transcribe an audio file from YouTube to text.
#
# Author: @nissmogt
# Date: 2021-12-09
#
# Usage: python yt_transcription.py <youtube_url>


import os
import whisper
import youtube_dl
import subprocess
from pathlib import Path
from transformers import pipeline


# Check if the audio file exists
def check_audio_file(audiofile):
    import contextlib
    import wave
    try:
        with contextlib.closing(wave.open(audiofile)) as f:
            return True
    except:
        return False


# Download the audio from a given URL, set outtmpl based on video title, and return video title
def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio/audio.mp3',
        'external_downloader': 'aria2c',
        'external_downloader_args': ['-x16', '-k1M'],
        'executable': '/usr/bin/aria2c',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'delete_after': False,
        'extract_audio': True,
        'audio_format': 'mp3',
        'audio_quality': 0,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_title = info_dict.get('title', None)
    video_title = "audio.mp3"
    return video_title


def transcribe_audio(url):
    # Set the audio and transcription paths
    audio_path = Path('audio')
    transcription_path = Path('transcriptions')

    # Create the audio and transcription directories if they don't exist
    if not audio_path.exists():
        audio_path.mkdir()
    if not transcription_path.exists():
        transcription_path = transcription_path.mkdir()

    title = download_audio(url)

    # Convert the MP3 file to WAV
    tmp_audio_file = os.path.join(audio_path, title)
    audiofile = os.path.join(audio_path, f"{title}.wav")
    subprocess.call(['ffmpeg', '-i', tmp_audio_file, '-acodec', 'pcm_s16le', '-ac', '1',
                     '-ar', '16000', audiofile])

    # Use OpenAI Whisper to transcribe the wav audio
    model = whisper.load_model("base")
    transcription = model.transcribe(audiofile)
    with open(os.path.join(transcription_path, title.strip(".mp3") + ".txt"), 'a') as f:
        f.write(transcription['text'] + ' ')

    # delete audio mp3 and wav files
    os.remove(tmp_audio_file)
    os.remove(audiofile)


if __name__ == '__main__':
    import sys

    # link = sys.argv[1]
    # link = 'https://www.youtube.com/watch?v=v26CcifgEq4'  # toast masters speech
    # link = 'https://www.youtube.com/watch?v=wMBHQktcSQ0'  # chris voigt bio talk
    link = 'https://www.youtube.com/watch?v=2bZi3Xm9tJE'
    # link = 'https://www.youtube.com/watch?v=9FudzqfpLLs'
    transcribe_audio(str(link))
