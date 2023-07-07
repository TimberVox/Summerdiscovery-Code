list1=[1,2,3,4,5,6,7,8,9,10]
number=0
for i in list1:
    if i%2==0:
        number=number+i
    else:
        number=number-i
print (number)

list2=["apple","pear","banana","alga"]
for l in list2:
    if l[0]=="a":
        print(l)
    else:
        continue

list3=['adder','elephant','spider','eel']
for p in list3:
    if p[-1]=="r":
        print(p)
    else:
        continue