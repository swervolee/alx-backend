#!/usr/bin/env python3
"""
LRU cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    Least Recently Used cache
    """

    def __init__(self):
        """
        init method
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add item to cache
        """
        if key and item:
            if key in self.cache_data:
                self.order.remove(key)
            self.cache_data[key] = item
            self.order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lru_key = self.order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

    def get(self, key):
        """
        Get item from cache
        """
        if key in self.cache_data:
            self.order.remove(key)
            self.order.insert(0, key)
            return self.cache_data[key]
        return None
