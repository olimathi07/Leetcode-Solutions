class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        return[key for key,v in c.most_common(k)]
      
                   
