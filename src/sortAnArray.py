def sortarray(nums):
    def mergeSort(a, l, r):
        if l >= r:
            return

        def merge(a, l, m, r):
            sorted = [0] * (r - l + 1)
            k = 0
            i = l
            j = m + 1

            while i <= m and j <= r:
                if a[i] < a[j]:
                    sorted[k] = a[i]
                    k += 1
                    i += 1
                else:
                    sorted[k] = a[j]
                    k += 1
                    j += 1

            while i <= m:
                sorted[k] = a[i]
                k += 1
                i += 1

            while j <= r:
                sorted[k] = a[j]
                k += 1
                j += 1

            a[l:l + len(sorted)] = sorted

        m = (l + r) // 2
        mergeSort(a, l, m)
        mergeSort(a, m + 1, r)
        merge(a, l, m, r)

    mergeSort(nums, 0, len(nums) - 1)
    
    return nums

# nums = [5,2,3,1]

nums = [5,1,1,2,0,0]

print(sortarray(nums))
