# 🎵 WarpAudio

Bending Sound. Shaping Space.
A sleek, highly customizable local music player that seamlessly bridges your offline library with YouTube's massive catalog.

WarpAudio is built for absolute simplicity. No complicated setups, no heavy bloat—just drop your songs, customize the interface to match your exact vibe, and you are good to go.

---

# ✨ Features

Instant Local Streaming: Drag, drop, and play. Stream your local music library flawlessly with full persistent storage.

Total Customization: The player is completely modular and customizable by you—make it look and feel exactly how you want.

Hybrid Library: Combines your local files with the power of YouTube's search engine (see the API setup below!).

---

# 🛠️ Quick Start

Getting WarpAudio up and running takes less than a minute.

Launch the Backend:
Run the Python development server to initialize the audio engine and persistent storage:

Bash
python server.py

Access the Player:
Open your browser and navigate to:

Code snippet
http://127.0.0.1:8000

Upload your favorite tracks or search the youtube catalog and start listening!

---

# 🔑 The Catch: Activating YouTube Search

To protect environment integrity, the production YouTube API key is fully hidden and secured. To unlock streaming from YouTube's massive library directly inside WarpAudio, you just need to drop in your own free key.

How to get your free key:
Head over to the Google Cloud Console.

Create a quick project and enable the YouTube Data API v3.

Generate an API Key (it's completely free).

Paste your key into your local configuration file (e.g., .env or config.py) to bridge your player to the cloud.

---

# 🎛️ Customization & Tech Stack

Frontend: Vanilla JS / modern CSS variables for effortless, deep theme customization.

Feel free to fork, tweak the UI, and build your ultimate audio deck!
