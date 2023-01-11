#!/usr/bin/env python3
"""async generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    yields a random float between
    0 and 10 ten times
    """
    for _ in range(10):
        await asyncio.sleep(1)
        num = random.random() * 10
        yield num
