n = int(input())
data = list(map(int, input().split()))

# Please write your code here.

data.sort(reverse=True)
print(data[0],data[1])