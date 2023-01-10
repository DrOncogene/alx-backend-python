#!/usr/bin/env python3
"""chaining in asyncio"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def get_results(res_arr: List[float], max_delay: int) -> List[float]:
    """calls wait_random and append the result"""
    res = await wait_random(max_delay)
    res_arr.append(res)
    return res_arr


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    gathers results executing
    wait_random n times
    """
    res = []
    await asyncio.gather(*(get_results(res, max_delay) for _ in range(n)))

    return res
