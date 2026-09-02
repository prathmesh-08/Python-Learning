#FIND WHICH NUMBER IS GREATER
a=int(input("Enter a number 1 : "))
b=int(input("Enter a number 2: "))
c=int(input("Enter a number 3: "))
d=int(input("Enter a number 4: "))

if(a>b and a>c and a>d):
    print("GREATEST NUMBER IS A ",a)
elif(b>a and b>c and b>d):
    print("GREATEST NUMBER IS B ",b)
elif(c>a and c>b and c>d):
    print("GREATEST NUMBER IS C ",c)
elif(d>a and d>b and d>c):
    print("GREATEST NUMBER IS D",d)