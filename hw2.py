# Name: Cody Alan Swearingen
# Evergreen Login: swecod03
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

import hw2_test

###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

x = hw2_test.n
y = 1
z = 0
while (x > 50):
    z = z+(x+y)
    x = x - 1
    y = y + 1
print z

###
### Problem 2
###
print "\n"
print "Problem 2 solution follows:"

for x in range (2,11):
    print (1.0/x)

###
### Problem 3
###
print "\n"
print "Problem 3 solution follows:"

n = 10
tri = 0
for i in range(11):
    tri = (tri + n)
    if tri == 110:
        tri = tri/2

print "Triangular number", n, "via loop:", tri
print "Triangular number", n, "via formula:", n*(n+1)/2

###
### Problem 4
###
print "\n"
print "Problem 4 solution follows:"

n = 10
f = 1
for i in range (9):
    n = n*f
    f = f+1
print n

###
### Problem 5
###
print "\n"
print "Problem 5 solution follows:"

b = []
n = 10
j = 1
k = 1
l = 1
for i in range (n):
    l = j*k
    k = k+1
    j = l
    b.insert(0,l)
print b[0]
print b[1]
print b[2]
print b[3]
print b[4]
print b[5]
print b[6]
print b[7]
print b[8]
print b[9]

###
### Problem 6
###
print "\n"
print "Problem 6 solution follows:"

b = []
n = 10
j = 1
k = 1
l = 1
u = 0
for i in range (n):
    l = j*k
    k = k+1
    j = l
    u = l**-1
    b.insert(0,u)
print b[0]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]+b[7]+b[8]+b[9]+1


###
### Collaboration
###

# I used docs.python.org for most of my references for coding.

###
### Reflection
###

# I mostly relied on online learning for this assignment. I used while and for
#functions for basic coding, but moved on to the use of lists to cache any
#values that I needed. This assignment took me approximately three hours total.
