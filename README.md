# UsefulAITools

## TranscribeYT
```yt_transcriber.py```: Transcribe YouTube videos using OpenAI Whisper.

### Installation 
**Note: All testing was done using Python 3.8.**
1. Run ```pip install -r requirements.txt``` to install dependencies.
 
This installs the necessary `youtube-dl` and `OpenAI Whisper` libraries.

2. The `ffmpeg` package must be downloaded separately. Use the following commands to install:
- *macOS*: ```brew install ffmpeg```. Must have Homebrew installed.
- *Ubuntu*: ```sudo apt-get install ffmpeg```

### Testing
3. Run ```python yt_transcriber.py``` to start the program. When prompted, leave 
Youtube URL blank to test with default video.

4. The transcribed text will be saved to a file called *audio.txt* in 
a directory called *transcriptions*.

### Usage
Given a valid YouTube URL, this program downloads YouTube audio and transcribes it using OpenAI Whisper. It creates two directories: 
- **transcriptions**: Stores the transcribed text in a file called *audio.txt*.
- **audio**: Temporarily stores the downloaded audio in a file called *audio.mp3* and contains the converted WAV file. 
The program deletes both files (can be changed to keep the audio files if you want).

To use the program, simply enter the URL of the YouTube video you want to transcribe either like this:

```python yt_transcriber.py PASTE_URL_HERE```

or by pasting the url when prompted.

Enjoy and please submit any issues you find to the Issues tab!

Thanks!
