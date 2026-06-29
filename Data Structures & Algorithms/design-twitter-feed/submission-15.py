class Twitter:

    def __init__(self):
        self.time = 0
        self.users = {}


    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = (self.time, tweetId)
        if userId not in self.users:
            self.users[userId] = [[], {userId}]
        self.users[userId][0].append(tweet)
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        
        tweets = []
        for user in self.users[userId][1]:
            tweets.extend(self.users[user][0])

        heapq.heapify(tweets)
        print(tweets)
        res = []

        count = 0
        while tweets and count < 10:
            res.append(heapq.heappop(tweets)[1])
            count += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = [[], {followerId}]
        self.users[followerId][1].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        # print(self.users[followerId][1])
        if followeeId in self.users[followerId][1]:
            self.users[followerId][1].remove(followeeId)
