# 🎥 AI-Video-Streaming-Engine

A Python-based real-time video streaming engine capable of ingesting multiple video sources, upscaling them to 4K, transcoding using Apple Silicon hardware acceleration, generating HLS output, and serving the stream through a local web server.

The long-term goal of this project is to build an **AI-powered streaming platform** with live subtitle translation, AI video enhancement, and low-latency streaming.

---

## 🚀 Features

- ✅ Local MP4 streaming
- ✅ Twitch Live streaming via Streamlink
- ✅ Direct Video URL support
- ✅ 4K video upscaling
- ✅ Apple Silicon hardware encoding (VideoToolbox)
- ✅ HLS (.m3u8) generation
- ✅ Local web server
- ✅ Browser playback using HLS.js
- 🚧 Live AI subtitle translation (Coming Soon)
- 🚧 AI video enhancement (Coming Soon)

---

## 🏗️ Architecture

```text
                   +----------------+
                   |  Video Source  |
                   +----------------+
                           |
          +----------------+----------------+
          |                |                |
       MP4 File        Twitch Live      Direct URL
          |                |                |
          +----------------+----------------+
                           |
                           ▼
                 Source Manager (Python)
                           |
                           ▼
                       FFmpeg Pipeline
                           |
         +-----------------+-----------------+
         |                                   |
         ▼                                   ▼
   4K Upscaling                     VideoToolbox Encoder
         |                                   |
         +-----------------+-----------------+
                           |
                           ▼
                    HLS (.m3u8 + .ts)
                           |
                           ▼
                   Local HTTP Server
                           |
                           ▼
                    Browser Player
```

---

## 🧠 Planned AI Pipeline

```text
                    Audio Stream
                         |
                         ▼
                  Faster-Whisper
                         |
                  Language Detection
                         |
                    Translation
                         |
                         ▼
                 English WebVTT (.vtt)
                         |
                         ▼
             Netflix-style Subtitle Track
                         |
                         ▼
                   Browser Player
```

---

# 📂 Project Structure

```text
Universal-Streaming-Engine/
│
├── main.py
├── player.html
├── README.md
│
├── hls/
│   ├── master.m3u8
│   ├── stream.m3u8
│   ├── subtitles_en.vtt
│   └── *.ts
│
└── temp/
```

---

# ⚙️ Supported Sources

### Local MP4

```python
SOURCE_TYPE = "mp4"
MP4_FILE = "/path/to/video.mp4"
```

### Twitch Live

```python
SOURCE_TYPE = "twitch"
TWITCH_CHANNEL = "Jinnytty"
```

### Direct URL

```python
SOURCE_TYPE = "url"
VIDEO_URL = "https://example.com/video.mp4"
```

---

# 🛠️ Tech Stack

- Python
- FFmpeg
- Streamlink
- HLS.js
- Apple VideoToolbox
- HTTP Live Streaming (HLS)
- HTML5 Video

### Planned

- Faster-Whisper
- OpenAI Whisper
- CoreML
- Metal Performance Shaders
- AI Super Resolution

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/<your-username>/Universal-Streaming-Engine.git

cd Universal-Streaming-Engine
```

---

## Install Python Packages

```bash
pip install streamlink
```

---

## Install FFmpeg

### macOS

```bash
brew install ffmpeg
```

---

## Run

```bash
python main.py
```

Open

```
http://localhost:8012/player.html
```

---

# 🎬 Streaming Pipeline

```text
Video Source
      │
      ▼
Source Manager
      │
      ▼
FFmpeg
      │
      ▼
4K Upscaling
      │
      ▼
VideoToolbox Encoding
      │
      ▼
HLS Playlist
      │
      ▼
Browser
```

---

# 🧠 Future Features

- [ ] Real-time subtitle translation
- [ ] Japanese → English subtitles
- [ ] Korean → English subtitles
- [ ] Chinese → English subtitles
- [ ] AI Super Resolution
- [ ] AI Frame Interpolation
- [ ] AI Face Restoration
- [ ] Noise Reduction
- [ ] Adaptive Bitrate Streaming
- [ ] Multi-language subtitles
- [ ] GPU Processing using Metal
- [ ] Docker Deployment
- [ ] Web Dashboard
- [ ] Performance Monitoring

---

# 📊 Current Status

| Feature | Status |
|----------|--------|
| MP4 Streaming | ✅ |
| Twitch Streaming | ✅ |
| URL Streaming | ✅ |
| 4K Upscaling | ✅ |
| HLS Generation | ✅ |
| VideoToolbox Encoding | ✅ |
| Browser Playback | ✅ |
| AI Subtitle Translation | 🚧 |
| AI Enhancement | 🚧 |

---

# 💡 Vision

The objective of this project is to build an **AI-powered universal video streaming engine** capable of:

- Streaming from multiple video sources
- AI-powered video enhancement
- Real-time subtitle translation
- Low-latency streaming
- Hardware-accelerated encoding
- Netflix-style subtitle support
- Browser-based playback
- Cross-platform deployment

---

# 📜 License

MIT License

---

# 👨‍💻 Author

**Tushar Debbarma**

If you like this project, consider giving it a ⭐ on GitHub!
