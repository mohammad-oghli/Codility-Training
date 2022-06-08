a = [0, 1, 0, 1, 1]


# Time Complexity O(N^2)
# def solution(A):
#     np = 0
#     for i in range(len(A) - 1):
#         for j in range(i + 1, len(A)):
#             if A[i] == 0 and A[j] == 1:
#                 np += 1
#     if np > 1000_000_000:
#         return -1
#     return np


def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P


# Time Complexity O(N)
def solution(A):
    np = 0
    prefix = prefix_sums(A)
    for i in range(len(A)):
        if A[i] == 0:
            np += prefix[len(A)] - prefix[i]
    if np > 1000_000_000:
        return -1
    return np

print(solution(a))
