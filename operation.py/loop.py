ope=0
while not  ope=="quit":
    ope=input("What operation do you want to do?")
    if not ope=="quit":
        x1=float (input("the first number is "))
        x2=float (input("the last number is "))
        if ope == "+":
            print ("The answer is "+str(x1+x2))
        elif ope == "-":
            print ("The answer is "+str(x1-x2))
        elif ope == "*":
            print ("The answer is "+str(x1*x2))
        elif ope == "/":
            if x2==0:
                print ("There is no answer")
            else:
                print ("The answer is "+str(x1/x2))
        else:
            print ("Sorry, I am not able to deal with this")
    else:
        exit