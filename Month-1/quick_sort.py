#time complexity=O(nlogn)
# basically you select a pivot element
# and then you divide the aray on the basis of its smallerness or largerness with respect to pivot element.
# now repeat the above two process for the left pile as well as right pile of array.


def quick_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[-1]
        left_pile=[]
        right_pile=[]
        for item in arr[:-1]:
            if item<pivot:
                left_pile.append(item)
            else:
                right_pile.append(item)

        sorted_left=quick_sort(left_pile)
        sorted_right=quick_sort(right_pile)

        return sorted_left+[pivot]+sorted_right



user_list=[]
user_length=int(input("Enter the length of your list: "))
for i in range(user_length):
    a=int(input(f"enter the {i+1} element: "))
    user_list.append(a)
print(f"your sorted list using quick sort is {quick_sort(user_list)}")