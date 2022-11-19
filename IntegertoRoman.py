class Solution:
    def intToRoman(self, num: int) -> str:
        pair={1:'I',5:'V',10:'X',4:'IV',9:'IX',10:'X',50:'L',40:'XL',90:'XC',500:'D',100:'C',400:'CD',900:'CM',1000:'M',0:''}
        n=num
        roman = ''
        digit=10**(len(str(num))-1)
        temp = (int(num)//digit)
        while (digit>0) :
	        while temp>9:
		        temp%=10
	        if 5<=temp<9:
		        roman = roman + pair[(digit)*5]
		        temp=temp-5
	        if 1<=temp<=3:
		        roman = roman + pair[digit]*(temp)
	        else:
	    	    roman =roman + pair[temp*(digit)]
	        digit//=10
	        if digit==0:
		        break
	        temp = int(num)//digit
	        if digit!=1:
	    	    temp = temp%digit
	        else :
		        temp = n%10
        return(roman)
