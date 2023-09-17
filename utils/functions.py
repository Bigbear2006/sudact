import re
from datetime import date


def get_judge(text: str):
    """
    Эта функция выбирает из текста фамилию и инициалы.
    Например:
    Иванов И. Г., Сидоров Л.И., Г. В. Петров, М.И. Белкин
    """
    pattern = re.compile(r'[А-Я][а-я]+\s[А-Я]\.(?:\s+|)[А-Я]\.|[А-Я]\.(?:\s|)[А-Я]\.\s[А-Я][а-я]+')
    judge = pattern.search(text)
    return judge.group()


def get_month_number(month: str):
    months = {
        'янв': 1,
        'фев': 2,
        'мар': 3,
        'апр': 4,
        'мая': 5,
        'июн': 6,
        'июл': 7,
        'авг': 8,
        'сен': 9,
        'окт': 10,
        'ноя': 11,
        'дек': 12,
    }
    return months[month]


def normalize_date(text: str) -> date:
    """
    Эта функция выбирает дату из текста и преобразует её в объект date.
    Пример:
    'Постановление от 10 марта 2023 г. по' -> 2023-03-10
    """
    pattern = re.compile(r'([0-9]{1,2})\s([а-я]+)\s([0-9]{4})')
    day, month, year = pattern.search(text).groups()
    month = get_month_number(month[:3])
    return date(int(year), int(month), int(day))


def get_place(text: str):
    pattern = re.compile(r'(город|г\.|город.) ?([А-Я][а-я]+(?:-[А-Яа-я][а-я]+)*(?:\sНовгород)?)')
    place = pattern.search(text)
    return place.group(2) if place is not None else place


def handle_error_place(text: str):
    """Вызывается в тех случаях, когда функция get_place() возвращает None"""
    places = ['Санкт-Петербург', 'Красноярск', 'Нижний Новгород']
    for place in places:
        if place in text:
            return place
    return None
