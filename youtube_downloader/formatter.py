def format_views(views):
    if views is None:
        return "Unknown"

    if views >= 1_000_000_000:
        return f"{views / 1_000_000_000:.1f}B"

    if views >= 1_000_000:
        return f"{views / 1_000_000:.1f}M"

    if views >= 1_000:
        return f"{views / 1_000:.1f}K"

    return str(views)


def format_duration(seconds):
    if not seconds:
        return "Unknown"

    seconds = int(seconds)

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    if hours > 0:
        return f"{hours}:{minutes:02d}:{seconds:02d}"

    return f"{minutes}:{seconds:02d}"