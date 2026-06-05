class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adj = {c:[]for w in words for c in w}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            print(minLen)
            if len(w1) > len(w2) and w1[:minLen] == w2 [:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].append(w2[j])
                    break

        print(adj)

        visit = set() #along the path
        ans = set()
        res = []

        def dfs(c):
            if c in visit:
                return False
            if c in ans:
                return True

            visit.add(c)
            for nei in adj[c]:
                if not dfs(nei):
                    return False

            visit.remove(c)
            ans.add(c)
            res.append(c)
            return True

        for char in adj:
            if not dfs(char):
                return ""
        res.reverse()
        return "".join(res) 
        