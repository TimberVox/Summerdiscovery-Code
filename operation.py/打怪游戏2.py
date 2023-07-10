def factorial(n):
    x=1
    for y in range(1,n+1) :
        x=x*y
    return x
print(factorial(3))

t=[7,78,90,32]
def max(l):
    q=t[0]
    for i in t:
        if i>q:
            q=i
        else:
            continue
    return q
print(max(t))


bits=[1,0,1,0,1]
data=["octopus",89,"jellyfish",70,"inkfish"]

def mask(bits,data):
    list1=[]
    n=0
    for g in range(0,len(bits)):
        if bits[g]==1:
            list1.append(data[g])
        elif bits[g]==0:
            continue
    return list1
print(mask(bits,data))