import subprocess
import os
import time

os.environ["PATH"] += ":/opt/homebrew/bin"

# =====================================
# CONFIG
# =====================================

SOURCE_TYPE = "twitch"  # mp4 | twitch | url

MP4_FILE = "/Users/tushardebbarma/Videos/sample.mp4"

TWITCH_CHANNEL = "JOEYKAOTYK"

VIDEO_URL = "https://example.com/video.mp4"

OUTPUT_DIR = "hls"

PORT = 8012

os.makedirs(OUTPUT_DIR, exist_ok=True)

# =====================================
# INPUT SOURCE
# =====================================

stream_process = None

if SOURCE_TYPE == "mp4":

    input_source = MP4_FILE

elif SOURCE_TYPE == "twitch":

    streamlink_cmd = [
        "streamlink",
        f"https://twitch.tv/{TWITCH_CHANNEL}",
        "best",
        "-O"
    ]

    print("Starting Streamlink...")
    stream_process = subprocess.Popen(
        streamlink_cmd,
        stdout=subprocess.PIPE,
        bufsize=10**8
    )

    time.sleep(3)

    input_source = "pipe:0"

elif SOURCE_TYPE == "url":

    input_source = VIDEO_URL

else:
    raise ValueError("Unsupported SOURCE_TYPE")



# =====================================
# FFMPEG
# =====================================

ffmpeg_cmd = [
    "ffmpeg",
    "-y",
]

if SOURCE_TYPE == "twitch":
    ffmpeg_cmd += ["-i", "pipe:0"]
else:
    ffmpeg_cmd += ["-re", "-i", input_source]

ffmpeg_cmd += [

    # 4K upscale
    "-vf",
    "scale=3840:2160:flags=lanczos,unsharp=7:7:1.0,format=yuv420p",

    # Apple Silicon hardware encoder
    "-c:v",
    "h264_videotoolbox",

    "-profile:v",
    "high",

    "-b:v",
    "18000k",

    "-maxrate",
    "20000k",

    "-bufsize",
    "40000k",

    "-c:a",
    "aac",

    "-f",
    "hls",

    "-hls_time",
    "2",

    "-hls_list_size",
    "5",

    "-hls_flags",
    "delete_segments+append_list+independent_segments",

    f"{OUTPUT_DIR}/stream.m3u8"
]

print("Starting FFmpeg...")

if SOURCE_TYPE == "twitch":

    ffmpeg = subprocess.Popen(
        ffmpeg_cmd,
        stdin=stream_process.stdout
    )

else:

    ffmpeg = subprocess.Popen(ffmpeg_cmd)

# =====================================
# WEB SERVER
# =====================================

server = subprocess.Popen([
    "python3",
    "-m",
    "http.server",
    str(PORT),
    "--directory",
    OUTPUT_DIR
])

print()
print("=" * 40)
print("WATCH:")
print(f"http://localhost:{PORT}/stream.m3u8")
print("=" * 40)

ffmpeg.wait()