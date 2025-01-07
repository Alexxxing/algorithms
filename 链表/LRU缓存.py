class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.first = DLinkedNode(0, 0)
        self.last = DLinkedNode(0, 0)
        self.size = 0
        self.first.next = self.last
        self.last.prev = self.first
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        else:
            cur_node = self.dic[key]
            self.insert_ahead(cur_node, if_exist=True)
            return cur_node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.dic:
            cur_node = DLinkedNode(key, value)
            if self.size + 1 <= self.capacity:
                self.insert_ahead(cur_node)
                self.size += 1
                self.dic[key] = cur_node
            else:
                self.insert_ahead(cur_node, if_exist=False)
                last_pre = self.last.prev
                last_pre_pre = last_pre.prev
                last_pre_pre.next = self.last
                self.last.prev = last_pre_pre
                last_pre.prev = None
                last_pre.next = None
                self.dic.pop(last_pre.key)
            self.dic[key] = cur_node
            print(self.dic)
        else:
            cur_node = self.dic[key]
            cur_node.value = value
            self.insert_ahead(cur_node, if_exist=True)

    def insert_ahead(self, node, if_exist=False):
        if if_exist:
            cur_pre = node.prev
            cur_next = node.next
            cur_pre.next = cur_next
            cur_next.prev = cur_pre

        first_next = self.first.next
        self.first.next = node
        first_next.prev = node
        node.next = first_next
        node.prev = self.first


class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


if __name__ == '__main__':
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    print(lRUCache.get(1))
    lRUCache.put(3, 3)
    print(lRUCache.get(2))
    lRUCache.put(4, 4)
    print(lRUCache.get(1))
    print(lRUCache.get(3))
    print(lRUCache.get(4))
