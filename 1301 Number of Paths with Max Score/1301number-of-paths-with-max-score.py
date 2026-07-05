from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7
        dp = [[(-1, 0) for _ in range(n)] for _ in range(n)]
        dp[n - 1][n - 1] = (0, 1)

        def cell_val(ch: str) -> int:
            if ch == "E" or ch == "S":
                return 0
            return ord(ch) - ord("0")

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == "X" or (i == n - 1 and j == n - 1):
                    continue

                best = -1
                ways = 0

                for x, y in ((i + 1, j), (i, j + 1), (i + 1, j + 1)):
                    if x < n and y < n and dp[x][y][0] != -1:
                        score, cnt = dp[x][y]
                        if score > best:
                            best = score
                            ways = cnt
                        elif score == best:
                            ways = (ways + cnt) % MOD

                if best != -1:
                    dp[i][j] = (best + cell_val(board[i][j]), ways)

        return [0, 0] if dp[0][0][0] == -1 else [dp[0][0][0], dp[0][0][1] % MOD]