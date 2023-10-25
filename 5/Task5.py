list_num = list(input())
print(list_num)
list_num = [int(item) for item in list_num]
difference = -1
if len(list_num) >= 2:
    difference = list_num[1] - list_num[0]
else:
    print("No")
    exit()
for i in range(len(list_num) - 1):
    if list_num[i + 1] - list_num[i] != difference:
        print("No")
        break
else:
    print("Yes")