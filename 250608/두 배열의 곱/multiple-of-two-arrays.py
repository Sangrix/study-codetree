arr_first = [
    [0 for _ in range(3)] for _ in range(3)
]

arr_second = [
    [0 for _ in range(3)] for _ in range(3)
]

arr_multi = [
     [0 for _ in range(3)] for _ in range(3)
]

num_first = 1
num_second =2

for i in range(3):
    for j in range(3):
        arr_first[i][j] = num_first
        num_first += 1


for i in range(3):
    for j in range(3):
        arr_second[i][j] = num_second
        num_second += 1

for i in range(3):
    for j in range(3):
        arr_multi[i][j] = (arr_first[i][j] * arr_second[i][j])
        print(arr_multi[i][j],end = " ")
    print()