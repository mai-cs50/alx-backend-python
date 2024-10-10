#!/usr/bin/env python3
"""Write a type-annotated function to_kv"""


from typing import List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return aTuple of string and a float"""
    return (k, float(v ** 2))
