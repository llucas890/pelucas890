def pushZerosToEnd(arr, n):
    count = 0
    for i in range(n):
        if arr[i] != 0:
             

            arr[count] = arr[i]
            count+=1
    while count < n:
        arr[count] = 0
        count += 1
         

arr = [4, 0, 5, 0, 3, 0, 0, 5]
n = len(arr)
pushZerosToEnd(arr, n)
print(arr)