from typing import List


def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    for i in nums2:
        nums1.append(i)
    nums1.sort()
    t=len(nums1)    
    if(t%2==0):
        m=nums1[t//2-1]
        n=nums1[(t//2)]
        return float((m+n)/2)
    else:
        return float(nums1[((t+1)//2)-1])


print(findMedianSortedArrays(self=2,nums1=[1,2],nums2=[3]))