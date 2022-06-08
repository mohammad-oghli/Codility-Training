a = [3, 1, 2, 4, 3]

def solution(A):
    totalA = sum(A)
    sum_p1 = 0
    min_d = abs(A[0] - (totalA - A[0]))
    for i in range(len(A) - 1):
        sum_p1 += A[i]
        diff = abs(sum_p1 - (totalA - sum_p1))
        if diff < min_d:
            min_d = diff
    return min_d

print(solution(a))
