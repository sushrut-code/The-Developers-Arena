#you basically select the minimum element in the inner loop and then swap it with the first element of the inner loop. Run this inner loop as many times as the length of the array in the outer loop.
# time complexity= O(n^2)


def selection_sort(arr):
    arr_length=len(arr)
    for i in range(arr_length):
        min_index=i
        for j in range(i+1,arr_length):
            if arr[j]<arr[min_index]:
                arr[j],arr[min_index]=arr[min_index],arr[j]
    return arr


user_list=[]
user_length=int(input("Enter the length of your list: "))
for i in range(user_length):
    a=int(input(f"enter the {i+1} element: "))
    user_list.append(a)
print(f"your sorted list using selection sort is {selection_sort(user_list)}")