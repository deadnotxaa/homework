n = 10
a = []
s = [[0] * n for i in range(n)]
s2 = [[0] * n for i in range(n)]

for i in range(n):
    a.append(list(map(int, input().split())))

s[0][0] = a[0][0]
s2[0][0] = a[0][0]

for j in range(1, n):
    s[0][j] = s[0][j - 1] + a[0][j]

for i in range(1, n):
    s[i][0] = s[i - 1][0] + a[i][0]

for i in range(n):
    for j in range(n):
        if i and j:
            s[i][j] = max(s[i - 1][j], s[i][j - 1]) + a[i][j]


for j in range(1, n):
    s2[0][j] = s2[0][j - 1] + a[0][j]

for i in range(1, n):
    s2[i][0] = s2[i - 1][0] + a[i][0]

for i in range(n):
    for j in range(n):
        if i and j:
            s2[i][j] = min(s2[i - 1][j], s2[i][j - 1]) + a[i][j]

print(s[n - 1][n - 1], s2[n - 1][n - 1], sep="")
