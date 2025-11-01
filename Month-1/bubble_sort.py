# we need to run two loops. outer loop defined for how many numbers we will run the inner loop and the inner loop defines the swapping of the values incase the first value is greater than the next value.
#time complexity=O(n^2)


def bubble_sort(arr):
    arr_length=len(arr)
    for i in range(arr_length-1):
        swapped=False
        for j in range(arr_length-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    return arr



user_list=[]
user_length=int(input("Enter the length of your list: "))
for i in range(user_length):
    a=int(input(f"enter the {i+1} element: "))
    user_list.append(a)
print(f"your sorted list using bubble sort is {bubble_sort(user_list)}")
