# in insertion sort,we divide the array into two parts.One part is sorted values and other part is unsorted values. we divide this based on the the current index which loops through the entire array.
#the left side of the current index is sorted values adn the right side is unsorted values.
#the inner loop works through the sorted values to find the right place for the the current index value and the outer loop works to move the current value from index1 to last.

#time complexity is O(n^2).


def insertion_sort(arr):
    arr_length=len(arr)
    for i in range(1,arr_length):
        insert_index=i
        current_value=arr[i]
        for j in range(i-1,-1,-1):
            if arr[j]>current_value:
                arr[j+1]=arr[j]
                insert_index=j
            else:
                break
        arr[insert_index]=current_value
    return arr













user_list=[]
user_length=int(input("Enter the length of your list: "))
for i in range(user_length):
    a=int(input(f"enter the {i+1} element: "))
    user_list.append(a)
print(f"your sorted list using insertion sort is {insertion_sort(user_list)}")