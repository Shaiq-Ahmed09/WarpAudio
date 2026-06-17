import os
import shutil
import json
from datetime import datetime
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI(title="AuraStream Backend")

# Allow the frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Create a local folder to store the music permanently
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# 1.5 Setup a Metadata Database file
METADATA_FILE = os.path.join(UPLOAD_DIR, "metadata.json")
if not os.path.exists(METADATA_FILE):
    with open(METADATA_FILE, "w") as f:
        json.dump([], f)

# 2. Mount the directory so the frontend can stream files directly from it
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")

@app.post("/api/upload")
async def upload_tracks(
    audio: UploadFile = File(...),
    cover: UploadFile = File(None),
    title: str = Form("Unknown Title"),
    artist: str = Form("Unknown Artist")
):
    """Receives a single track with metadata and cover art."""
    
    # 1. Save Audio File
    audio_path = os.path.join(UPLOAD_DIR, audio.filename)
    with open(audio_path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)
        
    # 2. Save Cover Art (If provided)
    cover_url = None
    if cover:
        cover_dir = os.path.join(UPLOAD_DIR, "covers")
        os.makedirs(cover_dir, exist_ok=True)
        cover_path = os.path.join(cover_dir, cover.filename)
        with open(cover_path, "wb") as buffer:
            shutil.copyfileobj(cover.file, buffer)
        cover_url = f"https://auraspace-music-player.onrender.com/{cover.filename}"

    # 3. Create Metadata Record
    upload_time = datetime.now().strftime("%b %d, %Y - %I:%M %p")
    track_metadata = {
        "id": audio.filename,
        "title": title,
        "artist": artist,
        "url": f"https://auraspace-music-player.onrender.com{audio.filename}",
        "cover_url": cover_url,
        "upload_time": upload_time
    }
    
    # 4. Save to Database
    with open(METADATA_FILE, "r") as f:
        db = json.load(f)
    db.append(track_metadata)
    with open(METADATA_FILE, "w") as f:
        json.dump(db, f)
        
    return {"message": "Successfully saved track", "tracks": [track_metadata]}

@app.get("/api/tracks")
def get_tracks():
    """Reads the database and returns all saved music."""
    try:
        with open(METADATA_FILE, "r") as f:
            tracks = json.load(f)
        return {"tracks": tracks}
    except Exception:
        return {"tracks": []}

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)