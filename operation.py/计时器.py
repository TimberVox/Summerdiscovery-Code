def countUp(n):
    if n==7:
        print("time is up")
        return
    print (n)
    countUp(n+1)
    return
countUp(1)
