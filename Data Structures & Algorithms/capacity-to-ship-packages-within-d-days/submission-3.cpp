class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {
        int maxVal = 0;
        int total = 0;
        for (int x : weights) {
            maxVal = max(maxVal, x);
            total += x;
        }
        int left = maxVal, right = total;
        int res = right;
        while (left <= right) {
            int mid = (left + right) / 2;

            if (valid(weights, mid, days)) {
                res = min(res, mid);
                right = mid - 1;
            } else {
                left = mid + 1;
            }
            
        }

        return res;
    }

    bool valid(vector<int>& weights, int maxVal, int days) {
        int ships = 1;
        int currVal = maxVal;
        for (int x : weights) {
            if (currVal - x < 0) {
                ships++;
                currVal = maxVal;
            }

            currVal -= x;
        }
        cout << maxVal << "," << ships << "," << days << endl;
        return ships <= days;
    }
};