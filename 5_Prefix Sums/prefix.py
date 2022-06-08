a = [4, 1, 3, 2]


def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P


P = prefix_sums(a)
print(P)
slice = P[4] - P[1]
print(slice)
