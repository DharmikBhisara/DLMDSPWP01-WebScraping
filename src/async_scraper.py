import aiohttp
import asyncio
import pandas as pd
import time
from io import StringIO

# List of dataset URLs
urls = [
    "http://localhost:8000/train.csv",
    "http://localhost:8000/test.csv",
    "http://localhost:8000/ideal.csv"
]

async def fetch_csv(session, url):
    async with session.get(url) as response:
        response.raise_for_status()
        text = await response.text()
        df = pd.read_csv(StringIO(text))
        print(f"{url.split('/')[-1]} → {df.shape}")
        return df

async def run_asynchronous():
    start = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_csv(session, url) for url in urls]
        await asyncio.gather(*tasks)

    end = time.time()
    print("Async scraping time:", round(end - start, 2), "seconds")


if __name__ == "__main__":
    asyncio.run(run_asynchronous())
