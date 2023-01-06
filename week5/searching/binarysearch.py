def search(arr, target):
    arr_size = len(arr)
    for i in range(arr_size):
        if target == arr[i]:
            return True
        elif arr[i] > target:
            return False
    return False


my_list = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]

print(search(my_list, 40))