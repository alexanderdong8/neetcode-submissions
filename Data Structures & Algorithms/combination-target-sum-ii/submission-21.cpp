class Solution {
public:
    vector<vector<int>> res;
    vector<int> arr;

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        unordered_map<int, int> canMap;
        for (int& x : candidates) {
            canMap[x] = (canMap.contains(x) ? canMap.at(x) : 0) + 1;
        }
        vector<vector<int>> val_freq;
        for (const auto& [val, freq] : canMap) {
            val_freq.push_back(vector<int>{val, freq});
        }

        dfs(val_freq, 0, 0, target);
        return res;

    }

    void dfs(vector<vector<int>>& val_freq, int total, int index, int target) {
        if (total > target || index >= val_freq.size()) 
            return;

        if (total == target) {
            auto copy = arr;
            res.push_back(copy);
            return;
        }

        dfs(val_freq, total, index+1, target);

        if (val_freq[index][1] > 0) {
            arr.push_back(val_freq[index][0]);
            val_freq[index][1]--;
            dfs(val_freq, total + val_freq[index][0], index, target);
            arr.pop_back();
            val_freq[index][1]++;
        }
    }
};
