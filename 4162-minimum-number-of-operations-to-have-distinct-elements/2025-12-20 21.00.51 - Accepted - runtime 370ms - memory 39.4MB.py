from collections import Counter

class Solution:
    def minOperations(self, nums):
        freq = Counter(nums)
        duplicates = sum(1 for v in freq.values() if v > 1)

        ops = 0
        i = 0

        while duplicates > 0:
            
            for _ in range(3):
                if i >= len(nums):
                    break

                val = nums[i]
                if freq[val] == 2:
                    duplicates -= 1
                freq[val] -= 1
                i += 1

            ops += 1

        return ops
