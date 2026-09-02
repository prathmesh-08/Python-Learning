a= int(input("Enter your age:"))
#IF STATEMENT NO 1      IT IS INDEPENDENT 
if(a%2 == 0):
    print("a is even")
    #END OF IF STATEMENT NO 1
    
    #IF STATEMENT NO 2
if(a>18):
    print("you can drive")
elif(a<0):
    print("Bc Age is invalid")
elif(a==0):
    print("Bc Age is invalid")
    
    
else:
    print("no buddy you cannot drive")
    
    print("End of program")