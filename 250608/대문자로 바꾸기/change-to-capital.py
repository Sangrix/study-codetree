n = 5
arr_2d = []
for _ in range(n):
    arr = list(input().split())
    arr_2d.append(arr)

for i in range(n):
    for j in range(3):
        arr_2d[i][j] = chr(ord(arr_2d[i][j]) + ord('A') - ord('a'))
        print(arr_2d[i][j], end = " ")
    print()