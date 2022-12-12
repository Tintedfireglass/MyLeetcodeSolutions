class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[]
        m=[1]
        f=[[1]]
        for i in range(1,numRows):
            l.append(1)
            for j in range(0,len(m)):
        
               if j!=len(m)-1:
                    l.append(m[j]+m[j+1])
            l.append(1)
            f.append(l)
            m=l
            l=[]
        return(f)
