from typing import List, Union

from flask import abort

from functions import limit, das_filter, unique_, sorted_, das_mapping, das_regex

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
В данном файле производится обработка post-запросов на сервер 
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def filter_in_cmd1(cmd2: str, value1: str, value2: Union[int, str]) -> List[str]:
    try:
        data: List[str] = das_filter(str_=value1)
        if cmd2 == 'map':
            return das_mapping(col=value2, data=data)
        elif cmd2 == 'limit':
            return limit(value=value2, data=data)
        elif cmd2 == 'unique':
            return unique_(data=data)
        elif cmd2 == 'sort':
            return sorted_(data=data, asc=value2)
        elif cmd2 == 'regex':
            return das_regex(reg=value2, data=data)
        abort(400)
    except Exception as e:
        abort(400, e)


def map_in_cmd1(cmd2: str, value1: Union[int, str], value2: Union[int, str]) -> List[str]:
    try:
        data: List[str] = das_mapping(col=value1)
        if cmd2 == 'unique':
            return unique_(data=data)
        elif cmd2 == 'limit':
            return limit(value=value2, data=data)
        elif cmd2 == 'filter':
            return das_filter(str_=value2, data=data)
        elif cmd2 == 'sort':
            return sorted_(data=data, asc=value2)
        elif cmd2 == 'regex':
            return das_regex(data=data, reg=value2)
        abort(400)
    except Exception as e:
        abort(400, e)


def sort_in_cmd1(cmd2: str, value1: str, value2: Union[int, str]) -> List[str]:
    try:
        data: List[str] = sorted_(asc=value1)
        if cmd2 == 'limit':
            return limit(value=value2, data=data)
        elif cmd2 == 'filter':
            return das_filter(str_=value2, data=data)
        elif cmd2 == 'unique':
            return unique_(data=data)
        elif cmd2 == 'map':
            return das_mapping(col=value2, data=data)
        elif cmd2 == 'regex':
            return das_regex(data=data, reg=value2)
        abort(400)
    except Exception as e:
        abort(400, e)


def limit_in_cmd1(cmd2: str, value1: Union[int, str], value2: Union[int, str]) -> List[str]:
    try:
        data: List[str] = limit(value=value1)
        if cmd2 == 'map':
            return das_mapping(col=value2, data=data)
        elif cmd2 == 'filter':
            return das_filter(str_=value2, data=data)
        elif cmd2 == 'sort':
            return sorted_(data=data, asc=value2)
        elif cmd2 == 'unique':
            return unique_(data=data)
        elif cmd2 == 'regex':
            return das_regex(data=data, reg=value2)
        abort(400)
    except Exception as e:
        abort(400, e)


def regex_in_cmd1(cmd2: str, value1: str, value2: Union[int, str]) -> List[str]:
    try:
        data: List[str] = das_regex(reg=value1)
        if cmd2 == 'map':
            return das_mapping(col=value2, data=data)
        elif cmd2 == 'filter':
            return das_filter(str_=value2, data=data)
        elif cmd2 == 'sort':
            return sorted_(data=data, asc=value2)
        elif cmd2 == 'unique':
            return unique_(data=data)
        elif cmd2 == 'limit':
            return limit(value=value2, data=data)
        abort(400)
    except Exception as e:
        abort(400, e)
