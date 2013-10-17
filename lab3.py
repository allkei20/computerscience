# Keir Allison-Bourne
# allkei20 
# Lab 3 

# enter a value for n 

# enter either "fibonacci" or "sum" into the variable "series" to decide 
# which algorithm to apply to n 

n = 0
series = ""

if ( series is "fibonacci" ):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    print n,"th fibonacci term:",a
else:    
    if ( series is "sum" ):
        sum = 0
        for i in range(n+1):
            sum = 3*i + sum
        print "sum:", sum
    
    else:
        print "Invalid string"