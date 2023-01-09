#!/usr/bin/env python3
"""asyncio syntax"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """execute a random delay"""
    delay: float = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
