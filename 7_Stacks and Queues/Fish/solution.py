a = [4, 3, 2, 1, 5]
b = [0, 1, 0, 0, 0]
# a = [4, 3, 2, 1, 5,9,12,6,8,10]
# b = [0, 1, 0, 0, 0,0,1,1,0,0] -> 4
# a = [4, 3, 2, 1, 5,9,12]
# b = [0,1,1,1,1,1,1] -> 7
# b = [1,0,0,0,0,0,0] -> 3

# time complexity O(N^2)
# def solution(A, B):
#     i = 0
#     j = i + 1
#     f_cycle = True
#     while i < len(B)-1 and f_cycle:
#         if B[i] == 1 and B[j] == 0:
#             if A[i] > A[j]:
#                 A.pop(j)
#                 B.pop(j)
#             else:
#                 A.pop(i)
#                 B.pop(i)
#         else:
#             i += 1
#             j = i + 1
#         if i == len(B)-1:
#             found = False
#             for k in range(len(B) - 1):
#                 if B[k] == 1 and B[k + 1] == 0:
#                     i = k
#                     j = i + 1
#                     found = True
#                     break
#             if not found:
#                 f_cycle = False
#     return len(A)

# time complexity O(N)
def solution(A, B):
    stack_1 = []
    survival = 0
    for ix, f_size in enumerate(A):
        if B[ix] == 1:
            stack_1.append(f_size)
        else:
            while len(stack_1) > 0:
                if stack_1[-1] > f_size:
                    break
                else:
                    stack_1.pop()
            if len(stack_1) == 0:
                survival += 1
    survival += len(stack_1)
    return survival

print(solution(a, b))

