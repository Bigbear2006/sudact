import time
import asyncio
import aiohttp
from utils.parse import parse_article


async def main():
    start = time.time()
    print('start...')
    connector = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(base_url='https://sudact.ru', connector=connector) as session:
        decisions = await parse_article(session, '/law/apk-rf/razdel-i/glava-1/statia-1/')
    end = time.time()
    print(f'Функция выполнена за {end - start} секунд.')
    print(*decisions, sep='\n')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
