#!/usr/bin/env python3
"""
fuction factory
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """sums a list of floats"""
    def inner(num: float) -> float:
        return multiplier * num

    return inner
