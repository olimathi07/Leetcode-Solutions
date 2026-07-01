class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        r = []

        for top in words:
            for left in words:
                if left == top:
                    continue
                if top[0] != left[0]:
                    continue

                for right in words:
                    if right in (top, left):
                        continue
                    if top[-1] != right[0]:
                        continue

                    for bottom in words:
                        if bottom in (top, left, right):
                            continue
                        if bottom[0] != left[-1]:
                            continue
                        if bottom[-1] != right[-1]:
                            continue

                        r.append([top, left, right, bottom])

        return r