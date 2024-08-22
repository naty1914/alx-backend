#!/usr/bin/python3
"""A module that defines a LRU caching system"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """It defines a class LRUCache that inherits from BaseCaching"""
    def __init__(self):
        """It initializes the class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """It adds an item in the cached_data"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.pop(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            least_ru_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD: {}".format(least_ru_key))

    def get(self, key):
        """IT retrieves an item by key from the cached data"""
        if key is None or key not in self.cache_data:
            return None
        val = self.cache_data.pop(key)
        self.cache_data[key] = val
        return val
