# Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

# Example 1:

# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
# Example 2:

# Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
# Example 3:

# Input: matrix = [[7,8],[1,2]]
# Output: [7]

#my solution
import numpy

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        max_column = []
        min_row = []
        
        for i,row in enumerate(matrix):
            min_row.append([min(row),row.index(min(row))])
            
            if i is 0:
                max_column = row
            else:
                count = 0
                while count < len(row):
                    max_column[count] = max(max_column[count],row[count])
                    count += 1
        
        result = []
        for num in min_row:
            if num[0] is max_column[num[1]]:
                result.append(num[0])
        
        return result

##faster solution

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        matrix_len = len(matrix)                       
		arr_len = len(matrix[0])                      
        lucky_N = []                                   
        for index in range(matrix_len):                #iterate through each list in matrix
            lucky = True                               #lucky for early break-out of-loop and to append to lucky_N
            min_number_at_list = min(matrix[index])    # get min # in current list
            for x in range(arr_len):                   # iterate through current list until min is reached
                if matrix[index][x] == min_number_at_list:  # enter when min is reached
                    for y in range(matrix_len):             # iterate though y-axis of matrix
                        if matrix[index][x] < matrix[y][x]  # if any number in y-axis > lucky number, break out of loop
                            lucky = False                   # no longer lucky **
                            break
                    if lucky: lucky_N.append(matrix[index][x])   # if number is lucky, append
                if not lucky: break # no longer lucky **, save computation (incase lucky number attempt is in middle of list)
        return lucky_N