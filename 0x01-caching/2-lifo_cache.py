#!/usr/bin/env python3
"""
LIFO cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Last In First Out cache
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
                last_key = list(self.cache_data.keys())[-2]
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

    def get(self, key):
        """
        Get method
        """
        return self.cache_data.get(key)
