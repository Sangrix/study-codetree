n = int(input())
m = list(map(int,input().split()))
count = 0

for i in range(n):
    if(m[i]==2):
        count += 1
    
    if(count==3):
        print(i+1)
        break
    