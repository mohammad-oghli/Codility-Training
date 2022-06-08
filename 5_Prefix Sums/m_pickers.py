# Mushroom Pickers
def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P


def count_total(P, x, y):
    return P[y + 1] - P[x]


a = [2, 3, 7, 5, 1, 3, 9]
p = prefix_sums(a)
k = 4
m = 6
moves = 0
total_m = 0
delta_p2 = len(a) - 1 - k
if delta_p2 >= m:
    total_m += count_total(p, k, k + m)
    # total_m += p[k + m + 1] - p[k]
else:
    total_m += count_total(p, k, len(a) - 1)
    # total_m += p[len(a)] - p[k]
    m = m - 2 * delta_p2
    if m > 0:
        delta_p1 = len(a) - 1 - delta_p2
        if delta_p1 > m:
            delta_p1 = m
        total_m += count_total(p, k - delta_p1, k - 1)
        # total_m += p[k] - p[k - delta_p1]

print(total_m)
