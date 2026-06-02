"""Extract coordinates from any Google Maps URL.

Try order:
  1. iframe embed  — !2d<lng>!3d<lat>
  2. regular URL   — @lat,lng / !3d!4d / q= / ll=
  3. short URL     — resolve redirect, then retry regular URL
"""
from .iframe_url import parse as _parse_iframe
from .maps_url import parse as _parse_maps
from .short_url import is_short, resolve


def extract(url: str) -> tuple[str, str]:
    """Return (lat, lng) from any Google Maps URL.

    Raises ValueError if coordinates cannot be found.
    """
    result = _parse_iframe(url) or _parse_maps(url)
    if result:
        return result

    if is_short(url):
        final = resolve(url)
        result = _parse_maps(final)
        if result:
            return result

    raise ValueError(f"Could not extract coordinates from: {url}")
