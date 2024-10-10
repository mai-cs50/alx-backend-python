#!/usr/bin/env python3
"""Define type checking"""


from typing import List, Tuple, Any


def zoom_array(lst: Tuple[Any, ...], factor: int = 2) -> List[Any]:
    """Type checking Excercise"""
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range((factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
