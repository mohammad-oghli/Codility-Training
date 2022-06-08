a = [2, 3, 1, 5]

def solution(A):
    if len(A) == 0:
        m_item = 1
    elif len(A) == 1:
        if A[0] > 1:
            m_item = A[0] - 1
        else:
            m_item = 2
    else:
        rn = max(A)
        total = 0
        for i in range(1, rn + 1):
            total += i
        if total - sum(A) == 0:
            m_item = rn + 1
        else:
            m_item = total - sum(A)
    return m_item

print(solution(a))