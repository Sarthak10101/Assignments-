x,y,z = input("Enter three numbers :").split()
if x<y and x<z :
    print("The number closest to 0 is ",x)
elif y<z :
    print("The number closest to 0 is ",y)
else :
    print("the number closest to 0 is ",z)
