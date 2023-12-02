from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(index, path):
            if index == len(digits):
                result.append(''.join(path))
                return

            letters = digit_mapping[digits[index]]

            for letter in letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        result = []
        backtrack(0, [])
        return result