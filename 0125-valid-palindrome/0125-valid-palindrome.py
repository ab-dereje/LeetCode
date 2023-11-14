class Solution:
    def isPalindrome(self, s: str) -> bool:
        ab=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
        s=s.lower()
        d = []
        for i in s:
            if (i in ab):
                d.append(i)
            else:
                continue
        left_pointer, right_pointer = 0, len(d) - 1
        while left_pointer < right_pointer:
            if d[left_pointer] != d[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1

        return True