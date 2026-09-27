import platform
import shutil

import imageio_ffmpeg


def get_operating_system():
    system = platform.system()

    if system == "Darwin":
        return "macOS"

    if system == "Windows":
        return "Windows"

    if system == "Linux":
        return "Linux"

    return system


def find_system_ffmpeg():
    return shutil.which("ffmpeg")


def get_ffmpeg_path():
    """
    Use a system FFmpeg if available.
    Otherwise use the FFmpeg executable
    supplied through imageio-ffmpeg.
    """

    system_ffmpeg = find_system_ffmpeg()

    if system_ffmpeg:
        return system_ffmpeg

    try:
        return imageio_ffmpeg.get_ffmpeg_exe()

    except Exception as error:
        raise RuntimeError(
            "FFmpeg could not be located."
        ) from error


def check_environment():

    return {
        "operating_system": get_operating_system(),
        "ffmpeg": get_ffmpeg_path()
    }
