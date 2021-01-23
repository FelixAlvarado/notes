# Given a string s of '(' , ')' and lowercase English characters. 

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
 

# Example 1:

# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:

# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:

# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
# Example 4:

# Input: s = "(a(b(c)d)"
# Output: "a(b(c)d)"
 

# Constraints:

# 1 <= s.length <= 10^5
# s[i] is one of  '(' , ')' and lowercase English letters.

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left = 0
        right = 0
        proper_right = 0
        
        for c in s:
            if c is '(': left += 1
            if c is ')': right += 1
            if c is ')' and proper_right < left: proper_right += 1
                
        
        if proper_right is right and left is right: return s
        
        left = 0
        right = 0
        
        result = ''
        
        for c in s:
            if c is '(' and left < proper_right: 
                result += c
                left += 1
            if c is ')' and right < left and right < proper_right: 
                result += c
                right += 1
            
            if c is not '(' and c is not ')':
                result += c
        
        return result