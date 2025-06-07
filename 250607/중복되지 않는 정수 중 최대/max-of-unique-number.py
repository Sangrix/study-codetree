n = int(input())
data = list(map(int, input().split()))

# Please write your code here.
max_val = 0

for val in data:
    if(max_val<val):
        count = 0
        for elem in data:
            if elem == val:
                count += 1
        if count == 1:
            max_val = val

print(max_val)