# (0,0), (1,0), (1,1), (2,0), (2,1), (2,2)....

arr_2d = []

for _ in range(4):
    arr = list(map(int,input().split()))
    arr_2d.append(arr)

sum_val = 0

for i in range(4):
    j = 0
    while(j<=i):
        sum_val += arr_2d[i][j]
        j+=1

print(sum_val)