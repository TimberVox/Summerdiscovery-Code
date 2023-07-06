list0=[]
input_something=input("Enter a list of numbers")
list0=[input_something]
while input_something!="quit":
    y=input("enter a number")
    list0.append(y)
    if y not in list0:
        continue
    else:
        break
print(list0)
