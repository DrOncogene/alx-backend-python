#!/usr/bin/env python3
"""
async comprehension
"""
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list:
    """loops over async generator 10 times"""
    return [num async for num in async_generator()]
