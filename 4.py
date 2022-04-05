def cnt(str):
    it = set()
    for i in str:
        it.add(i)
    return len(it)


with open("input.txt") as f:
    a = f.readlines()
a = [i.rstrip('\n') for i in a]

ml = 0
for i in a:
    if len(i) > ml:
        ml = len(i)

val = 1

for i in range(ml):
    for j in a:
        if cnt(j) == val:
            print(j)
    val += 1
