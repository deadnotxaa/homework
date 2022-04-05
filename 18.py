def isD(str):
    for i in range(1, len(str)):
        if str[i] == str[i - 1]:
            return True
    return False


with open("input.txt") as f:
    a = f.readlines()

a = [i.rstrip("\n") for i in a]

for i in a:
    if isD(i):
        print(i)
