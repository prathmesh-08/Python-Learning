marks1=int(input("Enter marks 1 :"))
marks2=int(input("Enter marks 2 :"))
marks3=int(input("Enter marks 3 :"))

#TOTAL PERCENTAGE

total_percentage = (marks1+marks2+marks3)/300*(100)

if(total_percentage>=40):
    print("CONGRATULATIONS YOU ARE PASSED ",total_percentage)
else:
    print("YOU ARE FAILED",total_percentage)