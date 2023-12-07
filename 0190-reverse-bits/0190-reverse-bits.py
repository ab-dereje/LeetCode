class Solution:
    def reverseBits(self, n: int) -> int:
        binary_str = bin(n)[2:]
        
        binary_str = binary_str.zfill(32)
        reversed_binary_str = binary_str[::-1]
        reversed_integer = int(reversed_binary_str, 2)

        return reversed_integer