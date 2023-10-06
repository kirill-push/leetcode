class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.counter = 0
        self.edge = {"old": -1, "new": -1}

    def get(self, key: int) -> int:
        if key in self.cache:
            if self.counter == 1:
                return self.cache[key]["data"]
            elif self.edge["new"] == key:
                return self.cache[key]["data"]
            else:
                node = self.cache[key]
                next_key = node["next"]
                prev_key = node["prev"]
                self.cache[next_key]["prev"] = prev_key
                if self.edge["old"] != key:
                    self.cache[prev_key]["next"] = next_key
                else:
                    self.edge["old"] = next_key
                new_key = self.edge["new"]
                self.edge["new"] = key
                self.cache[new_key]["next"] = key
                self.cache[key]["prev"] = new_key
                self.cache[key]["next"] = None
                return self.cache[key]["data"]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 1:
            if key in self.cache:
                self.cache[key] = value
            else:
                self.edge["old"] = key
                self.cache = {key: {"prev": None, "next": None, "data": value}}
                self.counter = 1
        else:
            if self.counter == 0:
                self.edge["old"] = key
                self.edge["new"] = key
                self.cache[key] = {"prev": None, "next": None, "data": value}
                self.counter += 1
            elif self.counter != self.capacity:
                new_key = self.edge["new"]
                if key not in self.cache:
                    self.cache[key] = {
                        "prev": new_key,
                        "next": None,
                        "data": value,
                    }
                    self.cache[new_key]["next"] = key
                    self.edge["new"] = key
                    self.counter += 1
                else:
                    self.get(key)
                    self.cache[key]["data"] = value
            elif self.counter == self.capacity:
                if key not in self.cache:
                    # delete oldes
                    old_key = self.edge["old"]
                    next_key = self.cache[old_key]["next"]
                    self.edge["old"] = next_key
                    self.cache[next_key]["prev"] = None
                    self.cache.pop(old_key)
                    # add to newest
                    new_key = self.edge["new"]
                    self.edge["new"] = key
                    self.cache[new_key]["next"] = key
                    self.cache[key] = {
                        "prev": new_key,
                        "next": None,
                        "data": value,
                    }
                else:
                    self.get(key)
                    self.cache[key]["data"] = value
