#!/usr/bin/env python3
"""async generator"""
import asyncio
import random


async def async_generator():
    """
    yields a random float between
    0 and 10 ten times
    """
    for _ in range(10):
        await asyncio.sleep(1)
        num = random.uniform(0, 10)
        yield num
