#!/usr/bin/python3
a = [ 2, 4, 6 ]
def rec():
    if len(a) == 1:
        return a[0]
    else:
        return a.pop() + rec()
#print (rec())
def rec2():
    if len(a) == 0:
        return 0
    else:
        x=a.pop()
        return 1 + rec2()

#print (rec2())
maximum = 0
def rec3(maximum):
    if len(a) == 0:
        return maximum
    else:
        x=a.pop()
        if maximum < x:
            maximum = x
        return rec3(maximum)
print (rec3(maximum))
