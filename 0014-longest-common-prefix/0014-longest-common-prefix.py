class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short = min(strs, key=len)
        for x in strs:
            while (len(short)>0):
                if x.startswith(short):
                    break
                else:
                    short=short[:-1]
        return short