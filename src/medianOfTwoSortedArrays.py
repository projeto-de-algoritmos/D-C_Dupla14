def medianSortedArrays(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    if n1 > n2:
        return medianSortedArrays(nums2, nums1)

    l = 0
    r = n1

    while l <= r:
        particao1 = l + (r - l) // 2
        particao2 = (n1 + n2 + 1) // 2 - particao1
        maxLeft1 = -2**31 if particao1 == 0 else nums1[particao1 - 1]
        maxLeft2 = -2**31 if particao2 == 0 else nums2[particao2 - 1]
        minRight1 = 2**31 - 1 if particao1 == n1 else nums1[particao1]
        minRight2 = 2**31 - 1 if particao2 == n2 else nums2[particao2]
        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) * 0.5 if (n1 + n2) % 2 == 0 else max(maxLeft1, maxLeft2)
        elif maxLeft1 > minRight2:
            r = particao1 - 1
        else:
            l = particao1 + 1


#nums1 = [1,3]
#nums2 = [2]
nums1 = [1,2]
nums2 = [3,4]
# nums1 = [1,2,3]
# nums2 = [4,5,6]
 
print(medianSortedArrays(nums1, nums2))
