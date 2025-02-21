from fastapi import FastAPI
import yt_dlp

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI YouTube MP3 Backend is Running"}

@app.get("/get_song_url/")
def get_song_url(song_name: str):
    ydl_opts = {'quiet': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{song_name}", download=False)
        if info and 'entries' in info and len(info['entries']) > 0:
            return {"url": info["entries"][0]["webpage_url"]}
        return {"url": None}
