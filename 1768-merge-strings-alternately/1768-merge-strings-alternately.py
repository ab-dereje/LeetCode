class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x=[]
        i=0
        j=0
        while len(word1)>i and len(word2)>j:
            x.append(word1[i])
            x.append(word2[j])
            i=i+1
            j=j+1
        x.extend(word1[i:])
        x.extend(word2[j:])
        
        return ''.join(x)