#!/usr/bin/env python3
"""
asyncio tasks
"""
from asyncio import Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    creates a task for wait_random
    """
    return Task(wait_random(max_delay))
