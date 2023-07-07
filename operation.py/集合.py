list0=[]
input_something=input("Enter a list of numbers")
list0=[input_something]
while input_something!="quit":
    y=input("enter a number")
    if y not in list0:
        list0.append(y)
        continue
    elif y=="quit":
        break
    elif y in list0:
        continue
print(list0)
