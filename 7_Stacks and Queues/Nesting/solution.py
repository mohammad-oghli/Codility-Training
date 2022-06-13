s = "(()(())())"
# s = "())"

# time complexity O(N)
def solution(S):
    lb = "("
    rb = ")"
    stack = []
    balanced = 1
    for ch in S:
        if ch in lb:
            stack.append(ch)
        elif ch in rb and len(stack) > 0:
            stack.pop()
        else:
            balanced = 0
    if balanced:
        if stack:
            balanced = 0
    return balanced


print(solution(s))
