def intersection(nums1, nums2):
        intersection = []
        for i in nums1:
            for j in nums2:
                if i == j and i not in intersection:
                    intersection.append(i)
        return intersection
        