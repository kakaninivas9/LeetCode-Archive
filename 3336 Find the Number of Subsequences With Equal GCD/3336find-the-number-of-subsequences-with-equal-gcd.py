import math
from typing import List

MOD = 1_000_000_007
MAX_VAL = 200
mu = [0] * (MAX_VAL + 1)
mu[1] = 1
for i in range(2, MAX_VAL + 1):
    n = i
    d = 2
    primes_cnt = 0
    square_free = True
    while d * d <= n:
        if n % d == 0:
            exp = 0
            while n % d == 0:
                n //= d
                exp += 1
            if exp >= 2:
                square_free = False
                break
            primes_cnt += 1
        d += 1
    if square_free and n > 1:
        primes_cnt += 1
    mu[i] = 0 if not square_free else (-1)**primes_cnt

pow2 = [pow(2, i, MOD) for i in range(MAX_VAL * 2 + 1)]
pow3 = [pow(3, i, MOD) for i in range(MAX_VAL + 1)]

lcm_table = [[0] * (MAX_VAL + 1) for _ in range(MAX_VAL + 1)]
for i in range(1, MAX_VAL + 1):
    for j in range(1, MAX_VAL + 1):
        lcm_table[i][j] = i * j // math.gcd(i, j)


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        maxV = max(nums)
        freq_all = [0] * (maxV + 1)
        for x in nums:
            freq_all[x] += 1

        ans = 0
        for g in range(1, maxV + 1):
            M = maxV // g
            if M == 0:
                continue

            freq = [0] * (M + 1)
            total = 0
            for k in range(1, M + 1):
                c = freq_all[k * g]
                if c:
                    freq[k] = c
                    total += c
            if total < 2:
                continue

            cnt = [0] * (M + 1)
            for d in range(1, M + 1):
                s = 0
                for k in range(d, M + 1, d):
                    s += freq[k]
                cnt[d] = s

            valid_d = []
            for d in range(1, M + 1):
                if mu[d] != 0 and cnt[d] != 0:
                    valid_d.append((d, mu[d], cnt[d]))

            g_ans = 0
            num_valid = len(valid_d)
            for i in range(num_valid):
                d1, m1, c1 = valid_d[i]
                for j in range(i, num_valid):
                    d2, m2, c2 = valid_d[j]

                    l = lcm_table[d1][d2]
                    c_both = cnt[l] if l <= M else 0

                    T = pow3[c_both] * pow2[c1 + c2 - (c_both << 1)]
                    N = (T - pow2[c2] - pow2[c1] + 1) % MOD

                    term = m1 * m2 * N

                    if i != j:
                        term *= 2

                    g_ans = (g_ans + term) % MOD
            ans = (ans + g_ans) % MOD
        return ans
