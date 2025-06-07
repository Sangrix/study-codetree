n = list(map(int,input().split()))

max_val = 0

for elem in n:
    if(max_val<elem):
        max_val = elem

print(max_val)