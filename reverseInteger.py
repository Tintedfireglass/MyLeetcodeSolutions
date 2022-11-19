class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            ns = str(x)
            nr=''
            for i in ns :
                nr = i+nr
            nr=int(nr)
        else:
            ns = str(-x)
            nr=''
            for i in ns :
                nr = i+nr
            nr=-int(nr)
        if nr>(2**31) or nr<(-(2**31)):
            return(0)
        else:
            return(nr)
