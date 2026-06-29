class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            print(columnNumber)
            num = columnNumber % 26
            # print((((num - 1) % 26)))
            res.append(chr((num) + ord('A')))
            columnNumber = columnNumber // 26
            

        res.reverse()
        return "".join(res)