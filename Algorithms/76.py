"""
76. Minimum Window Substring - Hard


Given two strings s and t of lengths m and n respectively, return the minimum window
substring of s such that every character in t (including duplicates) is included in
the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ds, dt = Counter(s), Counter(t)
        for k, v in dt.items():
            if k not in ds or ds[k] < v:
                return ""

        required = len(t)
        min_len = len(s)

        l, r, start = 0, 0, 0
        while r < len(s):
            if s[r] in dt:
                if dt[s[r]] > 0:
                    required -= 1
                dt[s[r]] -= 1

            while required == 0:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start = l

                if s[l] in dt:
                    if dt[s[l]] >= 0:
                        required += 1
                    dt[s[l]] += 1

                l += 1

            r += 1

        return s[start:start + min_len]

    
