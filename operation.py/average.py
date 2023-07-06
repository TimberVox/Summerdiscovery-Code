y=0
x=list[input("Enter a number")]
while True:
    if y!=0:
        y=input("Enter the next number")
        x=x+y
    else:
        break
average=x/len(x)
print(average)