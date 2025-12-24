class Node:
    def __init__(self, key:int, value:int):
        self.key = key
        self.value = value
        self.nxt = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.nxt, self.left.prev = self.right, None
        self.right.nxt, self.right.prev = None, self.left

    def remove(self, node: Node) -> None:
        # remove key from current position
        prev, nxt = node.prev, node.nxt
        prev.nxt = nxt
        nxt.prev = prev

    def add(self, node: Node) -> None:
        # Add key to most recently used position
        cur = self.left.nxt
        self.left.nxt = cur.prev = node
        node.prev = self.left
        node.nxt = cur

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        new_node = Node(key, value)
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(new_node)
            self.cache[key] = new_node
        else:
            self.add(new_node)
            self.cache[key] = new_node
            if len(self.cache) > self.capacity:
                lru_node = self.right.prev
                self.remove(lru_node)
                del self.cache[lru_node.key]