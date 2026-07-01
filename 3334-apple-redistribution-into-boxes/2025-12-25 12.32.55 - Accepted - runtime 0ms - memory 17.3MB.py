class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        t=sum(apple)
        capacity.sort(reverse=True)
        b=0
        n=0
        for i in capacity:
            n+=i
            b+=1
            if n>=t:
              return b