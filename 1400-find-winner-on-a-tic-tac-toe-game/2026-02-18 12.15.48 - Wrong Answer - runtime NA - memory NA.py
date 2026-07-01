class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        t=sum(r[0] for r in moves)
        d=sum(r[1] for r in moves)
        if t>d:
            return "A"
        elif d>t:
            return "B"
        return "Draw"