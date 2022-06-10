n = int(input())
k = int(input())


def F(n, k):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 1

    return F(n - 1, k) + F(n - 2, k) * k


print(F(n, k))

#print