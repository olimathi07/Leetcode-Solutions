class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words[0])
        r = []

        for top in words:
            for left in words:
                if top[0] != left[0]:
                    continue

                for right in words:
                    if top[-1] != right[0]:
                        continue

                    for bottom in words:
                        if bottom[0] != left[-1]:
                            continue
                        if bottom[-1] != right[-1]:
                            continue

                        r.append([top, left, right, bottom])

        return r