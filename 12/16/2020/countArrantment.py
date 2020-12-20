

# Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

# The number at the ith position is divisible by i.
# i is divisible by the number at the ith position.
 

# Now given N, how many beautiful arrangements can you construct?

#sentially makes an array of false booleans and tests posibilities for each array using number and index. numbers are only added for arrays that are filled up with all trues

class Solution:
    def countArrangement(self, n):
        vis = [False] * n
        curr_ind = 1
        self.ans = 0
        self.count(vis, curr_ind)
        return self.ans

    def count(self, vis, curr_ind):
        if curr_ind > len(vis):
            self.ans += 1
            return
        for i in range(len(vis)):
            if not vis[i] and (not (i + 1) % curr_ind or not curr_ind % (i + 1)):
                vis[i] = True
                self.count(vis, curr_ind + 1)
                vis[i] = False