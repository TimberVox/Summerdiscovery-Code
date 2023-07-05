print ("y1=ax+b and y2=cx+d")
a=int(input ("what is a "))
b=int(input ("what is b "))
c=int(input ("waht is c "))
d=int(input ("what is d "))

if a==c:
    print ("these lines are parallel")
if a>c or a<c:
    x=(d-b)/(a-c)
    y=a*x+b
    print ("the y intersect is "+str(y)+" and the x intersect is "+str(x))