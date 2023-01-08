#!/usr/bin/env python3
"""
more complex types
"""
from typing import List, Tuple, Sequence, Iterable

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuple from a list"""
    return [(i, len(i)) for i in lst]
