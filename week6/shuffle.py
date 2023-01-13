import random

def shuffle(values):
    
    # Loop over the range of indexes from 0 up to the length of the list:

    for i in range(len(values) -1):

        # Randomly pick an index to swap with:

        indexChange = random.randint(0, len(values) -1)

        # Swap the values between the two indexes:

        values[i], values[indexChange] = values[indexChange], values[i]

    return values #return values

my_list = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]#tests random numbers
my_list2= ["this", "is", "a", "random", "list"]#tests random strings
print(shuffle(my_list))
print(shuffle(my_list2))


#Time complexity is: 0(n) - The Time Complexity of a loop is considered as O(n) since the iterations of the function grow with the size of the list.