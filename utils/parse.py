import asyncio
import datetime
from aiohttp import ClientSession
from bs4 import BeautifulSoup

from .functions import get_judge, get_place, normalize_date, handle_error_place
from .models import Decision
from config import DEFAULT_PAGES_COUNT


async def parse_decision(session: ClientSession, url: str, number: str, date: datetime.date, case_number: str) -> Decision:
    """"Парсит город, фамилию и инициалы судьи из текста страницы"""
    async with session.get(url) as response:
        text = await response.text()

    html = BeautifulSoup(text, 'lxml')
    text = html.find('td', class_='h-col1 h-col1-inner3').get_text('\n')
    judge = get_judge(text)
    place = get_place(text)
    place = handle_error_place(text) if place is None else place
    print(url) if place is None else False

    decision = Decision.create(number=number, date=date, case_number=case_number, place=place, judge=judge, text=text)
    return decision


async def parse_page(session: ClientSession, url: str) -> list[Decision]:
    """Парсит решения с одной страницы"""
    async with session.get(url) as response:
        text = await response.text()

    html = BeautifulSoup(text, 'lxml')
    all_li = html.find('ul', class_='results2').find_all('li')
    all_a = [li.find('a') for li in all_li]
    titles = [a.text for a in all_a]

    urls = [a.get('href') for a in all_a]
    numbers = [li.find('span', class_='numb').text.replace('.', '') for li in all_li]
    dates = list(map(lambda x: normalize_date(x), titles))
    case_numbers = list(map(lambda x: x.split('№')[-1].strip(), titles))

    data = zip(urls, numbers, dates, case_numbers)
    tasks = [asyncio.create_task(parse_decision(session, url, num, date, case_num)) for url, num, date, case_num in data]
    completed, _ = await asyncio.wait(tasks)
    decisions = [i.result() for i in completed]
    return decisions


async def parse_article(session: ClientSession, url: str, max_page: int = DEFAULT_PAGES_COUNT) -> list[Decision]:
    """Парсит решения с нескольких страниц одной статьи"""
    tasks = [asyncio.create_task(parse_page(session, url+f'?page={page}')) for page in range(1, max_page+1)]
    completed, _ = await asyncio.wait(tasks)
    decisions = [j for i in completed for j in i.result()]
    return decisions
