arr = [1,1,0,-1,-1]

length = len(arr)
# print(length)

pos_list = []
zer_list = []
neg_list = []

for i in arr:
    if i < 0:
        neg_list.append(i)
    elif i == 0:
        zer_list.append(i)
    else:
        pos_list.append(i)

# print(neg_list)
# print(pos_list)
# print(zer_list)
# print('%.6f' % 2)

print("{:.6f}".format(len(pos_list)/length))
print("{:.6f}".format(len(neg_list)/length))
print("{:.6f}".format(len(zer_list)/length))