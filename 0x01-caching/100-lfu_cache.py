#!/usr/bin/env python3
"""
LFU cache
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    Least Frequently Used cache
    """

    def __init__(self):
        """
        init method
        """
        super().__init__()
        self.freq = {}
        self.min_freq = 0
        self.freq_list = {}

    def freq_update(self, key):
        """
        updates frequency of key
        """
        freq = self.freq[key]
        self.freq[key] += 1

        self.freq_list[freq].remove(key)
        if not self.freq_list[freq]:
            del self.freq_list[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        new_freq = freq + 1
        if new_freq not in self.freq_list:
            self.freq_list[new_freq] = []
        self.freq_list[new_freq].append(key)

    def get(self, key):
        """
        fetches data from cache store
        """
        if key not in self.cache_data:
            return None
        self.freq_update(key)
        return self.cache_data[key]

    def put(self, key, value):
        """
        inserts data into cache
        """
        if key in self.cache_data:
            self.cache_data[key] = value
            self.freq_update(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Evict the least frequently used key
                evict_key = self.freq_list[self.min_freq].pop(0)
                del self.cache_data[evict_key]
                del self.freq[evict_key]
                print(f"DISCARD: {evict_key}")

            self.cache_data[key] = value
            self.freq[key] = 1
            self.min_freq = 1

            if 1 not in self.freq_list:
                self.freq_list[1] = []
            self.freq_list[1].append(key)
