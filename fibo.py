temp = int(input("Number to check: "))
a = 0
b = 1
c = b
i=0
while(i!=1):
    a = b
    b = c
    c = a+b
    if(c == temp):
        print("It is a fibonacci number")
        break
        
    elif(c>temp):
        print("It is not a fibonacci number")
        break