x=input ("Choose a word you like")
if x[::1]==x[::-1]:
    print ("This is palindrome.")
else:
    print("This is not palindrome")