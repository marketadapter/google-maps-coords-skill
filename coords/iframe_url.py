"""Parse Google Maps iframe embed URLs for latitude and longitude.

In the pb= parameter, longitude is encoded as !2d and latitude as !3d —
the order is reversed compared to data= place URLs.
"""
import re


def parse(url: str) -> tuple[str, str] | None:
    """Return (lat, lng) from a Google Maps iframe embed URL, or None."""
    m = re.search(r'!2d(-?\d+\.\d+).*?!3d(-?\d+\.\d+)', url)
    if m:
        lng, lat = m.group(1), m.group(2)
        return lat, lng
    return None
