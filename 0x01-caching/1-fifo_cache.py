#!/usr/bin/env
"""
FiFo cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    First in first out cache
    """

    def __init__(self):
        """
        init method
        """
        super().__init__()

    def put(self, key, item):
        """
        adds item to cache
        """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            deleted_item = next(iter(self.cache_data))
            self.cache_data.pop(deleted_item)
            print(f"DISCARD: {deleted_item}")

    def get(self, key):
        """
        Get method
        """
        super().get(key)
