class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=''
        for i in digits:
            a=a+str(i)
        a=str(int(a)+1)
        return(list(a))


