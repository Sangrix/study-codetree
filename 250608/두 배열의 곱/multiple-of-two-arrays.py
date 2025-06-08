arr_first = []
for _ in range(3):
    arr = list(map(int,input().split()))
    arr_first.append(arr)

arr_second = []
for _ in range(3):
    arr = list(map(int,input().split()))
    arr_second.append(arr)

arr_multi = [
     [0 for _ in range(3)] for _ in range(3)
]

for i in range(3):
    for j in range(3):
        arr_multi[i][j] = arr_first[i][j] * arr_second[i][j]
        print(arr_multi[i][j],end = " ")
    print()