# Name: Keir Allison-Bourne     
# Evergreen Login: allkei20
# Computer Science Foundations
# Programming as a Way of Life
# Homework 6

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

def func(x,y,z):
    answer = 0 
    x * y = answer
    answer = answer + z
    return answer

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

a = random(3)
result = func(a[0],a[1],a[2])
print result

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

tel = {'Joe': 1112223333, 'Bob': 2223334444, 'Zach' : 3334445555}
del tel['Bob']
tel ['Suzy'] = 4445556666
print tel

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

b = random(10)
print b

for i in len(b):
    b[i] + 1

print b

###
### Problem 7
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 7 solution follows:"

c = random(10)
even = 0
odd = 0

for i in len(c):
    if (c[i]%2==0):
        for j in len(c):
            product = c[i] * c[j]
            even = even + product
    else:
        for h in len(c):
            oddsum = c[i] + c[h]
            odd = odd + oddsum

print even, odd 

###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").
