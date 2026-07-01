class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap=[]
        for i in nums:
            heap.append(i)
        heapq.heapify(heap)
        s=[]
        while heap:
            s.append(heapq.heappop(heap))
        return s