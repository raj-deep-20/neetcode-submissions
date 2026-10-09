class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        chSet = set(s)

        for ch in chSet:
            cnt = l = 0
            for r in range(len(s)):
                if s[r] == ch:
                    cnt += 1
                while (r-l+1) - cnt > k:
                    if s[l] == ch:
                        cnt -= 1
                    l += 1
                res = max(res, r - l + 1)
        return res