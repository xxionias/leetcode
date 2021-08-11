"""
415. Add Strings - Easy

Given two non-negative integers, num1 and num2 represented as string, return the
sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large
integers (such as BigInteger). You must also not convert the inputs to integers directly.



Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"


Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
"""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1, l2 = list(num1), list(num2)

        carry, res = 0, []
        while len(l1) > 0 or len(l2) > 0:
            n1 = ord(l1.pop()) - ord('0') if len(l1) > 0 else 0
            n2 = ord(l2.pop()) - ord('0') if len(l2) > 0 else 0

            s = n1 + n2 + carry
            res.append(s % 10)
            carry = s // 10

        if carry:
            res.append(carry)

        return ''.join([str(i) for i in res])[::-1]
