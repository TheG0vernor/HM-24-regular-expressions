from typing import List, Iterable, Union, Any
import re

from flask import abort

from constants import LOG_DIR


def das_mapping(col: Any, data: Iterable[str] = None) -> List[str]:
    """Принимает номер колонки (может принять массив) и возвращает требуемую колонку из массива"""
    if data is None:
        data = das_data()
    col = int(col)
    result: Iterable[str] = map(lambda v: v.split(' ')[col] + '\n', data)
    return list(result)


def das_filter(str_: Any, data: Iterable[str] = None) -> List[str]:
    """Принимает значение (может принять массив) и возвращает строки с этим значением"""
    if data is None:
        data = das_data()
    result: Iterable[str] = filter(lambda v: v if str_ in v else None, data)
    return list(result)


def unique_(data: Iterable[str]) -> List[str]:
    """Вернет массив с уникальными значениями"""
    return list(set(data))


def sorted_(asc: Any, data: Iterable[str] = None) -> List[str]:
    """Сортирует массив"""
    if data is None:
        data = das_data()
    if asc == 'asc':
        return sorted(data)
    elif asc == 'desc':
        return sorted(data, reverse=True)
    abort(400)


def limit(value: Any, data: Iterable[str] = None) -> List[str]:
    """Лимитирует вывод данных с массива"""
    if data is None:
        data = das_data()
    value = int(value)
    counter = 0
    result = []
    while counter < value:
        for i in data:
            result.append(i)
            counter += 1
            if counter == value:
                break

    return result


def das_regex(reg: Union[str, int], data: Iterable[str] = None) -> List[str]:
    """Принимает регулярное выражение (может принять массив) и возвращает строки с этим значением"""
    if data is None:
        data = das_data()
    regex = re.compile(fr"{reg}")
    result: List[str] = [i for i in data if regex.search(i)]
    return result


def das_data() -> List[str]:
    """Формирует массив с данными"""
    with open(LOG_DIR) as f:
        data = map(lambda v: v, f)
        return list(data)
