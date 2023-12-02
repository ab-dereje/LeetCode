class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)
        if index != -1:
            reversed_segment = word[:index + 1][::-1] + word[index + 1:]
            return reversed_segment
        else:
            return word