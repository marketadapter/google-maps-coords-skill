import pytest
from coords.iframe_url import parse


@pytest.mark.parametrize("url, expected", [
    # standard iframe embed — !2d<lng>!3d<lat>
    (
        "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3164.0!2d126.9780!3d37.5665!2m3",
        ("37.5665", "126.9780"),
    ),
    # southern hemisphere, western longitude
    (
        "https://www.google.com/maps/embed?pb=!1m18!2d-43.1729!3d-22.9068!2m3",
        ("-22.9068", "-43.1729"),
    ),
])
def test_parse_valid(url, expected):
    assert parse(url) == expected


@pytest.mark.parametrize("url", [
    "https://www.google.com/maps/place/Seoul/@37.5665,126.9780,15z",
    "https://maps.app.goo.gl/XXXXX",
    "https://www.google.com/maps?q=37.5665,126.9780",
])
def test_parse_returns_none(url):
    assert parse(url) is None
