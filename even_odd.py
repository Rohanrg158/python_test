list1=[1, 2, 3, 4]
print("First list:", list1)
list2=[5, 6, 7, 8]
print("Second list:", list2)
even=[]
odd=[]
list3=list1+list2
print("Concatenated list:", list3)
for i in list3:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
sorted_list=even+odd
print("Sorted list:", sorted_list)