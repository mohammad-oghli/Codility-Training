a = [9, 3, 9, 3, 9, 7, 9]

def solution(A):
    freq_A = {}
    for item in A:
        freq_A[item] = 0
    for item in A:
        freq_A[item] += 1
    for item in A:
        if freq_A[item] % 2 == 1:
            u_element = item
    return u_element

print(solution(a))