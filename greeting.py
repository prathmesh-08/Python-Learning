import time

name = input("Enter your name: ")
hour = int(time.strftime("%H"))

if hour < 12:
    print("Good Morning", name)
elif hour < 17:
    print("Good Afternoon", name)
else:
    print("Good Evening", name)