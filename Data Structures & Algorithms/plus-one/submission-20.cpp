class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carry = (digits[digits.size() - 1] + 1) / 10;
        digits[digits.size() - 1] = (digits[digits.size() - 1] + 1) % 10;

        if (carry == 0)
            return digits;

        for (int x=digits.size()-2; x >= 0; x--) {
            if (carry == 0)
                return digits;
            int newNum = (digits[x] + carry) % 10;
            carry = (digits[x] + carry) / 10;
            digits[x] = newNum;
        }

        if (carry >= 1)
            digits.insert(digits.begin(), carry);
        return digits;
    }
};
