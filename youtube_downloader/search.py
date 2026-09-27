import yt_dlp


def search_youtube(query, limit=20):

    options = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": True,
        "skip_download": True,
    }

    search_query = f"ytsearch{limit}:{query}"

    with yt_dlp.YoutubeDL(options) as ydl:

        result = ydl.extract_info(
            search_query,
            download=False
        )

    videos = result.get("entries", [])

    videos = [
        video
        for video in videos
        if video and video.get("id")
    ]

    videos.sort(
        key=lambda video: video.get("view_count") or 0,
        reverse=True
    )

    return videos
