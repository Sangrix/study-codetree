n = int(input())
data = list(map(int,input().split()))

max_val = 0
for i in range(n):
    for j in range(i+1,n):
        val = data[j]-data[i]

        if val > max_val:
            max_val = val

print(max_val)