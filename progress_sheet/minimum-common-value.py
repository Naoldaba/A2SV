class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i=j=0
        Min=float('inf')
        while i<len(nums1) and j<len(nums2):
            cur=nums1[i]==nums2[j]
            if cur and nums1[i]<Min:
                Min=nums1[i]
                break
            if nums1[i]<nums2[j]:
                i+=1
            elif nums2[j]<nums1[i]:
                j+=1
        return Min if Min!=float('inf') else -1
        