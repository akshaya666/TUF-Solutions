class Solution:
    def intersectionArray(self, nums1, nums2):

        n = min(len(nums1),len(nums2))

        i,j = 0,0

        inter = []

        idx = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                inter.append(nums1[i])
                i+=1
                j+=1
            
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1
        
        return inter
        