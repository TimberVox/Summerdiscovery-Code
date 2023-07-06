x=int(input("The initial number "))

while x!=1:
    if x%2==1:
        x=x*3+1
        print(x)
        continue
    elif x%2==0:
        x=x/2
        print(x)
        continue
