import sys
import yt_dlp
import whisper

def get_video_title(url):
    ydl_opts = {
        'quiet': True,
        'cookiefile': 'cookies.txt',  # 쿠키 인증
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info.get("title")

def download_audio(url, output_path="input.mp4"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'quiet': True,
        'cookiefile': 'cookies.txt',  # 쿠키 인증
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def transcribe(path="input.mp4", model_size="base"):
    model = whisper.load_model(model_size)
    result = model.transcribe(path)
    return result["text"]

if __name__ == "__main__":
    video_url = sys.argv[1]

    # 1. 제목 추출
    title = get_video_title(video_url)

    # 2. 오디오 다운로드
    download_audio(video_url)

    # 3. Whisper로 텍스트 추출
    script = transcribe()

    # 4. 로그 출력 (Make에서 파싱용)
    print("🔹VIDEO_TITLE_START🔹")
    print(title.strip())
    print("🔹VIDEO_TITLE_END🔹")

    print("🔸SCRIPT_START🔸")
    print(script.strip())
    print("🔸SCRIPT_END🔸")
