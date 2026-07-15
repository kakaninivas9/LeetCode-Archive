from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    bit = 1 << (ord(board[r][c]) - ord("1"))
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[(r // 3) * 3 + c // 3] |= bit

        def dfs():
            if not empty:
                return True

            best = -1
            best_mask = 0
            best_cnt = 10

            for i, (r, c) in enumerate(empty):
                mask = ~(rows[r] | cols[c] | boxes[(r // 3) * 3 + c // 3]) & 0x1FF
                cnt = mask.bit_count()
                if cnt < best_cnt:
                    best_cnt = cnt
                    best = i
                    best_mask = mask
                    if cnt == 1:
                        break

            r, c = empty.pop(best)
            box = (r // 3) * 3 + c // 3
            mask = best_mask

            while mask:
                bit = mask & -mask
                digit = bit.bit_length()
                board[r][c] = str(digit)

                rows[r] |= bit
                cols[c] |= bit
                boxes[box] |= bit

                if dfs():
                    return True

                rows[r] ^= bit
                cols[c] ^= bit
                boxes[box] ^= bit
                board[r][c] = "."

                mask ^= bit

            empty.insert(best, (r, c))
            return False

        dfs()