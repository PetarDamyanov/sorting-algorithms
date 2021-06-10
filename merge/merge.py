def merge(arr):
    if len(arr) > 1:

        R, L = arr[len(arr) // 2:], arr[:len(arr) // 2]

        merge(R)
        merge(L)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i, k = i + 1, k + 1
        while j < len(R):
            arr[k] = R[j]
            j, k = j + 1, k + 1
