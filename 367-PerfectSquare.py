class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sq=sqrt(num)
        if sq%1==0.0:
            return(True)
        else:
            return(False)
