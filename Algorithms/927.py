"""
927. Three Equal Parts - Hard

You are given an array arr which consists of only zeros and ones, divide the array
into three non-empty parts such that all of these parts represent the same binary value.

If it is possible, return any [i, j] with i + 1 < j, such that:

arr[0], arr[1], ..., arr[i] is the first part,
arr[i + 1], arr[i + 2], ..., arr[j - 1] is the second part, and
arr[j], arr[j + 1], ..., arr[arr.length - 1] is the third part.
All three parts have equal binary values.
If it is not possible, return [-1, -1].

Note that the entire part is used when considering what binary value it represents.
For example, [1,1,0] represents 6 in decimal, not 3. Also, leading zeros are allowed,
so [0,1,1] and [1,1] represent the same value.



Example 1:
Input: arr = [1,0,1,0,1]
Output: [0,3]

Example 2:
Input: arr = [1,1,0,1,1]
Output: [-1,-1]

Example 3:
Input: arr = [1,1,0,0,1]
Output: [0,2]

Example 4:
Input: arr = [0,0,0,1,1,0,0,0,1,1,0,0,1,1]
     index = [3,4,8,9,12,13]
     N = 14


Constraints:
3 <= arr.length <= 3 * 104
arr[i] is 0 or 1

Algo:
In this problem we need to split number into three parts, such that number in
each part after removed all zeroes are equal.

Let us check all the places, where we have 1. Let us have M elements such that.
1. If M == 0, it means that we have all zeroes, so we can split in any way, let
   us split it [0, 2].
2. If M is not divisible by 3, we can return [-1, -1] immediately, because if we
   can have three equal parts, number of ones in these parts must be the same.
3. Let us find now 6 indexes: p1, p2, p3, p4, p5, p6, where p1 is index of first 1,
   p2 is index of last one in first part, p3 is index of fisrt one in second part,
   and so on. Then it is necessary that A[p1:p2+1] equal to A[p3:p4+1] equal to A[p5:p6+1].
   Note that is is not sufficient though, because we can add some zeroes in the ends.
   So, if this condition do not holds, we return [-1, -1].
4. Evaluate lengths of how many zeros we can add in the end: l1, l2, l3. For l3
   we do not have any choice: we need to take all there zeroes. For l1 and l2 we
   can put zeroes in the beginning of one number or to the end of the next, so the
   options we have are: [0, ..., l1] for the first, [0, ..., l2] for the second
   and [l3] for third. So, if l3 > l2 or l3 > l1, we can not make parts equal and
   we return [-1, -1].
5. In the end return [p2 + l3, p4 + l3 + 1], in this way in each part we have l3 zeroes in the end.


Complexity
Time complexity is O(n), space complexity is O(n) as well to keep array of indexes.
"""
def threeEqualParts(arr):
    N = len(arr)
    ones = [i for i in range(N) if arr[i] == 1]
    M = len(ones)

    if M == 0: return [0, 2]

    if M % 3 != 0: return [-1, -1]

    p1, p2 = ones[0], ones[M // 3 - 1]
    p3, p4 = ones[M // 3], ones[2 * M // 3 - 1]
    p5, p6 = ones[2 * M // 3], ones[-1]
    pt1, pt2, pt3 = arr[p1:p2 + 1], arr[p3:p4 + 1], arr[p5:p6 + 1]

    if pt1 != pt2 or pt2 != pt3: return [-1, -1]

    zeros1 = p3 - p2 - 1
    zeros2 = p5 - p4 - 1
    zeros3 = N - p6 - 1
    if zeros3 > zeros1 or zeros3 > zeros2: return [-1, -1]

    return [p2 + zeros3, p4 + zeros3 + 1]

print(threeEqualParts([0,0,0,1,1,0,0,0,1,1,0,0,1,1]))
