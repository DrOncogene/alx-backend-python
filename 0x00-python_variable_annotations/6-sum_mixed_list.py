#!/usr/bin/env python3
"""
sums a mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """sums a list of floats"""
    return sum(mxd_list)
