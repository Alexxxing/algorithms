"""
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。


示例：

输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
"""


class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.dic = {}
        self.first = DLinkedNode(0, 0)
        self.last = DLinkedNode(0, 0)
        self.first.next = self.last
        self.last.prev = self.first

    def put(self, key: int, value: int):
        node = self.dic.get(key)
        if not node:
            node = DLinkedNode(key, value)
            if self.size + 1 > self.capacity:
                last_node = self.last.prev
                last_node_pre = last_node.prev
                last_node.next, last_node.prev = None, None
                last_node_pre.next = self.last
                self.last.prev = last_node_pre
                self.dic.pop(last_node.key)
            self.insert_head(node, False)
            self.size += 1
        else:
            node.value = value
            self.insert_head(node, True)
        self.dic[key] = node

    def get(self, key: int):
        node = self.dic.get(key)
        if not node:
            return -1
        self.insert_head(node, True)
        return node.value

    def insert_head(self, node: DLinkedNode, is_exist: bool):
        """
        :param node: double linked node
        :param is_exist: in LRU or not
        """
        if is_exist:
            node_pre = node.prev
            node_next = node.next
            node_next.prev = node_pre
            node_pre.next = node_next
        first_next = self.first.next
        self.first.next = node
        first_next.prev = node
        node.next = first_next
        node.prev = self.first


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
