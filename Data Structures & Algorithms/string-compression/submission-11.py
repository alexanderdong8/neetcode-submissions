class Solution:
    def compress(self, chars: List[str]) -> int:
        res = []
        cur = ""
        count = 0
        for x in range(len(chars)):
            if count == 0:
                cur = chars[x]
                count += 1

            else:
                if cur != chars[x]:
                    res.append(cur)

                    if count != 1:
                        res.append(str(count))

                    cur = chars[x]
                    count = 1

                else:
                    count += 1
        print(res)
        res.append(cur)
        if count != 1:
            for char in str(count):
                res.append(char)

        print(res)
        for x in range(len(res)):
            chars[x] = res[x]
        return len(res)
