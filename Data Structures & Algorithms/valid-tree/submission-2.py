class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()

        return self.dfs(0, -1, adj, visit) and len(visit) == n

    def dfs(self, node, parent, adj, visit):
        if node in visit:
            return False

        visit.add(node)


        for nei in adj[node]:
            if nei == parent:
                continue

            if not self.dfs(nei, node, adj, visit):
                return False

        return True


        