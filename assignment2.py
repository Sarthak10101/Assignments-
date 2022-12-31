x,y,z =  input("Enter three numbers :").split()
X = int(x)
Y= int(y)
Z = int (z)
if X<Y and X<Z :
    print("The number closest to 0 is ",X)
elif Y<Z :
    print("The number closest to 0 is ",Y)
else :
    print("the number closest to 0 is ",Z)
print (X+Y)    