class Solution {
    public int romanToInt(String s) {
         int I = 1;
         int V = 5;
         int X = 10;
         int L = 50;
         int C = 100;
         int D = 500;
         int M = 1000;
        int num[]=new int[15];
        int ret = 0;
        for (int i = s.length()-1;i>=0;i--){
            char val = s.charAt(i);  
            if (val=='I')
                num[i]=1;
            else if (val=='V')
                num[i]=5;
            else if (val=='X')
                num[i]=10;
            else if (val=='L')
                num[i]=50;
            else if (val=='C')
                num[i]=100; 
            else if (val=='D')
                num[i]=500;
             else if (val=='M')
                num[i]=1000;
           }
        
        ret = ret+num[s.length()-1];
        
        for (int i = s.length()-2;i>=0;i--){
            if (num[i]<num[i+1])
                ret=ret-num[i];
            else ret = ret+num[i];
        }
        return(ret);
    }
}
