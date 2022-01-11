class LRUCache:
    lru = []
    cache = {}
    capacity = 0
    
    def __init__(self, capacity: int):
        self.cache = {}
        self.lru = []
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.cache.keys():
            i = self.lru.index(key)
            self.lru.append(self.lru.pop(i))
            return self.cache.get(key)
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            i = self.lru.index(key)
            self.lru.append(self.lru.pop(i))
            self.cache[key] = value
            
        else:
            
            self.lru.append(key)
            self.cache[key] = value
        
            if len(self.cache) > self.capacity:
                self.cache.pop(self.lru.pop(0))