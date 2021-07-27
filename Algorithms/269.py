"""
269. Alien Dictionary - Hard

There is a new alien language that uses the English alphabet. However, the order
among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where
the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically
increasing order by the new language's rules. If there is no solution, return "".
If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where
they differ, the letter in s comes before the letter in t in the alien language.
If the first min(s.length, t.length) letters are the same, then s is smaller if
and only if s.length < t.length.



Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:

Input: words = ["z","x"]
Output: "zx"

Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.
"""
class BFSSolution:
    def alienOrder(self, words: List[str]) -> str:
        # Step 0: create data structures + the in_degree of each unique letter to 0.
        adj_list = defaultdict(set)
        in_degree = Counter({c : 0 for word in words for c in word})

        # Step 1: We need to populate adj_list and in_degree.
        # For each pair of adjacent words...
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else: # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): return ""

        # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)

        # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(output) < len(in_degree):
            return ""
        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(output)
"""
Time complexity : O(C).

There were three parts to the algorithm; identifying all the relations, putting
them into an adjacency list, and then converting it into a valid alphabet ordering.

In the worst case, the first and second parts require checking every letter of every
word (if the difference between two words was always in the last letter). This is O(C).

For the third part, recall that a breadth-first search has a cost of O(V+E), where
V is the number of vertices and E is the number of edges. Our algorithm has the
same cost as BFS, as it too is visiting each edge and node once (a node is visited
once all of its edges are visited, unlike the traditional BFS where it is visited
once one edge is visited). Therefore, determining the cost of our algorithm requires
determining how many nodes and edges there are in the graph.

Nodes: We know that there is one vertex for each unique letter, i.e. O(U) vertices.

Edges: Each edge in the graph was generated from comparing two adjacent words in the
input list. There are N−1 pairs of adjacent words, and only one edge can be generated
from each pair.

Finally, we need to combine the two parts: O(C) for the first and second parts, and
O(U+min(U^2,N)) for the third part. Adding them together, we get O(C+U+min(U^2,N)).

In summary, C is the biggest of the three, and N and U are smaller, although we
don't know which is smaller out of those two.

So for starters, we know that the U bit is insignificant compared to the C. Therefore,
we can just remove it: O(C+U+min(U^2,N))→O(C+min(U^2,N))

Now, to simplify the rest, consider two cases:

- If U^2 is smaller than N, then U < N < C. This leaves us with O(C).

- If N is larger, then because N < C, we're still left with O(C).


So in all cases, we know a final time complexity of O(C).

Space complexity: O(1) or O(U+min(U^2,N))
"""
class DFSSolution:
    def alienOrder(self, words: List[str]) -> str:
        # Step 0: Put all unique letters into the adj list.
        reverse_adj_list = {c : [] for word in words for c in word}

        # Step 1: Find all edges and put them in reverse_adj_list.
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    reverse_adj_list[d].append(c)
                    break
            else: # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word):
                    return ""

        # Step 2: Depth-first search.
        seen = {} # False = grey, True = black.
        output = []
        def visit(node):  # Return True iff there are no cycles.
            if node in seen:
                return seen[node] # If this node was grey (False), a cycle was detected.
            seen[node] = False # Mark node as grey.
            for next_node in reverse_adj_list[node]:
                result = visit(next_node)
                if not result:
                    return False # Cycle was detected lower down.
            seen[node] = True # Mark node as black.
            output.append(node)
            return True

        if not all(visit(node) for node in reverse_adj_list):
            return ""

        return "".join(output)
