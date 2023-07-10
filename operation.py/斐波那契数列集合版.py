def fibonacci(n):
    list1=[1]
    x=1
    for i in range(0,n):
        list1.append(x)
        x=list1[-1]+list1[-2]
    return (list1[n])
print(fibonacci(7))