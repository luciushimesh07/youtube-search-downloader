from .search import search_youtube
from .downloader import (
    download_video,
    download_audio,
    download_video_only,
)
from .formatter import (
    format_views,
    format_duration,
)
from .environment import check_environment


def choose_quality():

    print("\n" + "=" * 60)
    print("SELECT VIDEO QUALITY")
    print("=" * 60)

    print("""
1. Best available
2. 1080p
3. 720p
4. 480p
5. 360p
""")

    qualities = {
        "1": "best",
        "2": "1080",
        "3": "720",
        "4": "480",
        "5": "360",
    }

    while True:

        choice = input("Enter quality: ").strip()

        if choice in qualities:
            return qualities[choice]

        print("❌ Invalid option.")


def choose_download_type(url):

    print("\n" + "=" * 60)
    print("DOWNLOAD OPTIONS")
    print("=" * 60)

    print("""
1. 🎬 Video + Audio
2. 🎵 Audio only
3. 📹 Video only
""")

    while True:

        choice = input("Enter option: ").strip()

        try:

            if choice == "1":

                quality = choose_quality()

                print(
                    "\n⬇️ Downloading video + audio...\n"
                )

                download_video(url, quality)

                return

            if choice == "2":

                print(
                    "\n⬇️ Downloading audio...\n"
                )

                download_audio(url)

                return

            if choice == "3":

                quality = choose_quality()

                print(
                    "\n⬇️ Downloading video...\n"
                )

                download_video_only(
                    url,
                    quality
                )

                return

            print("❌ Choose 1, 2 or 3.")

        except Exception as error:

            print("\n❌ Download failed:")
            print(error)

            return


def start():

    print("=" * 70)
    print("              YOUTUBE SEARCH DOWNLOADER")
    print("=" * 70)

    try:

        environment = check_environment()

        print(
            f"\nSystem: "
            f"{environment['operating_system']}"
        )

    except Exception as error:

        print("\n❌ Environment setup failed:")
        print(error)

        return

    query = input(
        "\nEnter YouTube search title: "
    ).strip()

    if not query:

        print("❌ Search title cannot be empty.")

        return

    print("\n🔎 Searching YouTube...\n")

    try:

        videos = search_youtube(
            query,
            limit=20
        )

        if not videos:

            print("❌ No videos found.")

            return

        print("=" * 70)
        print("RESULTS — SORTED BY VIEW COUNT")
        print("=" * 70)

        for index, video in enumerate(
            videos,
            start=1
        ):

            title = video.get(
                "title",
                "Unknown title"
            )

            channel = (
                video.get("channel")
                or video.get("uploader")
                or "Unknown"
            )

            views = format_views(
                video.get("view_count")
            )

            duration = format_duration(
                video.get("duration")
            )

            video_id = video.get("id")

            url = (
                "https://www.youtube.com/watch?v="
                + video_id
            )

            print(f"\n[{index}] {title}")
            print(f"    👤 Channel  : {channel}")
            print(f"    👁 Views    : {views}")
            print(f"    ⏱ Duration : {duration}")
            print(f"    🔗 URL      : {url}")

        print("\n" + "=" * 70)

        while True:

            choice = input(
                f"\nSelect a video (1-{len(videos)}): "
            ).strip()

            if not choice.isdigit():

                print("❌ Enter a number.")

                continue

            choice = int(choice)

            if 1 <= choice <= len(videos):

                break

            print(
                f"❌ Choose between 1 and "
                f"{len(videos)}."
            )

        selected = videos[choice - 1]

        selected_url = (
            "https://www.youtube.com/watch?v="
            + selected["id"]
        )

        print("\n" + "=" * 70)
        print("SELECTED VIDEO")
        print("=" * 70)

        print(
            f"\nTitle: {selected.get('title')}"
        )

        choose_download_type(
            selected_url
        )

        print("\n" + "=" * 70)
        print("✅ FINISHED")
        print("=" * 70)

        print(
            "\nFiles are saved in ./downloads/"
        )

    except Exception as error:

        print("\n❌ Something went wrong:")
        print(error)
