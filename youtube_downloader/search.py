import yt_dlp


def search_youtube(query, limit=10):

    options = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": True,
        "skip_download": True
    }

    search_query = f"ytsearch{limit}:{query}"

    with yt_dlp.YoutubeDL(options) as ydl:
        result = ydl.extract_info(
            search_query,
            download=False
        )

    return result.get("entries", [])