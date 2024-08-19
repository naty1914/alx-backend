#!/usr/bin/env python3
""" A module that provides a function that returns a tuple"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """"It returns a tuple of size two containing a startindex and
    an end index"""
    startIndex = (page - 1) * page_size
    endIndex = startIndex + page_size
    return (startIndex, endIndex)
