ope=input("What operation do you want to do?")
x1=float (input("the first number is "))
x2=float (input("the last number is "))
if ope == "+":
    print ("The answer is "+str(x1+x2))
elif ope == "-":
    print ("The answer is "+str(x1-x2))
elif ope == "*":
    print ("The answer is "+str(x1*x2))
else:
    if x2==0:
        print ("There is no answer")
    else:
        print ("The answer is "+str(x1/x2))