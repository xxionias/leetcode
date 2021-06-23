"""
Finding the longest common subsequence between two strings is useful for
checking the difference between two files (diffing). Git needs to do this when
merging branches. It's also used in genetic analysis (combined with other
algorithms) as a measure of similarity between two genetic codes.
"""

"""
text1 = "gactagctaacg"
text2 = "tagctagcgcaa"
"""

"""
Approach 1: Memoization
The first string has M suffixes, the second string has N suffixes.

define function LCS(text1, text2):
    # If either string is empty there, can be no common subsequence.
    if length of text1 or text2 is 0:
        return 0

    # The case when the letter1 *is not* part of the optimal solution
    case1 = LCS(text1.substring(1), text2)

    # The case when the letter1 *is* part of the optimal solution
    letter1 = the first letter in text1
    if letter1 is in tex2:
        firstOccurrence = first position of letter1 in text2
        case2 = 1 + LCS(tex1.substring(1), text2.substring(firstOccurrence + 1))

    return maximum of case1 or case2

Time complexity:
Space complexity:
"""
from functools import lru_cache
class Solution1:
    def LCS(self, text1, text2):
        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0

            case1 = memo_solve(p1 + 1, p2)

            first_occurrence = text2.find(text1[p1], p2)
            case2 = 0
            if first_occurrence != -1:
                case2 = 1 + memo_solve(p1 + 1, first_occurrence + 1)

            return max(case1, case2)
        return memo_solve(0, 0)

text1 = "gactagcaacg"
text2 = "tagcagcgcaa"
sol = Solution1()
print(sol.LCS(text1, text2))
print(LCS.cache_info())
