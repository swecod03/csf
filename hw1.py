# Name: Cody Swearingen
# Evergreen Login: swecod03
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1 solution follows:"

bit = math.sqrt((0-5.86)**2-4*8.5408)
plus = (5.86 + bit) / 2
minus = (5.86 - bit) / 2
print "Value 1"
print minus
print "Value 2"
print plus

###
### Problem 2
###

print "Problem 2 solution follows:"

import hw1_test
dan = hw1_test
print dan.a
print dan.b
print dan.c
print dan.d
print dan.e
print dan.f

###
### Problem 3
###

print "Problem 3 solution follows:"

print str ((dan.a and dan.b) or (not dan.c) and not (dan.d or dan.e or dan.f))

###
### Collaboration
###

# ... List your collaborators here, as a comment (on a line starting with "#").

# Worked along with ngungo16 to solve math.
# Assisted ngungo16 and vancho06 with programming logic

# 10/03/13 - added reflections to desc.
