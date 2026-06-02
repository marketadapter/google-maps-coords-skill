#!/usr/bin/env python3
"""Extract lat/lng from a Google Maps URL.

Usage:
    python extract.py <google_maps_url>
    uv run extract.py <google_maps_url>
"""
import sys
from coords import extract


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python extract.py <google_maps_url>", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1].strip()
    try:
        lat, lng = extract(url)
        print(f"위도 (lat): {lat}")
        print(f"경도 (lng): {lng}")
    except ValueError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
