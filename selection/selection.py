def selection(arr):
    for step in range(len(arr)):
        min_index = step

        for i in range(step + 1, len(arr)):
            if arr[i] < arr[min_index]:
                min_index = i
        arr[step], arr[min_index] = arr[min_index], arr[step]
