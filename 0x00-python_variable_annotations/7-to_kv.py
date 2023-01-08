#!/usr/bin/env python3
"""
compose tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    """sums a list of floats"""
    return (k, v)
