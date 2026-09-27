from .search import search_youtube
from .downloader import (
    download_video,
    download_audio,
    download_video_only
)
from .formatter import (
    format_views,
    format_duration
)


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
        "5": "360"
    }

    while True:

        choice = input("Enter quality: ").strip()

        if choice in qualities:
            return qualities[choice]

        print("❌ Invalid option. Try again.")


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

        if choice == "1":

            quality = choose_quality()

            print("\nStarting video + audio download...\n")

            download_video(url, quality)

            return

        elif choice == "2":

            print("\nStarting audio download...\n")

            download_audio(url)

            return

        elif choice == "3":

            quality = choose_quality()

            print("\nStarting video-only download...\n")

            download_video_only(url, quality)

            return

        else:

            print("❌ Invalid option. Please choose 1, 2 or 3.")


def start():

    print("=" * 70)
    print("                 YOUTUBE SEARCH DOWNLOADER")
    print("=" * 70)

    query = input(
        "\nEnter YouTube search title: "
    ).strip()

    if not query:

        print("\n❌ Search title cannot be empty.")
        return

    print("\n🔎 Searching YouTube...\n")

    try:

        videos = search_youtube(query)

        if not videos:

            print("❌ No videos found.")
            return

        print("=" * 70)
        print("SEARCH RESULTS")
        print("=" * 70)

        for i, video in enumerate(videos, start=1):

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
                f"https://www.youtube.com/watch?v="
                f"{video_id}"
            )

            print(f"\n[{i}] {title}")
            print(f"    Channel  : {channel}")
            print(f"    Views    : {views}")
            print(f"    Duration : {duration}")
            print(f"    URL      : {url}")

        print("\n" + "=" * 70)

        while True:

            choice = input(
                f"\nSelect a video (1-{len(videos)}): "
            ).strip()

            if not choice.isdigit():

                print("❌ Please enter a number.")
                continue

            choice = int(choice)

            if 1 <= choice <= len(videos):
                break

            print(
                f"❌ Select a number between "
                f"1 and {len(videos)}."
            )

        selected_video = videos[choice - 1]

        selected_id = selected_video.get("id")

        selected_url = (
            f"https://www.youtube.com/watch?v="
            f"{selected_id}"
        )

        print("\n" + "=" * 70)
        print("SELECTED VIDEO")
        print("=" * 70)

        print(
            f"\nTitle: {selected_video.get('title')}"
        )

        print(f"URL: {selected_url}")

        choose_download_type(selected_url)

        print("\n" + "=" * 70)
        print("✅ DOWNLOAD FINISHED")
        print("=" * 70)

        print(
            "\nYour files are in: ./downloads/"
        )

    except Exception as e:

        print("\n❌ Something went wrong:")
        print(e)