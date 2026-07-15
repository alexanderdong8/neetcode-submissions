/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
vector<TreeNode*> tree_arr; // what happesn when i change between treenode* and treenode

    void recoverTree(TreeNode* root) {
        dfs(root);
        vector<pair<TreeNode*, TreeNode*>> nodes;

        for (int x = 0; x < tree_arr.size()-1; x++) {
            if (tree_arr[x]->val > tree_arr[x+1]->val) {
                nodes.emplace_back(tree_arr[x], tree_arr[x+1]);
            }
        }

        if (nodes.size() == 1) {
            int temp = nodes[0].first->val;
            //TreeNode* temp = nodes[0].first; what would this do, wuld it create a copy?
            nodes[0].first->val = nodes[0].second->val;
            nodes[0].second->val = temp;
        }
        else if (nodes.size() == 2) {
            int temp = nodes[0].first->val;
            nodes[0].first->val = nodes[1].second->val;
            nodes[1].second->val = temp;
        }
    }
    void dfs(TreeNode* node) {
        if (!node)
            return;

        dfs(node->left);
        tree_arr.push_back(node); // whats happens if i just push in a pointer, does it make a copy or what happens
        dfs(node->right);
        return;
    }
};