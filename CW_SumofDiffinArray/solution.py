
arr = [1]
if arr == []:
    print(0)
arr.sort()
arr = arr[::-1]
x = 0
for i in range(len(arr)-1):
    x += arr[i] - arr[i+1]

print(x)