a = []
s = set()
n = int(input())

for i in range(n):
    el = int(input())
    a.append(el)
    s.add(el)

print(len(s))

for i in s:
    print(i, "--", a.count(i))
