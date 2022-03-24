def F(n):
    if n > 2:
        return F(n - 2) + F(n // 2)
    else:
        return n

print(F(9))