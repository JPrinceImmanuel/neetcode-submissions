class Solution:
    def isPalindrome(self, s: str) -> bool:

        rsc = ''.join(e for e in s if e.isalnum())
        rsc = rsc.lower()

        for i in range (len(rsc)//2):
            pointer_1 = i
            pointer_2 = len(rsc) -1 -i

            if rsc[pointer_1] != rsc[pointer_2]:
                return False
        return True 


        
            

        