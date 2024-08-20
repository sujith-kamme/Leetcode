def sumNumbers(self, root: Optional[TreeNode]) -> int:
        root_to_leaf_paths = []
    
        def pathTraversal(node, paths, running_value):
            if node is None:
                return
            
            new_running_value = running_value + str(node.val)
            if node.left == None and node.right == None:
                paths.append(int(new_running_value))
            
            pathTraversal(node.left, paths, new_running_value)
            pathTraversal(node.right, paths, new_running_value)
        
        pathTraversal(root, root_to_leaf_paths, '')
        return sum(root_to_leaf_paths)