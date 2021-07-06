from typing import List
def twoSum(self, nums: List[int], target: int) -> List[int]:
        o=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    o.append(i)
                    o.append(j)
        
        return o
list= [7,1,2,15]
target=9 
print(twoSum(self=2,nums=list,target=target))

