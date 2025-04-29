from httpx import AsyncClient, Response as HttpxResponse

class HttpResponse:

    def __init__(self, status: int, content: bytes):
        self.status = status
        self.content = content

    def json(self):
        import json
        return json.loads(self.content.decode())

    def text(self) -> str:
        return self.content.decode("utf-8")


class HttpClient:

    async def get(self, url: str) -> HttpResponse:
        async with AsyncClient() as client:
            response: HttpxResponse = await client.get(url)
            return HttpResponse(status=response.status_code, content=response.content)