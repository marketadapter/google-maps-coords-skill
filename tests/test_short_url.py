import pytest
from unittest.mock import MagicMock, patch
from coords.short_url import is_short, resolve


@pytest.mark.parametrize("url, expected", [
    ("https://maps.app.goo.gl/XXXXX", True),
    ("http://maps.app.goo.gl/XXXXX", True),
    ("https://www.google.com/maps/place/Seoul", False),
    ("https://goo.gl/maps/XXXXX", False),
    ("https://maps.google.com/?q=37.5,126.9", False),
])
def test_is_short(url, expected):
    assert is_short(url) == expected


def test_resolve_follows_redirect():
    final_url = "https://www.google.com/maps/place/Seoul/@37.5665,126.9780,17z/data=..."
    mock_result = MagicMock()
    mock_result.stdout = final_url

    with patch("subprocess.run", return_value=mock_result) as mock_run:
        result = resolve("https://maps.app.goo.gl/XXXXX")

    assert result == final_url
    cmd = mock_run.call_args[0][0]
    assert cmd[0] == "curl"
    assert "https://maps.app.goo.gl/XXXXX" in cmd


def test_resolve_returns_original_on_empty_response():
    mock_result = MagicMock()
    mock_result.stdout = "   "

    with patch("subprocess.run", return_value=mock_result):
        result = resolve("https://maps.app.goo.gl/XXXXX")

    assert result == "https://maps.app.goo.gl/XXXXX"
