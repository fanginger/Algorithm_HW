

def enqueue(myQueue, val):
    for i in range(len(a)-1,0,-1):
        a[i] = a[i-1]
    a[0] = val


a = [5, 4, 3, 2, 1]
print(a)
# a = [5, 5, 4, 3, 2]
# a = [6, 5, 4, 3, 2]

enqueue(a, 6)
print(a)