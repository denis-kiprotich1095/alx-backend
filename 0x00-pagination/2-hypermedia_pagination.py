#!/usr/bin/env python3
"""Simple helper function"""
import csv
import math
from typing import List
import math


def index_range(page, page_size):
    """return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters"""
    assert (page > 0 and type(page) == int)
    assert (type(page_size) == int)
    last = page * page_size
    first = last - page_size
    tup = ()
    tup = list(tup)
    tup.insert(-1, last)
    tup.insert(0, first)
    tup = tuple(tup)
    return (tup)


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
        """return the appropriate page of the dataset"""
        assert (page > 0 and isinstance(page, int))
        assert (page_size > 0 and isinstance(page_size, int))
        rang = ()
        self.dataset()
        if self.dataset() is None:
            return []
        rang = index_range(page, page_size)
        rang = list(rang)
        return (self.dataset()[rang[0]: rang[-1]])

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns a dictionary containing the following key-value pairs"""
        total = self.dataset()
        total_pages = math.ceil(len(total) / page_size)
        next_page = (page + 1) if (page + 1) < total_pages else None
        prev_page = (page - 1) if (page - 1) > 1 else None
        data = self.get_page(page, page_size)
        hyper = {
                'page_size': page_size,
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
                }
        return (hyper)
