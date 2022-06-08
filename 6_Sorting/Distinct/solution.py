a = [2, 1, 1, 2, 3, 1]

# Time complexity O(N) or O(NlogN)
# def solution(A):
#     d_elem = set()
#     for item in A:
#         d_elem.add(item)
#     return len(d_elem)

# Time complexity O(N) or O(NlogN)
def solution(A):
    if len(A) == 0:
        dn = 0
    else:
        dn = 1
    A.sort()
    for i in range(len(A)-1):
        if A[i] != A[i + 1]:
            dn += 1
    return dn

print(solution(a))

