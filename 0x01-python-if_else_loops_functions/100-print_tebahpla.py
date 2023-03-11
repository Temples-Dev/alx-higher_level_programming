#!/usr/bin/python3
def revalpha():
    s=""
    for i in reversed(range(ord('a'), ord('z')+1)):
        if i in range(97, 123):
            if (ord('a') - i) % 2 == 0:
                s+= chr(i -32)
            else:
                s += chr(i)
        else:
            s += chr(i)
    print(s,end="")
revalpha()
