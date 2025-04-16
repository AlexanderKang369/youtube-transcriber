def get_video_title(url):
    ydl_opts = {
        'quiet': True,
        'cookiefile': 'cookies.txt',  # ← 쿠키 파일을 명시적으로 지정!
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info.get("title")

def download_audio(url, output_path="input.mp4"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'quiet': True,
        'cookiefile': 'cookies.txt',  # ← 여기에도 추가!
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
