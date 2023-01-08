#!/usr/bin/env python3
"""
compose tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """composes a tuple"""
    return (k, v ** 2)
