print ("ax^2+b^x+c=0")
a=int(input("herea"))
b=int(input("hereb"))
c=int(input("herec"))
x1=(-b+(b**2-4*a*c)**1/2)/(2*a)
x2=(-b-(b**2-4*a*c)**1/2)/(2*a)
print ("The answer is"+ str(x1)+"or"+str(x2))