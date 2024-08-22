#!/usr/bin/python3
"""A module that defines a LRU caching system"""
from base_caching import BaseCaching
from collections import OrderedDict, defaultdict


class LFUCache(BaseCaching):
    """It defines a class LFUCache that inherits from BaseCaching"""
    def __init__(self):
        """It initializes the class"""
        super().__init__()
        self.cache_data = {}
        self.item_frequency = defaultdict(int)
        self.accessed_order = OrderedDict()

    def put(self, key, item):
        """It adds an item in the cached_data"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.item_frequency[key] += 1
            self.accessed_order.move_to_end(key)
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_frequency = min(self.item_frequency.values())
            for k, v in self.item_frequency.items():
                if v == min_frequency:
                    least_used_key = k
                    break
            print("DISCARD: {}".format(least_used_key))
            self.cache_data.pop(least_used_key)
            self.item_frequency.pop(least_used_key)
        self.cache_data[key] = item
        self.item_frequency[key] += 1
        self.accessed_order[key] = len(self.accessed_order)

    def get(self, key):
        """IT retrieves an item by key from the cached_data"""
        if key is None or key not in self.cache_data:
            return None
        self.item_frequency[key] += 1
        self.accessed_order.move_to_end(key)
        return self.cache_data[key]
