#!/usr/bin/env python3
"""asyncio syntax"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def get_results(res_arr: list, max_delay: int) -> list:
    """calls wait_random and append the result"""
    res = await wait_random(max_delay)
    res_arr.append(res)
    return res_arr


async def wait_n(n: int, max_delay: int):
    """runs a function async"""
    res = []
    await asyncio.gather(*(get_results(res, max_delay) for _ in range(n)))

    return res
