n = 5

for i in range(1,n+1):
    # print(i)
    for j in range(n-i):
        print(' ',end='')
    for k in range(i):
        print('#',end='')
    print()