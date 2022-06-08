a = [3, 8, 9, 7, 6]
k = 3


def solution(A, K):
    shifted_A = A.copy()
    for i in range(len(A)):
        if i + K > len(A) - 1:
            shift_index = (i + K) % len(A)
        else:
            shift_index = i + K
        shifted_A[shift_index] = A[i]
    return shifted_A


print(solution(a, k))
