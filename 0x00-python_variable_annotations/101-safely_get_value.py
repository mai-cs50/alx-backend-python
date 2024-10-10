#!/usr/bin/env python3
"""Advanced type annotate function"""


from typing import Any, Mapping, TypeVar, Union


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]
                     = None) -> Union[Any, T]:
    """More type annotation"""
    if key in dct:
        return dct[key]
    else:
    return default
