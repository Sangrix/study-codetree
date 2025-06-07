n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
min_val=arr[0]
count = 0

for elem in arr:
    if(min_val==elem):
        count += 1
    elif(min_val>elem):
        min_val = elem
        count = 1
    
print(min_val, count)