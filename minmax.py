arr = [6,3,5,7,9]

arr.sort()
minsum = maxsum = 0

for i in range(len(arr)-1):
    minsum += arr[i]

for j in range(1,len(arr)):
    maxsum += arr[j]

print(f"{minsum} {maxsum}")