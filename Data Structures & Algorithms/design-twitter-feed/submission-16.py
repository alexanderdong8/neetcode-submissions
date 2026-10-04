class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.connections = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        arr = []
        def dfs(userId):
            for (tweetId, time) in self.tweets[userId]:
                arr.append((tweetId, time))

            for newUser in self.connections[userId]:
                dfs(newUser)
        
        dfs(userId)
        arr.sort(key=lambda x: x[1])
        res = [tweetId for tweetId, time in arr]
        return res
        


    def follow(self, followerId: int, followeeId: int) -> None:
        self.connections[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.connections[followerId].remove(followeeId)
