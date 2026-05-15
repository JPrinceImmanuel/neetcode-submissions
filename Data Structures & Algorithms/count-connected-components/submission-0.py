class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)


        visit = set()

        res = 0

        for i in range(n):
            if i not in visit:
                visit.add(i)
                self.dfs(i, visit, adj)
                res+=1

        return res


    def dfs(self, node, visit, adj):
        for nei in adj[node]:
            if nei not in visit:
                visit.add(nei)
                self.dfs(nei, visit, adj)


        