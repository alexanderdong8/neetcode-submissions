#include <sstream>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

class Trie {
public:
    unordered_map<string, Trie> children;
    bool isEnd = false;

    Trie() {}

    
};
class Solution {
public:
    vector<string> res;
    vector<string> arr = {"/"};
    
    vector<string> removeSubfolders(vector<string>& folder) {
        Trie root{};
        for (string path : folder) {
            Trie* curr = &root;
            stringstream ss(path);
            string part;
            while (getline(ss, part, '/')) {
                if (!part.empty()) {
                    if (curr->children.find(part) == curr->children.end())
                        curr->children[part] = Trie();
                    
                    curr = &curr->children[part];
                }
            }
            curr->isEnd = true;
        }
        dfs(root, "/");
        return res;
    }

    void dfs(const Trie& node, string path) {
        if (node.isEnd) {
            path.pop_back();
            res.push_back(path);
            return;
        }

        for (const auto& [key, value] : node.children) {
            dfs(value, path + key + '/');
        }

    }
        
        
};