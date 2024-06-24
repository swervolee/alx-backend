#!/usr/bin/env python3
"""
Simple Pagination
"""
from typing import Tuple, List
import csv


def index_range(page: int, page_size: int) -> Tuple:
    """
    returns start and end index of page
    """
    start = (page - 1) * page_size
    end = page * page_size

    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        for i in [page, page_size]:
            assert isinstance(i, int)
            assert i > 0
        data = self.dataset()
        Range = index_range(page, page_size)
        try:
            result = data[Range[0]: Range[1]]
        except IndexError:
            return []
