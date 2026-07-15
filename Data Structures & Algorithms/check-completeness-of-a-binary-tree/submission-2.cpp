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
    bool isCompleteTree(TreeNode* root) {
        deque<TreeNode*> queue = {root};
        int level = 0;
        bool last = false;
        bool early = false;
        while (!queue.empty()) {
            cout << queue.size() << endl;
            int length = queue.size();
            if (length != pow(2, level)) {
                last = true;
            }

            for (int x = 0; x < length; x++) {
                TreeNode* node = queue.front();
                queue.pop_front();
                if (node->left) {
                    if (early)
                        return false;
                    if (last)
                        return false;
                    
                    queue.push_back(node->left);
                } else {
                    cout << node->val << endl;
                    early = true;
                }

                if (node->right) {
                    if (early)
                        return false;
                    if (last)
                        return false;
                    queue.push_back(node->right);
                } else {
                    cout << node->val << endl;
                    early = true;
                }
            }
            level += 1;
        }
        return true;
    }
};