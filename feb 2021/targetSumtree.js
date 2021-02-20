// Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

// A leaf is a node with no children.

var hasPathSum = function(root, targetSum, current = 0) {
    if (!root) return false;
    if ((targetSum - root.val) == 0 && !root.left && !root.right) return true;
    return hasPathSum(root.left, targetSum - root.val) || hasPathSum(root.right, targetSum - root.val);
};