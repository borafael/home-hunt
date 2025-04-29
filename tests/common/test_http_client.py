
import pytest
import httpx
from unittest.mock import AsyncMock

from common.http_client import HttpClient, HttpResponse

def test_http_response_creation():
    response = HttpResponse(status=200, content=b"test content")
    assert response.status == 200
    assert response.content == b"test content"


def test_http_response_json_decoding():
    response = HttpResponse(status=200, content=b'{"key": "value"}')
    data = response.json()
    assert isinstance(data, dict)
    assert data["key"] == "value"


def test_http_response_text_decoding():
    response = HttpResponse(status=200, content=b"some text")
    text = response.text()
    assert isinstance(text, str)
    assert text == "some text"

@pytest.mark.asyncio
async def test_basic_get():
    client = HttpClient()
    response: HttpResponse = await client.get("https://www.google.com")
    assert 200 == response.status