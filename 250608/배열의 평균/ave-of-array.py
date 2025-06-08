arr_2d = []
for _ in range(2):
    arr = list(map(int,input().split()))
    arr_2d.append(arr)

for i in range(2):
    sum_arr = 0
    for j in range(4):
        sum_arr += arr_2d[i][j]
    avg_arr = sum_arr/4.0
    print(round(avg_arr,1), end = " ")
print()

for i in range(4):
    sum_arr = 0
    for j in range(2):
        sum_arr += arr_2d[j][i]
    avg_arr = sum_arr/2.0
    print(round(avg_arr,1),end=" ")
print()

sum_val = 0
for i in range(2):
    for j in range(4):
        sum_val+=arr_2d[i][j]
    avg_arr = sum_val/8.0
print(round(avg_arr,1),end=" ")