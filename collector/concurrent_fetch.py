import httpx
import asyncio


async def fetch(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return url, response


async def batch_fetch(urls: list[str]) -> list[str]:
    tasks = [fetch(url) for url in urls]
    # Use asyncio.gather to run tasks concurrently
    responses = await asyncio.gather(*tasks)
    return [(url, response.text) for url, response in responses if response.status_code == 200]
