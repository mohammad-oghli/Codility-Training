def solution(n):
    left_i = -1
    right_i = -1
    max_b = 0
    b_num = format(n, "b")
    for i in range(len(b_num)):
        if b_num[i] == '1':
            if left_i == -1:
                left_i = i
            else:
                right_i = i
        if left_i != -1 and right_i != -1:
            len_b = len(b_num[left_i + 1:right_i])
            if len_b > max_b:
                max_b = len_b
            left_i = right_i
            right_i = -1
    return max_b


# 529 -> 1000010001
# should return 4
print(solution(529))
