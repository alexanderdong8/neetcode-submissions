class Solution:
    def reverse(self, x: int) -> int:
        res = []
        negative = False
        if x < 0:
            x = abs(x)
            negative = True
        while x > 0:
            num = x % 10
            res.append(num)
            x = x // 10
        res2 = 0
        for x in res:
            res2 = (res2 * 10) + x

        if negative:
            res2 *= -1

        return res2 if (math.pow(2, 31) * -1) <= res2 <= (math.pow(2, 31)-1) else 0