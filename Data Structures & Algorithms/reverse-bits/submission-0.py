class Solution:

    def reverseBits(self, n: int) -> int:

        a = bin(n)[2:]       # 21 -> "10101"
        a = a.zfill(32)      # 32 bits

        d = []

        for i in a:
            d.append(int(i))

        d.reverse()          # bits reverse

        ans = 0

        for i in range(32):
            ans += d[i] * (2 ** (31 - i))

        return ans