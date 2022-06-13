str = "{[()()]}"
#str = "([)()]"


def solution(S):
    lb_arr = ["[", "{", "("]
    rb_arr = ["]", "}", ")"]
    stack = []
    balanced = 1
    for ch in S:
        if ch in lb_arr:
            stack.append(ch)
        elif ch in rb_arr and len(stack) > 0:
            lb = stack.pop()
            lx = lb_arr.index(lb)
            rx = rb_arr.index(ch)
            if lx != rx:
                balanced = 0
                break
        else:
            balanced = 0
    if balanced:
        if stack:
            balanced = 0
    return balanced


print(solution(str))
