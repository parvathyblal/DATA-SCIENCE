arr = []
x = int(input("Enter no of elements"))
for i in range(0,x):
    n=int(input("enter the element"))
    arr.append(n)
print("array is:{arr}",arr)
for i in range(0,x):
    for j in range(i+1,x):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print("The sort no:", arr)
output:
Enter no of elements4
enter the element7
enter the element5
enter the element6
enter the element4
array is:{arr} [7, 5, 6, 4]
The sort no: [4, 5, 6, 7]
