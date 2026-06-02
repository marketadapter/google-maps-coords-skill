"""Parse regular Google Maps URLs for latitude and longitude.

Handles:
  @lat,lng,zoom   — most place and search URLs
  !3d<lat>!4d<lng> — place URLs with a data= parameter
  q=lat,lng        — search/query URLs
  ll=lat,lng       — legacy format
"""
import re

_PATTERNS: list[tuple[str, int, int]] = [
    (r'@(-?\d+\.\d+),(-?\d+\.\d+)', 1, 2),
    (r'!3d(-?\d+\.\d+)!4d(-?\d+\.\d+)', 1, 2),
    (r'[?&]q=(-?\d+\.\d+),(-?\d+\.\d+)', 1, 2),
    (r'[?&]ll=(-?\d+\.\d+),(-?\d+\.\d+)', 1, 2),
]


def parse(url: str) -> tuple[str, str] | None:
    """Return (lat, lng) from a regular Google Maps URL, or None."""
    for pattern, lat_group, lng_group in _PATTERNS:
        m = re.search(pattern, url)
        if m:
            return m.group(lat_group), m.group(lng_group)
    return None
