# implementing Stack data structure
size = 0
store = [0] * 100

def push(x):
    global size
    global stack
    size += 1
    store[size-1] = x
    stack = store[:size]


def pop():
    global size
    global stack
    popped_item = stack[size-1]
    size -= 1
    stack = store[:size]
    return popped_item


push(8)
push(4)
push(7)
print(stack)
push(6)
print(stack)
pop()
print(stack)
pop()
print(stack)
push(3)
print(stack)
print(pop())
print(stack)
