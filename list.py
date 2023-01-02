a=[]
b=[]

sum1= 0
sum2 = 0
for i in range (20) :
    c =(input ("Enter a number :"))
    c =int (c)
    if c % 2==0 :
        a.append(c)
        sum1 = sum1 + c
    else :
        b.append(c) 
        sum2 = sum2 + c   
print(a)
print (b)
print("The sum of first 10 even numbers is ",sum1)
print ("The sum of first 10 odd numbers is",sum2)


