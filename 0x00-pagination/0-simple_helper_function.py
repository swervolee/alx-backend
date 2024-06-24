#!/usr/bin/env python3
"""
Paging
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    returns start and end index of page
    """
    start = (page - 1) * page_size
    end = page * page_size

    return (start, end)
