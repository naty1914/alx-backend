#!/usr/bin/python3
"""A mododule that defines a MRU caching system"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """It defines a class MRUCache that inherits from BaseCaching"""
    def __init__(self):
        """It initializes the class"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.most_recent_key = None

    def put(self, key, item):
        """It adds an item in the cached_data"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.pop(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if self.most_recent_key is not None:
                recent_key = self.most_recent_key
                print(f"DISCARD: {recent_key}")
                self.cache_data.pop(recent_key)
        self.cache_data[key] = item
        self.most_recent_key = key

    def get(self, key):
        """IT retrieves an item by key from the cached data"""
        if key is None or key not in self.cache_data:
            return None
        self.most_recent_key = key
        return self.cache_data[key]
