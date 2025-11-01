def binary_search(nums,n):
    left=0
    right=len(nums)   #excluding the right boundary
    while right>left:
        middle=(left+right)//2
        if nums[middle]>n:
            right=middle
        elif nums[middle]<n:
            left=middle+1
        else:
            return middle
    return None
user_list=[]
user_length=int(input("Enter the length of your list: "))
for i in range(user_length):
    a=int(input(f"enter the {i+1} element: "))
    user_list.append(a)
user_list.sort()
user_item=int(input("Enter what item you want to search for: "))
print(f"the index of your item is {binary_search(user_list,user_item)}")


