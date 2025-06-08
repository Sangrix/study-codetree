n,m = map(int, input().split())

arr_first = []
arr_second = []
arr_multi = [
    [0 for _ in range(m)] for _ in range(n)
]

for _ in range(n):
    arr = list(map(int,input().split()))
    arr_first.append(arr)

for _ in range(n):
    arr = list(map(int,input().split()))
    arr_second.append(arr)

for i in range(n):
    for j in range(m):
        if(arr_first[i][j] == arr_second[i][j]):
            arr_multi[i][j] = 0

        else:
            arr_multi[i][j] = 1

        print(arr_multi[i][j], end = " ")
    print()