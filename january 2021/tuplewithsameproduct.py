# Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

 

# Example 1:

# Input: nums = [2,3,4,6]
# Output: 8
# Explanation: There are 8 valid tuples:
# (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
# (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
# Example 2:

# Input: nums = [1,2,4,5,10]
# Output: 16
# Explanation: There are 16 valids tuples:
# (1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
# (2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
# (2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,4,5)
# (4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
# Example 3:

# Input: nums = [2,3,4,6,8,12]
# Output: 40
# Example 4:

# Input: nums = [2,3,5,7]
# Output: 0

# faster time and space solution

import math
from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_dict = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]
                if product in product_dict:
                    product_dict[product] += 1
                else:
                    product_dict[product] = 1

        return sum([4*v*(v-1) for v in product_dict.values() if v >= 2])


# my solution
import math
from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
#         make list of products of pairs in array
# only add to list if both numbers are unique
# only add to result if all numbers in both pairs are unique
# depending on number of pairs, use equation to determine how much to add to result
        products = defaultdict(list)
        result = 0

        for idx in range(0,len(nums)):
            for idx2 in range(0,idx):
                product = nums[idx] * nums[idx2]
                products[f"{product}"].append([nums[idx2],nums[idx]])

        for key in products.keys():
            if len(products[f"{key}"]) > 1:
                new_pairs = Solution.add_result(len(products[f"{key}"]))
                result += new_pairs

        return int(result * 8)
    
    

    def add_result(pairs):
        return math.factorial(pairs)/(math.factorial(2)*math.factorial(pairs - 2))