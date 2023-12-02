class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        G = 0
        P = 0
        M = 0
        m_range = 0
        p_range = 0
        g_range = 0
        for i in range(len(garbage)):
            if "M" in garbage[i]:
                m_range =i
            if "P" in garbage[i]:
                p_range =i
            if "G" in garbage[i]:
                g_range =i
        for i in range(m_range+1):
            for j in range(len(garbage[i])):
                if ("M" == garbage[i][j]):
                    M += 1
                    print(M)
            if(i!=m_range):
                M += travel[i]

        for i in range(p_range+1):
            for j in range(len(garbage[i])):
                if ("P" == garbage[i][j]):
                    P += 1
            if(i!=p_range):
                P += travel[i]
        for i in range(g_range+1):
            for j in range(len(garbage[i])):
                if ("G" == garbage[i][j]):
                    G += 1
            if(i!=g_range):
                G += travel[i]
        ans=P+M+G

        return ans