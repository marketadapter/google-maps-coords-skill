import pytest
from coords.maps_url import parse


@pytest.mark.parametrize("url, expected", [
    # @lat,lng,zoom
    (
        "https://www.google.com/maps/place/Seoul/@37.5665,126.9780,15z",
        ("37.5665", "126.9780"),
    ),
    (
        "https://www.google.com/maps/@37.5665,126.9780,17z",
        ("37.5665", "126.9780"),
    ),
    # data= with !3d<lat>!4d<lng>
    (
        "https://www.google.com/maps/place/NAME/data=!3m1!4b1!4m6!3m5!1s0x0!3d37.5665!4d126.9780",
        ("37.5665", "126.9780"),
    ),
    # q=lat,lng
    (
        "https://www.google.com/maps?q=37.5665,126.9780",
        ("37.5665", "126.9780"),
    ),
    (
        "https://www.google.com/maps/search/?q=37.5665,126.9780",
        ("37.5665", "126.9780"),
    ),
    # ll=lat,lng (legacy)
    (
        "https://maps.google.com/?ll=37.5665,126.9780",
        ("37.5665", "126.9780"),
    ),
    # negative coordinates (southern/western hemisphere)
    (
        "https://www.google.com/maps/@-33.8688,151.2093,15z",
        ("-33.8688", "151.2093"),
    ),
])
def test_parse_valid(url, expected):
    assert parse(url) == expected


@pytest.mark.parametrize("url", [
    "https://www.google.com/",
    "https://maps.app.goo.gl/XXXXX",
    # iframe URLs should not match here
    "https://www.google.com/maps/embed?pb=!1m18!2d126.9780!3d37.5665",
])
def test_parse_returns_none(url):
    assert parse(url) is None
