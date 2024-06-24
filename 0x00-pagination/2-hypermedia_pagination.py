#!/usr/bin/env python3
"""
Simple Pagination
"""
from typing import Tuple, List, Dict
import csv
import math


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
        """
        Returns a page from the Popular baby names csv
        """
        for i in [page, page_size]:
            assert type(i) is int and i > 0
        data = self.dataset()
        Range = index_range(page, page_size)
        try:
            result = data[Range[0]: Range[1]]
            return result
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
            Provide pagination information with details on the page.
        """
        data = self.dataset()
        data_length = len(data)
        total_pages = math.ceil(data_length / page_size)
        page_data = self.get_page(page, page_size)
        next_page = page + 1 if page + 1 <= total_pages else None
        prev_page = page - 1 if page - 1 >= 1 else None

        info = {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
        return info
