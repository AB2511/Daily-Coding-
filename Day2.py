class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l: int, r: int) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]  

        res = ""
        for i in range(len(s)):
            tmp1 = expand(i, i)
            tmp2 = expand(i, i+1)

            if len(tmp1) > len(res): res = tmp1
            if len(tmp2) > len(res): res = tmp2

        return res
