n = 30
a = list()
sum = 0
s = 0

for i in range(20):
    m = int(input())
    a.append(m)
    if m < 0:
        s += 1
        sum += m

print(sum)
if s == 30:
    print('there is no numbers below zero')
