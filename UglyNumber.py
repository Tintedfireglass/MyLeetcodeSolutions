class Solution:
    def isUgly(self, n: int) -> bool:
        ct=0
        if n<=0:
            return(False)
        while n>1:
            if n%2==0:
                n/=2
            elif n%3==0:
                n/=3
            elif n%5==0:
                n/=5
            else:
                ct=1
                break
        if ct==1:
            return(False)
        else:
            return(True)
