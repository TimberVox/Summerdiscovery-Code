x=input("你的单词")
if x [int((len(x)-1)/2)]==x [int(-(len(x)+1)/2)] and x[int((len(x)-3)/2)]==x[int(-(len(x)+3)/2)]:
    print ("这个是回文")

else:
    print ("这个不是回文")
