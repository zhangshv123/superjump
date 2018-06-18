#!/usr/bin/python
public class topdown {
    //DFS TOPDOWN(preorder)
    public TypeR func(T_1 t_1, T_p t_p) {
        checkRootExists();

        TreeNode[] array = new TreeNode[TREE_HEIGHT];

        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);

        while (!stack.empty()) {
            TreeNode node = stack.pop();

            //1.operation at node;

            //2.push children to stack
            stack.push(childLast); //最后一个孩子
            ........
            stack.push(childFirst);
        }
        return result;
    }

    private class TreeNode {
        T_v_1 field;
        int height;
    }
}
	