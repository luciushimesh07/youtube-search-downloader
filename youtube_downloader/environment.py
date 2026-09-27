import os
import platform
import shutil

from static_ffmpeg import run


def get_operating_system():
    system = platform.system()

    if system == "Darwin":
        return "macOS"

    if system == "Windows":
        return "Windows"

    if system == "Linux":
        return "Linux"

    return system


def get_ffmpeg_paths():

    system_ffmpeg = shutil.which("ffmpeg")
    system_ffprobe = shutil.which("ffprobe")

    if system_ffmpeg and system_ffprobe:
        return system_ffmpeg, system_ffprobe

    try:

        ffmpeg, ffprobe = (
            run.get_or_fetch_platform_executables_else_raise()
        )

        return ffmpeg, ffprobe

    except Exception as error:

        raise RuntimeError(
            "FFmpeg/FFprobe could not be installed automatically."
        ) from error


def get_ffmpeg_directory():

    ffmpeg, ffprobe = get_ffmpeg_paths()

    ffmpeg_dir = os.path.dirname(ffmpeg)

    if os.path.dirname(ffprobe) != ffmpeg_dir:

        raise RuntimeError(
            "FFmpeg and FFprobe are located "
            "in different directories."
        )

    return ffmpeg_dir


def check_environment():

    ffmpeg, ffprobe = get_ffmpeg_paths()

    return {
        "operating_system": get_operating_system(),
        "ffmpeg": ffmpeg,
        "ffprobe": ffprobe,
    }
