class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # data = nums1+nums2
        # data.sort()
        # if (len(nums1)+len(nums2)) % 2 == 1:
        #     return data[(len(nums1)+len(nums2))//2]
        # else:
        #     return (data[(len(nums1)+len(nums2))//2] +
        #             data[(len(nums1)+len(nums2))//2-1])/2
        data = []
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                data.append(nums1[i])
                i+=1
            else:
                data.append(nums2[j])
                j+=1
        data+=nums1[i:] +nums2[j:]
        if (len(nums1)+len(nums2)) % 2 == 1:
            return data[(len(nums1)+len(nums2))//2]
        else:
            return (data[(len(nums1)+len(nums2))//2] +
                    data[(len(nums1)+len(nums2))//2-1])/2 
