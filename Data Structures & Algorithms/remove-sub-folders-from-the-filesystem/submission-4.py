class Trie:
    def __init__(self):
        self.children = {}
        self.end = False
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        root = Trie()
        res = []
        seen = set()
        for path in folder:
            pathArr = path.split("/") # remember if it has it in the beginning it will return nothing
            pathArr = pathArr[1:]
            curr = root
            newPath = True
            for subPath in pathArr:
                print(subPath)
                if subPath not in curr.children:
                    curr.children[subPath] = Trie()
                else:
                    if curr.children[subPath].end:
                        print(subPath, curr.children[subPath].end)
                        newPath = False
                curr = curr.children[subPath]

            curr.end = True
                
            if newPath:
                res.append(path)

        return res