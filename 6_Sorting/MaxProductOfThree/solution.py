a = [-3, 1, 2, -2, 5, 6]

# Time complexity O(NlogN)
# def solution(A):
#     A.sort()
#     # most lowests with the biggest
#     lowest_2 = A[0] * A[1] * A[-1]
#     # most biggests
#     biggest_3 = A[-1] * A[-2] * A[-3]
#     return max(lowest_2, biggest_3)

# Time complexity O(NlogN)
def solution(A):
    if len(A) < 3:
        return 0
    if len(A) == 3:
        return A[0] * A[1] * A[2]
    A.sort()
    p_arr = []
    n_arr = []
    for item in A:
        if item >= 0:
            p_arr += [item]
        else:
            n_arr += [item]
    if len(p_arr) >= 3 and len(n_arr) >= 2:
        return max(p_arr[-1] * p_arr[-2] * p_arr[-3], n_arr[0] * n_arr[1] * p_arr[-1])
    elif 0 < len(p_arr) < 3 and len(n_arr) >= 2:
        return n_arr[-1] * n_arr[-2] * p_arr[-1]
    elif len(p_arr) >= 3 and len(n_arr) < 2:
        return p_arr[-1] * p_arr[-2] * p_arr[-3]
    else:
        return n_arr[-1] * n_arr[-2] * n_arr[-3]

print(solution(a))