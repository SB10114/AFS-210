# def search(arr, target): #time complexity is 0(n) this is a linear list
#     arr_size = len(arr)
#     for i in range(arr_size):
#         if target == arr[i]:
#             return True
#         elif arr[i] > target:
#             return False
#     return False

def binarySearch(arr, target):
    start = 0
    end = len(arr) -1
    
    while start <= end:
        midpoint = (start + end) // 2
        if arr[midpoint] == target:
            return True
        else:
            if target < arr[midpoint]:
                end = midpoint -1
            else:
                start = midpoint +1
    
        return False


my_list = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
my_list2 = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
my_list3 = ["Alpha", "Beta", "Delta","Epsilon", "Gamma", "Theta", "Zeta"]


print(binarySearch(my_list, 40))
print(binarySearch(my_list2, 22))
print(binarySearch(my_list3, 'Alpha'))