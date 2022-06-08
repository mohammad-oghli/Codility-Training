import math

# Time Complexity O(Y - X)
# def solution(X, Y, D):
#     # write your code in Python 3.6
#     m_jmp = 0
#     total_d = 0
#     while Y - X > total_d:
#         total_d += D
#         m_jmp += 1
#     return m_jmp

# Time complexity O(1)
def solution(X, Y, D):
    delta = Y - X
    m_jmp = math.ceil(delta / D)
    return m_jmp

print(solution(10, 85, 30))
