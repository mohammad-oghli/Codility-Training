# implementing Queue data structure
head, tail = 0, 0
store = [0] * 100
N = 10  # number of queue elements


def push(x):
    global tail
    global queue
    tail = (tail + 1) % N
    store[tail - 1] = x
    queue = store[head:tail]


def pop():
    global head
    global queue
    popped_item = queue[0]
    head = (head + 1) % N
    queue = store[head:tail]
    return popped_item


def size():
    return (tail - head + N) % N


def empty():
    return head == tail


print(empty())
print(size())
push(4)
push(8)
print(queue)
push(6)
print(queue)
pop()
print(queue)
print(pop())
print(queue)
push(3)
print(queue)
print(empty())
print(size())
