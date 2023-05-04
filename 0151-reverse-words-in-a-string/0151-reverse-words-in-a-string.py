class Solution:
    def reverseWords(self, s: str) -> str:
        word=s.split()
        word.reverse()
        sen=" ".join(word)
        return sen