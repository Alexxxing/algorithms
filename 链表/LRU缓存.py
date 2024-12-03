class LRUCache:

    def __init__(self, capacity: int):
        self.hash_map = dict()
        self.dummy_head = DLinkedNode(0)
        self.dummy_tail = DLinkedNode(0)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if not self.hash_map.get(key):
            print(-1)
        else:
            cur_node = self.hash_map.get(key)
            self.change_prev_node(cur_node)
            print(self.hash_map.get(key).value)

    def put(self, key: int, value: int) -> None:
        node = DLinkedNode(key, value)
        if self.hash_map.get(key):
            old_node = self.hash_map.get(key)
            old_node.value = value
            self.change_prev_node(old_node)
        elif self.size + 1 > self.capacity:
            expire_node = self.dummy_tail.prev
            self.hash_map.pop(expire_node.key)

            expire_prev_node = expire_node.prev
            expire_prev_node.next = self.dummy_tail
            self.dummy_tail.prev = expire_prev_node

            next_node = self.dummy_head.next
            next_node.prev, self.dummy_head.next = node, node
            node.prev, node.next = self.dummy_head, next_node

            self.hash_map[key] = node
        else:
            next_node = self.dummy_head.next
            next_node.prev = node
            self.dummy_head.next = node
            node.next = next_node
            node.prev = self.dummy_head
            self.hash_map[key] = node
            self.size += 1

    def change_prev_node(self, node):
            pre_node = node.prev
            next_node = node.next
            pre_node.next = next_node
            next_node.prev = pre_node

            head_node = self.dummy_head.next
            node.prev = self.dummy_head
            node.next = head_node
            self.dummy_head.next = node
            head_node.prev = node


class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


if __name__ == '__main__':
    lRUCache = LRUCache(2)
    lRUCache.get(2)
    lRUCache.put(2, 6)
    lRUCache.get(1)
    lRUCache.put(1, 5)
    lRUCache.put(1, 2)
    lRUCache.get(1)
    lRUCache.get(2)
