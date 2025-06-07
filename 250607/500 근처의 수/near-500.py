data = list(map(int,input().split()))

max_val = 0
min_val = 1000

for elem in data:
    if(elem<500):
        if(max_val<elem):
            max_val = elem

for elem in data:
    if(elem>500):
        if(min_val>elem):
            min_val = elem


print(max_val, min_val)