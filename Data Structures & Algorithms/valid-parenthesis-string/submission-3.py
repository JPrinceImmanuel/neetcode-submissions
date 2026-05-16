class Solution:
    def checkValidString(self, s: str) -> bool:

        open_p = "("
        close_p = ")"
        star = "*"

        # if s[0] == close_p or s[len(s)-1] == open_p:
        #     return False
        # if s == "()":
        #     return True

        open_p_res = []
        star_res = []
        for i in range(len(s)):
            if s[i] == open_p:
                open_p_res.append(i)
            if s[i] == star:
                star_res.append(i)
            if s[i] == close_p:
                if len(open_p_res) != 0:
                    open_p_res.pop()
                elif len(star_res) !=0:
                    star_res.pop()
                else:
                    return False

        print(open_p_res)
        print(star_res) 

       
        while len(star_res) != 0 and len(open_p_res) !=0:

            if open_p_res[-1] > star_res[-1]:
                return False
            
            open_p_res.pop()
            star_res.pop()

        return len(open_p_res) == 0
                

        