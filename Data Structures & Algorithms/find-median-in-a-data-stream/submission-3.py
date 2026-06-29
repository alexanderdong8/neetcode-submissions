class MedianFinder:

    def __init__(self):
        self.maxHeap = [] # left side
        self.minHeap = [] # right side
        self.median = 0

    def addNum(self, num: int) -> None:
        if num > self.median:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        while len(self.minHeap) - len(self.maxHeap) > 1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)

        while len(self.maxHeap) - len(self.minHeap) > 1:
            val = heapq.heappop(self.maxHeap) * -1
            heapq.heappush(self.minHeap, val)

        if len(self.maxHeap) == len(self.minHeap):
            self.median = (self.minHeap[0] + (self.maxHeap[0] * -1)) / 2
        else:
            self.median = self.minHeap[0] if len(self.minHeap) > len(self.maxHeap) else self.maxHeap[0] * -1

    def findMedian(self) -> float:
        return self.median
        
        