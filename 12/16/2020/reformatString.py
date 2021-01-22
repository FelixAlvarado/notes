# Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

# You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

# Return the reformatted string or return an empty string if it is impossible to reformat the string.

 

# Example 1:

# Input: s = "a0b1c2"
# Output: "0a1b2c"
# Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
# Example 2:

# Input: s = "leetcode"
# Output: ""
# Explanation: "leetcode" has only characters so we cannot separate them by digits.
# Example 3:

# Input: s = "1229857369"
# Output: ""
# Explanation: "1229857369" has only digits so we cannot separate them by characters.
# Example 4:

# Input: s = "covid2019"
# Output: "c2o0v1i9d"
# Example 5:

# Input: s = "ab123"
# Output: "1a2b3"

class Solution:
    def reformat(self, s: str) -> str:
        #seperate by type (int or letter)
        #check if length difference is less than 2
        #reformat
        numbers = []
        letters = []
        for symbol in s:
            if symbol.isdigit():
                # use isNAN in javascript
                numbers.append(symbol)
            else:
                letters.append(symbol)
        
        print('numbers',numbers)
        print('letters',letters)
        if abs(len(numbers) - len(letters)) >=2:
            return ""
        
        result = ''
        last = ''
        
        if(len(numbers) > len(letters)):
            result += numbers.pop(0)
            last = 'number'
        else:
            result += letters.pop(0)
            last = 'letter'
        
        while len(numbers) > 0 or len(letters) > 0:
            if(last == 'number'):
                result += letters.pop(0)
                last = 'letter'
            else: 
                result += numbers.pop(0)
                last = 'number'
        
        return result