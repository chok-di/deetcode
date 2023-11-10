class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1,r1 = 0, len(nums1) - 1
        l2,r2 = 0, len(nums2) - 1
        temp1,temp2 = 0,0

        while l1 <= r1 and l2 <= r2:
            if l1 == r1:
                temp1 = nums1[l1]
            if l2 == r2:
                temp2 = nums2[l2]
            if nums1[l1] <= nums2[l2]:
                l1 += 1
            else:
                l2 += 1
            if nums1[r1] >= nums2[r2]:
                r1 -= 1
            else:
                r2 -= 1
        if l1 <= r1:
            return (nums1[(l1 + r1)//2] + nums1[(l1 + r1)//2 + (l1 + r1) % 2 ])/2
        if l2 <= r2:
            return (nums2[(l2 + r2)//2] + nums2[(l2 + r2)//2 + (l2 + r2) % 2 ])/2
        return (temp1 + temp2)/2
