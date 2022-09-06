class LRUList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []

    def contains_substring(self, substring):
        for item in self.cache:
            if substring in str(item):
                self.cache.remove(item)
                self.cache.append(item)
                return True
        return False

    def set(self, value):
        if len(self.cache) >= self.capacity:
            self.cache.pop(0)
        self.cache.append(value)

    def __str__(self):
        return str(self.cache)
