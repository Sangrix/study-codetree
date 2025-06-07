n = int(input())
data = list(map(int, input().split()))

min_val = data[1]-data[0]
for i in range(1,n-1):
    if(min_val>(data[i+1] - data[i])):
        min_val = (data[i+1]-data[i])
print(min_val)