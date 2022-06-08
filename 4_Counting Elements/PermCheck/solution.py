a = [4, 1, 3, 2]


# a = [4, 1, 3]
# a = [9, 5, 7, 3, 2, 7, 3, 1, 10, 8]
# a = [1]
# def solution(A):
#     if len(A) <= 1 and A[0] > 1:
#         return 0
#     freq_arr = [0] * (max(A) + 1)
#     sum_freq = 0
#     for item in A:
#         freq_arr[item] += 1
#         sum_freq += 1
#         if freq_arr[item] > 1:
#             return 0
#     if sum_freq == max(A):
#         return 1
#     return 0

def solution(A):
    freq_dict = {}
    for elem in A:
        freq_dict[elem] = 0
    for elem in A:
        freq_dict[elem] += 1
        if freq_dict[elem] > 1:
            return 0
    if sum(freq_dict.values()) == max(A):
        return 1
    return 0


print(solution(a))
