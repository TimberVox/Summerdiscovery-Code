import random
while True:
    g=0
    y=int(random. randrange(0,101,1))
    while True:
        x=(input("Guess what my number is. "))
        if x=="q":
            break
        elif x=="r":
            break
        elif x=="z":
            print(y)
            continue
        elif x==input ("s",200):
            break
        elif int(x)>y:
            print("No, my number is lower than ",str(x)," .")
            continue
        elif int(x)<y:
            print("No, my number is higher than ",str(x)," .")
            continue
        else:
            print("Yes, you are right.")
            break
    g=x
    if g==200:
        break
    if g=="q":
        break
    if g=="r":
        continue
    z=input("Do you want to play again? ")
    if z=="N":
        break
    if z=="Y":
        continue
