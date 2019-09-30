

def push(myStack, val):
    max = 5
    if len(myStack) < max:
        myStack.append(None) # add some space
        for i in range(len(a)-1,0,-1):
            a[i] = a[i-1]
        a[0] = val

def pop(myStack):

    return

# max 5
#a = [5, 4, 3, 2, 1]
#print(a)

## Push example
## Larger than 5, do not allow to push
a = [ 4, 3, 2, 1]
print(len(a))
#a = [5, 4, 3, 2, 1]
print(a.pop())
print(len(a))
## You can push
# a = [4, 3, 2, 1]
# push(a, 6)
# a = [6, 4, 3, 2, 1]


# print(a)