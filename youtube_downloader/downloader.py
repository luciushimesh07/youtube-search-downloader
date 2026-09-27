import os

import yt_dlp

from .environment import get_ffmpeg_path


DOWNLOAD_FOLDER = "downloads"


def download_video(url, quality):

    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

    ffmpeg_path = get_ffmpeg_path()

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

        "merge_output_format": "mp4",

        "ffmpeg_location": ffmpeg_path,

        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])


def download_audio(url):

    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

    ffmpeg_path = get_ffmpeg_path()

    options = {

        "format": "bestaudio/best",

        "outtmpl": (
            f"{DOWNLOAD_FOLDER}/"
            "%(title)s.%(ext)s"
        ),

        "ffmpeg_location": ffmpeg_path,

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

    ffmpeg_path = get_ffmpeg_path()

    if quality == "best":

        format_string = "bv*"

    else:

        format_string = f"bv*[height<={quality}]"

    options = {

        "format": format_string,

        "outtmpl": (
            f"{DOWNLOAD_FOLDER}/"
            "%(title)s.%(ext)s"
        ),

        "ffmpeg_location": ffmpeg_path,

        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])
