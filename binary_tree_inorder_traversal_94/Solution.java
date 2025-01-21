package LeetCode.binary_tree_inorder_traversal_94;

import java.util.ArrayList;
import java.util.List;

class Solution {

    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> vaList = new ArrayList<>();
        
        if (root == null) return vaList;

        vaList.addAll(inorderTraversal(root.left));
    
        vaList.add(root.val);

        vaList.addAll(inorderTraversal(root.right));

        return vaList;
    }
}
    
