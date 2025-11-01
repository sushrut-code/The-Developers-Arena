#only works in non-negative values
#time complexity depends on range of possible values k and number of values n
#time complexity is O(n+k)


def counting_sort(arr):
    max_value=max(arr)
    count=[0]*(max_value+1)
    while len(arr)>0:
        num=arr.pop(0)
        count[num]+=1
    for i in range(len(count)):
        while count[i]>0:
            arr.append(i)
            count[i]-=1
    return arr

















user_list=[]
user_length=int(input("Enter the length of your list: "))
for i in range(user_length):
    a=int(input(f"enter the {i+1} element: "))
    user_list.append(a)
print(f"your sorted list using counting sort is {counting_sort(user_list)}")
