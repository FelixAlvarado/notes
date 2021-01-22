# Given a binary tree, write a function to get the maximum width of the given tree. The maximum width of a tree is the maximum width among all levels.

# The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

# It is guaranteed that the answer will in the range of 32-bit signed integer.

# Example 1:

# Input: 

#            1
#          /   \
#         3     2
#        / \     \  
#       5   3     9 

# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
# Example 2:

# Input: 

#           1
#          /  
#         3    
#        / \       
#       5   3     

# Output: 2
# Explanation: The maximum width existing in the third level with the length 2 (5,3).
# Example 3:

# Input: 

#           1
#          / \
#         3   2 
#        /        
#       5      

# Output: 2
# Explanation: The maximum width existing in the second level with the length 2 (3,2).
# Example 4:

# Input: 

#           1
#          / \
#         3   2
#        /     \  
#       5       9 
#      /         \
#     6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        #use pre order traversal to iterate through tree
        #make queue of nodes, keeping track of their level and position
        #at the end of each level, subtract lowest position from highest position to get width  
        print(root)
        if root.left == None and root.right == None:
            return 1
        
        currentLevel = 2
        lowest = 0
        highest = 0
        maxWidth = 0
        queue = []
        if root.left is not None:
            queue.append([2,1,root.left])
        
        if root.right is not None:
            queue.append([2,2,root.right])
            
                
        while len(queue) > 0:
            newNode = queue.pop(0)
            if newNode[0] != currentLevel:
                maxWidth = max(highest - lowest + 1, maxWidth)
                currentLevel += 1
                lowest = 0
                highest = 0
            
            if newNode[1] < lowest or lowest == 0:
                lowest = newNode[1]
            
            if newNode[1] > highest or highest == 0:
                highest = newNode[1]
                
            newLevel = currentLevel + 1
            
            if newNode[2].left != None:
                queue.append([newLevel,newNode[1]*2 - 1 , newNode[2].left])
            
            if newNode[2].right != None:
                queue.append([newLevel,newNode[1]*2 , newNode[2].right])
                    
        maxWidth = max(highest - lowest + 1, maxWidth)
        
        return maxWidth