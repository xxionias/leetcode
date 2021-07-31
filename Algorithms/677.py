"""
677. Map Sum Pairs - Medium

Implement the MapSum class:

- MapSum() Initializes the MapSum object.
- void insert(String key, int val) Inserts the key-val pair into the map. If the key
already existed, the original key-value pair will be overridden to the new one.
- int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.


Example 1:

Input
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
Output
[null, null, 3, null, 5]

Explanation
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);
mapSum.sum("ap");           // return 3 (apple = 3)
mapSum.insert("app", 2);
mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)


Constraints:

1 <= key.length, prefix.length <= 50
key and prefix consist of only lowercase English letters.
1 <= val <= 1000
At most 50 calls will be made to insert and sum.
"""
# Approach1: Brute Force
class MapSum1(object):
    def __init__(self):
        self.map = {}

    def insert(self, key, val):
        self.map[key] = val

    def sum(self, prefix):
        return sum(val for key, val in self.map.items() if key.startswith(prefix))

# Approach2: Trie
class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.sum = 0

class MapSum2:
    def __init__(self):
        self.trieRoot = TrieNode()
        self.map = defaultdict(int)

    def insert(self, key, val):
        diff = val - self.map[key]
        curr = self.trieRoot
        for c in key:
            curr = curr.child[c]
            curr.sum += diff
        self.map[key] = val

    def sum(self, prefix):
        curr = self.trieRoot
        for c in prefix:
            if c not in curr.child:
                return 0
            curr = curr.child[c]
        return curr.sum
