# Name: Keir Allison-Bourne
# Evergreen Login: allkei20
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

import hw2_test

n = hw2_test.n
x = 0
gaussnum = 0

while ( x <= n ):
    gaussnum = x + gaussnum
    x = x + 1 

print gaussnum
        
###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

for x in range(10):
    answer = 1.0/(x+1)
    print answer
    
###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

n = 10
triangular = 0

for i in range(n):
    triangular = (i+1) + triangular
    
print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", n*(n+1)/2

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

n = 10
factorial = 1

for f in range(n):
    factorial = (f+1) * factorial
    
print factorial

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

numlines = 10

for s in range(numlines):
    p = numlines - s
    factorial2 = 1
    for q in range(p):
        factorial2 = (q+1) * factorial2
    print factorial2

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

numlines = 10
sumofrec = 1

for s in range(numlines):
    p = numlines - s
    factorial2 = 1
    for q in range(p):
        factorial2 = (q+1) * factorial2
    factorial2 = 1.0 / factorial2
    sumofrec = factorial2 + sumofrec
print sumofrec

###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").

###
### Reflection
###

# ... Write how long this assignment took you, including doing all the readings
# ... and tutorials linked to from the homework page. Did the readings, tutorials,
# ... and lecture contain everything you needed to complete this assignment?
