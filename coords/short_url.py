"""Resolve Google Maps short URLs (maps.app.goo.gl) to their final destination.

Resolution is done via curl to follow HTTP redirects. Requires curl on PATH.
"""
import re
import subprocess


_SHORT_HOST = re.compile(r'^https?://maps\.app\.goo\.gl/')


def is_short(url: str) -> bool:
    """Return True if url is a Google Maps short URL."""
    return bool(_SHORT_HOST.match(url))


def resolve(url: str) -> str:
    """Follow HTTP redirects and return the final URL.

    Falls back to the original url if curl returns an empty response.
    """
    result = subprocess.run(
        ["curl", "-sL", "-o", "/dev/null", "-w", "%{url_effective}", url],
        capture_output=True,
        text=True,
        timeout=15,
    )
    final = result.stdout.strip()
    return final if final else url
