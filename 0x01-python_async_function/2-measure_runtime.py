#!/usr/bin/env python3
"""Import wait_random from the previous python file that you’ve written"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """spawn wait_random n times with the specified max_delay."""
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    return (end_time - start_time) / n
