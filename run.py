import sys
import yt_dlp
import whisper

def get_video_title(url):
    with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
        info = ydl.extract_info(url, download=False)
        return info.get("title")

def download_audio(url, output_path="input.mp4"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def transcribe(path="input.mp4", model_size="base"):
    model = whisper.load_model(model_size)
    result = model.transcribe(path)
    return result["text"]

if __name__ == "__main__":
    url = sys.argv[1]
    title = get_video_title(url)
    download_audio(url)
    script = transcribe()

    with open("title.txt", "w", encoding="utf-8") as f:
        f.write(title)
    with open("script.txt", "w", encoding="utf-8") as f:
        f.write(script)
