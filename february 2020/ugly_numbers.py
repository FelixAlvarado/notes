# Given four integers n, a, b, and c, return the nth ugly number.

# Ugly numbers are positive integers that are divisible by a, b, or c.

 

# Example 1:

# Input: n = 3, a = 2, b = 3, c = 5
# Output: 4
# Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
# Example 2:

# Input: n = 4, a = 2, b = 3, c = 4
# Output: 6
# Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.
# Example 3:

# Input: n = 5, a = 2, b = 11, c = 13
# Output: 10
# Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.
# Example 4:

# Input: n = 1000000000, a = 2, b = 217983653, c = 336916467
# Output: 1999999984

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
                # least common multiple
        def lcm(a, b):
            return a * b // math.gcd(a, b)
        nums = sorted([a, b, c])
        nums2 = [lcm(a, b), lcm(b, c), lcm(a, c)]
        nums3 = lcm(nums2[0], c)
        lo, hi = n, nums[-1] * n
        while lo < hi:
            mid = (lo + hi) // 2
            rank = (sum(mid // n for n in nums) -
                    sum(mid // n for n in nums2) + 
                    mid // nums3 )
            if rank < n:
                lo = mid + 1
            else:
                hi = mid
        return lo