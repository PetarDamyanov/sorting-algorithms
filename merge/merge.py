def merge(arr):
    if len(arr) > 1:

        R, L = arr[len(arr) // 2:], arr[:len(arr) // 2]

        merge(R)
        merge(L)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k][0], L[i][0] = L[i][0], arr[k][0]
                # arr[k], L[i] = L[i], arr[k]
                i += 1
            else:
                arr[k][0], R[j][0] = R[j][0], arr[k][0]
                # arr[k], R[j] = R[j], arr[k]
                j += 1
            k += 1
        while i < len(L):
            arr[k][0], L[i][0] = L[i][0], arr[k][0]
            # arr[k], L[i] = L[i], arr[k]
            i, k = i + 1, k + 1
        while j < len(R):
            arr[k][0], R[j][0] = R[j][0], arr[k][0]
            # arr[k], R[j] = R[j], arr[k]
            j, k = j + 1, k + 1
