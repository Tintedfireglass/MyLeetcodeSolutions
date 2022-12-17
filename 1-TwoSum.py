class Solution(object):
    def twoSum(self, nums, target):
        l=[]
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if i!=j and nums[i]+nums[j]==target:
                    l.append(i)
                    l.append(j)
                    continue

                         
        return(set(l))
                    
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
