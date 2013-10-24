# Cody Alan Swearingen
# swecod03
# Collaborators: Steven, Alexei
n = raw_input('please enter a number: ')
n = int(n)
series = raw_input('fibonacci or sum?: ')
if series == "fibonacci":
    x = 0
    y = 0
    z = 0
    for i in range(n):
        z = x+y
        y = x
        x = z
        if z == 0:
            print 1
            x = 1
        else:
            print z
elif series == "sum":
    p = 0
    q = 0
    r = 0
    s = 0
    for i in range(n+1):
        r = p
        q = q+1
        p = 3*q
        s = s+r
    print s
else:
    print "INVALID STRING YO"