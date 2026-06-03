class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {}

        for src, p in prerequisites:
            if src not in hashmap:
                hashmap[src] = []
            hashmap[src].append(p)

        visit = set()

        for j in range(numCourses):
            if not self.dfs(j, visit, hashmap):
                return False
        return True

    def dfs(self, crs, visit, hashmap):
        if crs in visit:
            return False
        if crs not in hashmap or hashmap[crs] == []:
            return True
        visit.add(crs)
        for i in hashmap[crs]:
            if not self.dfs(i, visit, hashmap):
                return False
        visit.remove(crs)
        hashmap[crs] = []
        return True


    

        