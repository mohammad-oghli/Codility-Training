# a = [1, 3, 1, 3, 2, 1, 3]
a = [1, 3, 1, 4, 2, 3, 5, 4]

# def solution(X, A):
#     positions = [0] * (X+1)
#     for i in range(len(A)):
#             positions[A[i]] = 1
#             if sum(positions) == X:
#                 return i
#     return -1


def solution(X, A):
    positions = [0] * (X + 1)
    sum_pos = X
    for i in range(len(A)):
        if positions[A[i]] == 0:
            sum_pos -= 1
            positions[A[i]] = 1
        if sum_pos == 0:
            return i
    return -1


print(solution(5, a))
