class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q = []
        hashset = set(["+", "*", "-", "/"])
        result = 0
        for x in tokens:
            print(x)
            if x not in hashset:
                q.append(int(x))
            else:
                if x == "+":
                    first = q.pop()
                    second = q.pop()
                    result = second + first
                    q.append(result)

                if x == "*":
                    first = q.pop()
                    second = q.pop()
                    result = second * first
                    q.append(result)

                if x == "/":
                    first = q.pop()
                    second = q.pop()
                    print(first, second)
                    result = int(second / first)
                    print(result)
                    q.append(result)
                if x == "-":
                    first = q.pop()
                    second = q.pop()
                    result = second - first
                    q.append(result)
                
        return q.pop()