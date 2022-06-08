a = [10, 2, 5, 1, 8, 20] # -> should return 1
#a = [10, 50, 5, 1] # -> should return 0

# Brute force time complexity O(N^3)
# def solution(A):
#     A.sort()
#     for i in range(len(A) - 2):
#         for j in range(i + 1, len(A) - 1):
#             for k in range(j + 1, len(A)):
#                 triangle_cond = A[i] + A[j] > A[k]
#                 if not triangle_cond:
#                     break
#                 triangle_cond &= A[i] + A[k] > A[j]
#                 triangle_cond &= A[j] + A[k] > A[i]
#                 if triangle_cond:
#                     return 1
#     return 0

# Dynamic programming time complexity O(NlogN)
def solution(A):
    A.sort()
    triangle_cond = False
    i = 0
    while not triangle_cond and i < len(A) - 2:
        for j in range(i + 1, len(A) - 1):
            triangle_cond = A[i] + A[j] > A[j + 1]
            if not triangle_cond:
                break
            triangle_cond &= A[i] + A[j + 1] > A[j]
            triangle_cond &= A[j] + A[j + 1] > A[i]
            if triangle_cond:
                return 1
        i += 1
    return 0

print(solution(a))