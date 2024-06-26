#!/usr/bin/env python3
"""
CACHE CLASS
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class
    """
    def __init__(self):
        """
        The init method
        """
        super().__init__()

    def put(self, key, item):
        """
        adds an item to cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Fetches an item from the cache
        """
        return self.cache_data.get(key)
