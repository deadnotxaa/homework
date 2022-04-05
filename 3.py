with open("input.txt") as f:
    a = f.readlines()

a = [i.rstrip('\n') for i in a]

ml = 0
for i in a:
    if len(i) > ml:
        ml = len(i)

for i in a:
    if len(i) == ml:
        print(i)
