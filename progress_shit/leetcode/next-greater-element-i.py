class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        
        dic=defaultdict(lambda: -1)

        for i in range(len(nums2)):
            while stack and stack[-1]<nums2[i]:
                poped_elem=stack.pop()
                dic[poped_elem]=nums2[i]

            stack.append(nums2[i])
        
        return [dic[greater] for greater in nums1]

        




        