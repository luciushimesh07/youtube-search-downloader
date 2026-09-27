import os

import yt_dlp

from .environment import get_ffmpeg_directory


DOWNLOAD_FOLDER = "downloads"


def download_video(url, quality):

    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

    # Get the directory containing both
    # ffmpeg and ffprobe.
    ffmpeg_directory = get_ffmpeg_directory()

    if quality == "best":

        format_string = "bv*+ba/b"

    else:

        format_string = (
            f"bv*[height<={quality}]+ba/"
            f"b[height<={quality}]"
        )

    options = {
        "format": format_string,

        "outtmpl": (
            f"{DOWNLOAD_FOLDER}/"
            "%(title)s.%(ext)s"
        ),

        # Tell yt-dlp where FFmpeg and FFprobe are.
        "ffmpeg_location": ffmpeg_directory,

        "merge_output_format": "mp4",

        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])


def download_audio(url):

    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

    # Get the directory containing both
    # ffmpeg and ffprobe.
    ffmpeg_directory = get_ffmpeg_directory()

    options = {
        "format": "bestaudio/best",

        "outtmpl": (
            f"{DOWNLOAD_FOLDER}/"
            "%(title)s.%(ext)s"
        ),

        "ffmpeg_location": ffmpeg_directory,

        "noplaylist": True,

        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])


def download_video_only(url, quality):

    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

    # Video-only doesn't normally require merging,
    # but using the same environment keeps the
    # downloader consistent.
    ffmpeg_directory = get_ffmpeg_directory()

    if quality == "best":

        format_string = "bv*"

    else:

        format_string = (
            f"bv*[height<={quality}]"
        )

    options = {
        "format": format_string,

        "outtmpl": (
            f"{DOWNLOAD_FOLDER}/"
            "%(title)s.%(ext)s"
        ),

        "ffmpeg_location": ffmpeg_directory,

        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])
