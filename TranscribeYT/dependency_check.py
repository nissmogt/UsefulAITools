import os
import subprocess


def check_dependencies():
    try:
        import youtube_dl
        import openai
        import whisper
        import dotenv
    except ImportError as e:
        missing_module = str(e).split()[-1]
        subprocess.call(['pip', 'install', missing_module])
        check_dependencies()
