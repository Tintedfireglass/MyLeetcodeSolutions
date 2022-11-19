class Solution {
    public boolean isPalindrome(int x) {
        boolean ret;
       if (x<0){
           ret = false;
           return(ret);}
        else {
            int ans=0;
            int ex = x;
             while(ex>0){
                int w = ex%10;
                 ex =ex/10;
                ans = 10*ans +w ;
             }
            if(ans==x){
                ret = true;
                return(ret);}
            else {
                ret = false;
                return(ret);
                }
            }            
        }
    }
