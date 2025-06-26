import asyncio

async def download_data(source, delay):
    print(f"Starting download from {source}...")
    await asyncio.sleep(delay)
    return f"Data from {source}"

async def main():
    sources = [
        ("Source A", 2),
        ("Source B", 1),
        ("Source C", 3),
    ]

    tasks = [download_data(source, delay) for source, delay in sources]
    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)

