class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache():
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _remove_node(self, node):
        pred = node.prev
        succ = node.next

        pred.next = succ
        succ.prev = pred

    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _pop_tail(self):
        popped_node = self.tail.prev
        self._remove_node(popped_node)
        return popped_node

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.data = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = Node(), Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.data.get(key, None)

        if not node:
            return -1

        self._move_to_head(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.data.get(key, None)

        if node:
            node.val = val
            self._move_to_head(node)
        else:
            node_to_add = Node(key, value)
            self.data[key] = node_to_add
            self._add_node(node_to_add)

            self.size += 1

            if self.size > self.capacity:
                node_to_delete = self._pop_tail()
                del self.data[node_to_delete.key]
                self.size -= 1




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
