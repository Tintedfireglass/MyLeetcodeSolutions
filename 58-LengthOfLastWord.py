import re
import sys
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x=re.split(" ",s)  
        for i in x[::-1]:
            if i!="":
                return(len(i))
                sys.exit()
            else:
                continue
