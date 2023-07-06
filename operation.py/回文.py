x=input ("你的单词")
y= -1
z= 0
while z<=len(x)-1:
    if x[z]==x[y]:
        if z<len(x)-1:
            z=z+1
            y=y-1
            continue
        else:
            print("这是回文")
            break
    else:
        if z<len(x)-1:
            z=z+1
            y=y-1
        else:
            print ("这不是回文")
            break

