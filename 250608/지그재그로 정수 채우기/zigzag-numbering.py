n, m = map(int, input().split())

# Please write your code here.
arr_2d=[
    [0 for _ in range(m)] for _ in range(n)
]

num = 0

for i in range(m):
    if(i%2==0):
        for j in range(n):
            arr_2d[j][i] = num
            num+=1
    else:
        for j in range(n-1,-1,-1):
            arr_2d[j][i] = num
            num += 1

for i in range(n):
    for j in range(m):
        print(arr_2d[i][j], end = " ")
    print()
        
        