n = 20
a = list()
min = 1e9

for i in range(20):
    j = int(input())
    a.append(j)
    if j % 6 == 0 and j < min:
        min = j

print(min)
