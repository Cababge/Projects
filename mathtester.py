import math
import random
import tkinter as tk
# The different levels to correspond to the different levels of difficulty
# of the sums that are given
def P1():
    global y
    global x
    global answer
    global question
    global valid
    y = 0
    x = 1
    while (y < x): #Random number generator that makes sure the biggers numbers comes first
        x = random.randint(1,50)
        y = random.randint(1,50)
    operator = random.randint(1,2)
    if operator == 1:
        question = print("What is {} + {}?".format(y,x))
        answer = y+x
    elif operator == 2:
        question = print("What is {} - {}?".format(y,x))
        answer = y-x
        return answer
    valid = True

#**************************************************************************************************

def P2():
    global y
    global x
    global answer
    global valid
    y = 0
    x = 1
    while (y < x):
        x = random.randint(1,500)
        y = random.randint(1,500)
    operator = random.randint(1,2)
    if operator == 1:
        print("What is {} + {}?".format(y,x))
        answer = y+x
    elif operator == 2:
        print("What is {} - {}?".format(y,x))
        answer = y-x
        return answer
    valid = True

#**************************************************************************************************
    
def P3():
    global y
    global x
    global answer
    global valid
    y = 0
    x = 1
    while (y < x) or y%x !=0:
        x = random.randint(2,9)
        y = random.randint(200,700)
    operator = random.randint(1,2)
    if operator == 1:
        print("What is {} * {}?".format(y,x))
        answer = y*x
    elif operator == 2:
        print("What is {} / {}?".format(y,x))
        answer = y/x
        return answer
    valid=True

#**************************************************************************************************
            
def P4():
    global y
    global x
    global answer
    global valid
    y = 0
    x = 1
    while (y < x):
        x = random.randint(3,14)
        y = random.randint(200,800)
    operator = random.randint(1,2)
    if operator == 1:
        print("What is {} * {}?".format(y,x))
        answer = y*x
    elif operator == 2:
        print("What is {} * {}?".format(y,x))
        answer = y*x
        return answer
    elif operator == 3:
        x = 1
        y = 0
        while (y < x) or y%x != 0:
            x = random.randint(2000,5000)
            y = random.randint(4500,12000)
        print("What is {} + {}?".format(y,x))
        answer = y+x
    elif operator == 4:
        x = 1
        y = 0
        while (y < x) or y%x != 0:
            x = random.randint(2000,5000)
            y = random.randint(4500,12000)
        print("What is {} - {}?".format(y,x))
        answer = y-x 
    valid = True

#**************************************************************************************************

def P5():
    global y
    global x
    global answer
    global valid
    y = 0
    x = 1
    while (y < x) or y%x != 0:
        x = random.randint(3,19)
        y = random.randint(300,1700)
    operator = random.randint(1,4)
    if operator == 1:
        print("What is {} * {}?".format(y,x))
        answer = y*x
    elif operator == 2:
        print("What is {} / {}?".format(y,x))
        answer = y/x
        return answer
    elif operator == 3:
        x = 1
        y = 0
        while (y < x) or y%x != 0:
            x = random.randint(4000,10000)
            y = random.randint(5000,30000)
        print("What is {} + {}?".format(y,x))
        answer = y+x
    elif operator == 4:
        x = 1
        y = 0
        while (y < x) or y%x != 0:
            x = random.randint(4000,10000)
            y = random.randint(5000,30000)
        print("What is {} - {}?".format(y,x))
        answer = y-x 
    valid = True

#**************************************************************************************************

def P6():
    global y
    global x
    global answer
    global valid
    y = 0
    x = 1
    while (y < x) or y%x != 0:
        x = random.randint(3,19)
        y = random.randint(400,2000)
    operator = random.randint(1,4)
    if operator == 1:
        placement = random.randint(1,2)
        if placement == 1:
            print("What is {} * {}?".format(y,x))
            answer = y*x
        elif placement == 2:
            print("____ * {} = {}".format(x,x*y))
            answer = y
    elif operator == 2:
        print("What is {} / {}?".format(y,x))
        answer = y/x
        return answer
    elif operator == 3:
        x = 1
        y = 0
        while (y <= x) or y%x != 0:
            x = random.randint(4000,10000)
            y = random.randint(5000,20000)
        print("What is {} + {}?".format(y,x))
        answer = y+x
    elif operator == 4:
        x = 1
        y = 0
        while (y <= x) or y%x != 0:
            x = random.randint(4000,10000)
            y = random.randint(5000,20000)
        placement = random.randint(1,3)
        if placement == 1:           
            print("What is {} - {}?".format(y,x))
            answer = y-x 
        elif placement == 2:
            print("____ + {} = {}".format(x,x+y))
            answer = y
        elif placement == 3:
            print("{} + ____ = {}".format(y,x+y))
            answer = x
    valid = True

#**************************************************************************************************

def experimental():
    global y
    global x
    global answer
    global valid
    y = 0
    x = 1
    while (y < x):
        x = random.randint(1,5000)
        y = random.randint(1,5000)
    operator = random.randint(1,2)

    #if len(str(x)) == 1:
    #    digitx = 2
    #if len(str(x)) == 2:
    #    digitx = 1
    #if len(str(x)) == 3:
    #    digitx = 0
    #if len(str(y)) == 1:
    #    digity = 2
    #if len(str(y)) == 2:
    #    digity = 1
    #if len(str(y)) == 3:
    #    digity = 0
    digitx = 4-len(str(x))
    digity = 4-len(str(y))


    if operator == 1:
        print("   "+" "*digity+str(y))
        print("  +"+" "*digitx+str(x))
        print("="*10)
        answer = x+y
    elif operator == 2:
        print("   "+" "*digity+str(y))
        print("  -"+" "*digitx+str(x))
        print("="*10)
        answer = y-x
    elif operator == 3:
        x=random.randint(2,9)
        y=random.randint(300,999)
        print("   "+str(y))
        print("  x  "+str(x))
        print("="*10)
        answer = x * y
    elif operator == 4:
        while y%x != 0:
            x=random.randint(2,9)
            y=random.randint(300,999)
        print("   "+str(y))
        print("  ÷  "+str(x))
        print("="*10)
        answer = y / x
    valid = True

#**************************************************************************************************

def fractions():
    global y
    global x
    global answer
    global valid
    y = 0
    x = 1
    while (y < x) or y%x != 0:
        x = random.randint(3,19)
        y = random.randint(300,1700)
    operator = random.randint(1,4)
    if operator == 1:
        print("What is {} * {}?".format(y,x))
        answer = y*x
    elif operator == 2:
        print("What is {} / {}?".format(y,x))
        answer = y/x
        return answer
    elif operator == 3:
        x = 1
        y = 0
        while (y < x) or y%x != 0:
            x = random.randint(4000,10000)
            y = random.randint(5000,30000)
        print("What is {} + {}?".format(y,x))
        answer = y+x
    elif operator == 4:
        x = 1
        y = 0
        while (y < x) or y%x != 0:
            x = random.randint(4000,10000)
            y = random.randint(5000,30000)
        print("What is {} - {}?".format(y,x))
        answer = y-x 
    valid = True

#**************************************************************************************************

# The outputs and inputs
flag = True
print("Welcome! In this game you will be given an equation to solve.")
print("You can keep going as long as you answer the questions correctly")
print("If you answer the questions wrong, the game will end")
while flag == True:
    streak = True
    counter = 0
    print("Choose a level \n\
    1.P1 \n\
    2.P2 \n\
    3.P3 \n\
    4.P4 \n\
    5.P5 \n\
    6.P6 \n\
    7.Quit \n\
    8.Experimental")
          
    level = input("Select your level: ")

    print("*"*99)

    if level == "1" or level == "P1" or level == "p1":
        grade = "P1"
        while streak:
            P1()
            valid = True
            while valid:
                reply = (input("Answer: ")) #Reply validation checks
                if reply.isdigit(): #Ensures that only numbers are entered
                    reply = int(reply)
                    valid = not valid
                else:
                    print("Please enter numbers only")

            if int(reply) == answer:
                print("Correct!")
                counter += 1
            else:

                print("Too bad! The correct answer is {}".format(answer))
                print("Your final score is {}".format(counter))
                print("*"*99)
                name = input("Enter your name: ")
                with open ('scoresP1.text' , 'a') as f:
                    f.write(name + " : " + str(counter) + " points. " + "Level: " + str(grade))
                    f.write("\n")
                    f.close()
                with open ('scoresP1.text') as w:
                    print("Scores:")
##                    for i in range(10):
                    line = w.read()
                    print(line)
                streak = not streak
        
        
    elif level == "2" or level == "P2" or level == "p2":
        grade = "P2"
        while streak:
            P2()
            valid = True
            while valid:
                reply = (input("Answer: "))
                if reply.isdigit():
                    reply = int(reply)
                    valid = not valid
                else:
                    print("Please enter numbers only")

            if reply == answer:
                print("Correct!")
                counter += 1
            else:
                print("Too bad! The correct answer is {}".format(answer))
                print("Your final score is {}".format(counter))
                print("*"*99)
                name = input("Enter your name: ")
                with open ('scoresP2.text' , 'a') as f:
                    f.write(name + " : " + str(counter) + " points. " + "Level: " + str(grade))
                    f.write("\n")
                    f.close()
                with open ('scoresP2.text') as w:
                    print("Scores:")
                    line = w.read()
                    print(line)
                streak = not streak        

    elif level == "3" or level == "P3" or level == "p3":
        grade = "P3"
        while streak:
            P3()
            valid = True
            while valid:
                reply = (input("Answer: "))
                if reply.isdigit():
                    reply = int(reply)
                    valid = not valid
                else:
                    print("Please enter numbers only")

            if reply == answer:
                print("Correct!")
                counter += 1
            else:
                print("Too bad! The correct answer is {}".format(answer))
                print("Your final score is {}".format(counter))
                print("*"*99)
                name = input("Enter your name: ")
                with open ('scoresP3.text' , 'a') as f:
                    f.write(name + " : " + str(counter) + " points. " + "Level: " + str(grade))
                    f.write("\n")
                    f.close()
                with open ('scoresP3.text') as w:
                    print("Scores:")
                    line = w.read()
                    print(line)
                streak = not streak 

    elif level == "4" or level == "P4" or level == "p4":
        grade = "P4"
        while streak:
            P4()
            valid = True
            while valid:
                reply = (input("Answer: "))
                if reply.isdigit():
                    reply = int(reply)
                    valid = not valid
                else:
                    print("Please enter numbers only")

            if reply == answer:
                print("Correct!")
                counter += 1
            else:
                print("Too bad! The correct answer is {}".format(answer))
                print("Your final score is {}".format(counter))
                print("*"*99)
                name = input("Enter your name: ")
                #store the scores, name and grade in the text file
                with open ('scoresP4.text' , 'a') as f:
                    f.write(name + " : " + str(counter) + " points. " + "Level: " + str(grade))
                    f.write("\n")
                    f.close()
                with open ('scoresP4.text') as w:
                    print("Scores:")
##                    for i in range(10):
                    line = w.read()
                    print(line)
                streak = not streak 

    elif level == "5" or level == "P5" or level == "p5":
        grade = "P5"
        while streak:
            P5()
            valid = True
            while valid:
                reply = (input("Answer: "))
                if reply.isdigit():
                    reply = int(reply)
                    valid = not valid
                else:
                    print("Please enter numbers only")

            if reply == answer:
                print("Correct!")
                counter += 1
            else:
                print("Too bad! The correct answer is {}".format(answer))
                print("Your final score is {}".format(counter))
                print("*"*99)
                name = input("Enter your name: ")
                #store the scores, name and grade in the text file
                with open ('scoresP5.text' , 'a') as f:
                    f.write(name + " : " + str(counter) + " points. " + "Level: " + str(grade))
                    f.write("\n")
                    f.close()
                with open ('scoresP5.text') as w:
                    print("Scores:")
##                    for i in range(10):
                    line = w.read()
                    print(line)
                streak = not streak 

    elif level == "6" or level == "P6" or level == "p6":
        grade = "P6"
        while streak:
            P6()
            valid = True
            while valid:
                reply = (input("Answer: "))
                if reply.isdigit():
                    reply = int(reply)
                    valid = not valid
                else:
                    print("Please enter numbers only")

            if reply == answer:
                print("Correct!")
                counter += 1
            else:
                print("Too bad! The correct answer is {}".format(answer))
                print("Your final score is {}".format(counter))
                print("*"*99)
                name = input("Enter your name: ")
                #store the scores, name and grade in the text file
                with open ('scoresP6.text' , 'a') as f:
                    f.write(name + " : " + str(counter) + " points. " + "Level: " + str(grade))
                    f.write("\n")
                    f.close()
                with open ('scoresP6.text') as w:
                    print("Scores:")
##                    for i in range(10):
                    line = w.read()
                    print(line)
                streak = not streak
##
    elif level == "7" or level == "Quit" or level == "quit":
       flag = False

    elif level == "8":
        grade = "ex"
        while streak:
            experimental()
            valid = True
            while valid:
                reply = (input("Answer: ")) #Reply validation checks
                if reply.isdigit(): #Ensures that only numbers are entered
                    reply = int(reply)
                    valid = not valid
                else:
                    print("Please enter numbers only")

            if int(reply) == answer:
                print("Correct!")
                counter += 1
            else:
                print("Too bad! The correct answer is {}".format(answer))
                print("Your final score is {}".format(counter))
                print("*"*99)
                name = input("Enter your name: ")
                with open ('scores_ex.text' , 'a') as f:
                    f.write(name + " : " + str(counter) + " points. " + "Level: " + str(grade))
                    f.write("\n")
                    f.close()
                with open ('scores_ex.text') as w:
                    print("Scores:")
##                    for i in range(10):
                    line = w.read()
                    print(line)
                streak = not streak


##with open ('scores.text') as w:
##    print("Scores:")
##    for i in range(10):
##        line = w.readline()
##        print(line)

