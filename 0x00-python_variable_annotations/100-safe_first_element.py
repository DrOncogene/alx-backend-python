#!/usr/bin/env python3
"""
duck-type annotations
"""
from typing import Any, Union


def safe_first_element(lst: Any) -> Union[Any, None]:
    """duck typing"""
    if lst:
        return lst[0]
    else:
        return None
