class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []

        l = 0
        r = len(matrix[0])-1
        top = 0
        bottom = len(matrix)-1

        while l <=r and top <= bottom:
            
            # left to right
            for i in range(l,r+1):
                res.append(matrix[l][i])
            top+=1

            # top to bottom
            for i in range(top, bottom+1):
                res.append(matrix[i][r])
            r-=1

            if top > bottom or l > r :
                break

            # right to left
            for i in range(r, l-1, -1):
                res.append(matrix[bottom][i])
            bottom-=1

            #bottom to top
            for i in range(bottom, top-1, -1):
                res.append(matrix[i][l])
            l+=1

        return res
            
                

        

        