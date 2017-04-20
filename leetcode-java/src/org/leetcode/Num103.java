package org.leetcode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

/**
 * Created by shuai on 2017/4/20.
 */

// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}


public class Num103 {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        Stack<TreeNode> s1 = new Stack<>();
        Stack<TreeNode> s2 = new Stack<>();
        s1.push(root);
        List<List<Integer>> ret = new ArrayList<>();
        if(root == null){
            return ret;
        }
        while (!s1.isEmpty() || !s2.isEmpty()){
            List<Integer> values = new ArrayList<>();
            if(!s1.isEmpty()){
                while(!s1.isEmpty()){
                    TreeNode node = s1.pop();
                    values.add(node.val);
                    if (node.left != null)
                        s2.push(node.left);
                    if (node.right != null)
                        s2.push(node.right);
                }
            }
            else {
                while(!s2.isEmpty()){
                    TreeNode node = s2.pop();
                    values.add(node.val);
                    if (node.right != null)
                        s1.push(node.right);
                    if (node.left != null)
                        s1.push(node.left);
                }
            }
            ret.add(values);
        }
        return ret;
    }

    public static void main(String[] args){
        TreeNode root = new TreeNode(3);
        TreeNode node1 = new TreeNode(9);
        TreeNode node2 = new TreeNode(20);
        TreeNode node3 = new TreeNode(15);
        TreeNode node4 = new TreeNode(7);
        root.left = node1;
        root.right = node2;
        node2.left = node3;
        node2.right = node4;
        Num103 sol = new Num103();
        System.out.println(sol.zigzagLevelOrder(root));
    }
}
