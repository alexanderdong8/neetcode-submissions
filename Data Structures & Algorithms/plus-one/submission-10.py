class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = (digits[-1] + 1) // 10
        digits[-1] = (digits[-1]+1) % 10
        if not carry:
            return digits

        for x in range(len(digits)-2, -1, -1):
            if carry == 0:
                break
            print(x, digits, carry)
            newNum = (digits[x] + carry) % 10
            carry = (digits[x] + carry) // 10
            digits[x] = newNum
            

        print(digits)
        if carry >= 1:
            digits.insert(0, carry)

        return digits
        