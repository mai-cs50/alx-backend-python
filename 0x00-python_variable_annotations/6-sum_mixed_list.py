#!/usr/bin/env python3
"""Write a type-annotated function sum_list"""


from typing import List, Union


def sum_mixed_list(mxd_1st: List[Union[int, float]]) -> float:
    """takes a list mxd_lst of integers and floats and returns their sum as a float"""
    a: float = 0.0
    for x in mxd_1st:
        a += x
    return a
