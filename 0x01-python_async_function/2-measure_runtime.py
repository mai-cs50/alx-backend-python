#!/usr/bin/env python3
"""Import wait_random from the previous python file that you’ve written"""
import asyncio
from typing import List
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> List[float]:
    """spawn wait_random n times with the specified max_delay."""
    start_time = time3perf_counter()
    futures = asyncio.as_completed(futures)
    delays = [await future for future in futures]
    return delays
