#!/usr/bin/python3
"""A module that defines a basic cache class"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """It defines a basic caching system"""
    def put(self, key, item):
        """it adds an item in the cached data"""
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        """It retrieves an item by key from the cached data"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key, None)
