#
# This python function uses the transformers library to transcribe an audio file from YouTube to text.
#
# Author: @nissmogt
# Date: 2021-12-09
#
# Usage: python yt_transcription.py <youtube_url>


import os
import youtube_dl
import subprocess
from pathlib import Path
from transformers import pipeline


# Download the audio from a given URL, set outtmpl based on video title, and return video title
def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.mp3',
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
    return video_title


def transcribe_audio(url):

    # Check if the audio file exists
    def check_audio_file(audio_file):
        import contextlib
        import wave
        try:
            with contextlib.closing(wave.open(audio_file)) as f:
                return True
        except:
            return False

    # Set the audio and transcription paths
    audio_path = Path('audio')
    transcription_path = Path('transcriptions')

    # Create the audio and transcription directories if they don't exist
    if not audio_path.exists():
        audio_path.mkdir()
    if not transcription_path.exists():
        transcription_path = transcription_path.mkdir()

    tmp_audio_file = os.path.join(audio_path, 'audio.mp3')
    if not os.path.exists(tmp_audio_file):
        title = download_audio(url)
    else:
        # get title of mp3 file
        title = os.path.basename(tmp_audio_file).strip('.mp3')

    audiofile = os.path.join(audio_path, title + '.wav')
    print(audiofile)

    # Use ffmpeg to convert the MP3 file to WAV
    if not os.path.exists(audiofile):
        subprocess.call(['ffmpeg', '-i', tmp_audio_file, audiofile])
    else:
        print(f'{audiofile} already exists')

    # load the model and set max tokens to max length of the audio file
    transcriber = pipeline(model="openai/whisper-base")

    # transcribe audio file
    transcription = transcriber(audiofile, max_new_tokens=1000000, padding=True)

    print("Saving transcription to file")
    transcription_path = os.path.join('transcriptions', title + '.txt')
    with open(transcription_path, 'w') as f:
        f.write(transcription['text'])


if __name__ == '__main__':

    import sys
    link = sys.argv[1]
    # link = 'https://www.youtube.com/watch?v=9bZkp7q19f0'
    transcribe_audio(str(link))
