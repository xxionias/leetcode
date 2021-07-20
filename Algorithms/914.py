from collections import Counter
from functools import reduce
class Solution():
    def hasGroupSizeX(self, deck):
        def gcp(a, b):
            while b:
                a, b = b, a%b
            return a
        counts = Counter(deck).values()
        return reduce(gcp, deck) > 1
