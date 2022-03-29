def sortarray(nums):
    def mergeSort(a, l, r):
        if l >= r:
            return

        def merge(a, l, m, r):
            sorted = [0] * (r - l + 1)
            k = 0
            i = l
            j = m + 1

            # verifica do inicio ate o fim
            while i <= m and j <= r:
                if a[i] < a[j]:
                    sorted[k] = a[i]
                    k += 1
                    i += 1
                else:
                    sorted[k] = a[j]
                    k += 1
                    j += 1

            # verifica do inicio ate o meio
            while i <= m:
                sorted[k] = a[i]
                k += 1
                i += 1
            
            # verifica do meio ate o ate o fim
            while j <= r:
                sorted[k] = a[j]
                k += 1
                j += 1

            a[l:l + len(sorted)] = sorted

        # meio
        m = (l + r) // 2
        # chama a funca para as duas metades
        mergeSort(a, l, m)
        mergeSort(a, m + 1, r)
        # combina as duas formas de maneira ordenada
        merge(a, l, m, r)

    mergeSort(nums, 0, len(nums) - 1)
    
    return nums

# listas
nums = [5,2,3,1]
# nums = [5,1,1,2,0,0]

print(sortarray(nums))
