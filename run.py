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
    print("🔹VIDEO_TITLE_START🔹")
    print(title.strip())
    print("🔹VIDEO_TITLE_END🔹")

    download_audio(url)
    script = transcribe()
    print("🔸SCRIPT_START🔸")
    print(script.strip())
    print("🔸SCRIPT_END🔸")
