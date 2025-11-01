def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_half=arr[:mid]
    right_half=arr[mid:]

    sorted_left=merge_sort(left_half)
    sorted_right=merge_sort(right_half)

    return merge(sorted_left,sorted_right)

def merge(left,right):
    result=[]
    i=j=0

    while i<len(left) and j <len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


















user_list=[]
user_length=int(input("Enter the length of your list: "))
for i in range(user_length):
    a=int(input(f"enter the {i+1} element: "))
    user_list.append(a)
print(f"your sorted list using merge sort is {merge_sort(user_list)}")