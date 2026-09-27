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
    """
    Return paths to both FFmpeg and FFprobe.

    If the user already has FFmpeg installed,
    use the system versions.

    Otherwise static-ffmpeg downloads/provides
    the appropriate platform binaries.
    """

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


def check_environment():

    ffmpeg, ffprobe = get_ffmpeg_paths()

    return {
        "operating_system": get_operating_system(),
        "ffmpeg": ffmpeg,
        "ffprobe": ffprobe,
    }
