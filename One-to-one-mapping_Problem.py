queue = list()

def enqueue(x):
    queue.append(x)

def dequeue():
    return queue.pop(0)

def map_one_to_one(f):
    # counter[x] counts the number of arrows achieve x.
    counter = list(range(len(f)))

    for i in range(len(f)):
        counter[i] = 0

    for i in range(len(f)):
        counter[f[i]] += 1

    for i in range(len(counter)):
        if counter[i] == 0:
            enqueue(i)

    while len(queue) > 0:
        x = dequeue()
        counter[f[x]] -= 1

        if counter[f[x]] == 0:
            enqueue(f[x])

    s = []
    for i in range(len(counter)):
        if counter[i] > 0:
            s.append(i)

    return s

f = [1,1,2,6,5,7,4,9,5,7]
print(map_one_to_one(f))