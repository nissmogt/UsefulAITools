# UsefulAITools

## TranscribeYT
```yt_transcriber.py```: Transcribe YouTube videos using OpenAI Whisper.

### Installation 
**Note: All testing was done using Python 3.8.** Ignore any step if you already have any of these installed.
1. Run ```pip install -r requirements.txt``` to install dependencies.
 
This installs the necessary `youtube-dl` and `OpenAI Whisper` libraries.

2. The `ffmpeg` package must be downloaded separately. Use the following commands to install:
- *macOS*: ```brew install ffmpeg```. Must have Homebrew installed.
- *Ubuntu*: ```sudo apt-get install ffmpeg```

3. Download the required aria2c binary for your OS from [here](https://aria2.github.io/). 
Place the binary in the `bin` folder. This package is nice because it supports a number of advanced features such 
as download acceleration, resumable downloads, and support for downloading files from multiple sources. 
Or use the following commands to install:
- *macOS*: ```brew install aria2```. Must have Homebrew installed.
- *Ubuntu*: ```sudo apt-get install aria2```
### Testing
1. Run ```python yt_transcriber.py``` to start the program. When prompted, leave 
Youtube URL blank to test with default video.

2. The transcribed text will be saved to a file called *audio.txt* in 
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

### Instructions for noobs
1. To clone this repository, you will need to have Git installed on your computer. If you do not already have Git installed, 
you can download and install it from the official website [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

2. Once you have Git installed, you can follow these steps to clone the repository:

3. Open a terminal or command prompt and navigate to the directory where you want to clone the repository.
Run the following command to clone the repository:```git clone https://github.com/nissmogt/UsefulAITools.git```
4. See steps 1-3 in the Installation section above to install the dependencies and run the program.
5. Run a test using instructions in Testing section above.
6. You are now ready to use. Congrats noob, you're not a noob anymore. Enjoy!