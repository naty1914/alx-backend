#!/usr/bin/python3
""" A module that defines a LIFO caching system"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """It defines a class LIFOCache that inherits from BaseCaching"""
    def __init__(self):
        """It initializes the class"""
        super().__init__()
        self.order_of_insertion = []

    def put(self, key, item):
        """It adds an item in the cached data"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.order_of_insertion.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")
        self.order_of_insertion.append(key)

    def get(self, key):
        """IT retrieves an item by key from the cached data"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
