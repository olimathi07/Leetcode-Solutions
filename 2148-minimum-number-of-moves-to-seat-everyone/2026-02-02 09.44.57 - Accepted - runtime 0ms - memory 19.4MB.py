class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        c=0
        seats.sort()
        students.sort()
        for i in range(len(seats)):
           c+=abs(seats[i]-students[i])
        return c