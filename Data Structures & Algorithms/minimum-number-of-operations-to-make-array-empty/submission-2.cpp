class Solution {
public:
    int minOperations(vector<int>& nums) {
        unordered_map<int, int> nums_count;
        for (int &x : nums) {
            nums_count[x] += 1;
        }
        int res = 0;
        for (auto &[key, value] : nums_count) {
            if (value == 1)
                return -1;

            if (value % 3 == 0)
                res += value / 3;
            
            if (value % 3 == 1)
                res += (value / 3) - 1 + 2;
            
            if (value % 3 == 2)
                res += (value / 3) + 1;

        }

        return res;
    }
};