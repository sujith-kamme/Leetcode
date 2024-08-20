def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        https://leetcode.com/problems/maximum-depth-of-binary-tree/
        '''
        global max_depth
        max_depth = -1
        if root is None:
            return 0
        def depthTraversal(node, current_depth):
            global max_depth
            if node is None:
                return
            new_current_depth = 1+current_depth
            max_depth = max(max_depth, new_current_depth)
            if node.left == None and node.right == None:
                return
            depthTraversal(node.left, new_current_depth)
            depthTraversal(node.right, new_current_depth)
        

        depthTraversal(root, 0)
        return max_depth