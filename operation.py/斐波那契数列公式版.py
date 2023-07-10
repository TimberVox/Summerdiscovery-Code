def fibonacci(n):
    x=int(n)
    if x==1:
        fibonacci(x)==1
    elif x>1:
        fibonacci(x)==(1/5**(1/2))((((1+5**(1/2))/2)**x)-(((1-5**(1/2)))/2)**x)
    return fibonacci(n)
print(fibonacci(7))