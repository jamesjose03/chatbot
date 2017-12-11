# Chat Bot

import time
import random
remider={}
print ("Please enter your name: ")
name=input()
f="y"
while f=="y":
    print ("Welcome, ",name," !, What can I do for you?")
    print ("MENU \n 1. Get current Time & Date \n 2. Set Reminder \n 3. View Reminders \n 4. Roll a die \n 5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        localtime=time.asctime(time.localtime(time.time()))
        print (localtime)
        print ("Have a nice day, ",name)

    elif choice == 2:
        f1=open("reminders.txt","a")
        print ("What is to be reminded, ",name," ?")
        title = input("Title: ")
        print ("At what time?")
        time1=int(input("Time: "))
        print ("Confirm remainder? Y/N: ")
        ch=input()
        if ch=="Y" or ch=="y":
            f1.write(name)
            f1.write("\n")
            f1.write(title)
            f1.write("\n")
            f1.write(str(time1))
            f1.close()
        else:
            print("Remainder cancelled!")

    elif choice == 3:
        
        f2 = open("reminders.txt","r")
        f=f2.readlines()
        for i in range(len(f)):
            if f[i]==(name+"\n"):
                print (name," , your remainders are: ")
                print (f)
                f2.close()

    elif choice == 4:
        print("Roling a die!")
        for i in range(3,0,-1):
            print (i)

        print ("The die rolled: ",random.randint(0,6))
        
    f=input("Do you want to continue ? y/n: ")
