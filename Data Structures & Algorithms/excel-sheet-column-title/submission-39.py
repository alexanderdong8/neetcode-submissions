class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            print(columnNumber)
            num = columnNumber % 26
            # print((((num - 1) % 26)))
            res.append(chr(((num - 1) % 26) + ord('A')))
            columnNumber = (columnNumber-1) // 26
            

        res.reverse()
        return "".join(res)