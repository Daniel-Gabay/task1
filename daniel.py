
#שאלה 1

# num = int(input("Enter a Number "))
# if num > 0:
#     print("positive")
# elif num < 0:
#     print("negative")
# else:
#     print("zero")


#שאלה 2 
#לבקש ציון מהמשתמש 
# user_grade = int(input("Enter a grade (0-100) "))

# if user_grade <0 or user_grade > 100:
#     print("Invalid grade! Please enter a number between 0 and 100.")

# A = 93
# B = 83
# C = 76
# D = 66
# F = 60

# if user_grade >= A: 
#     print("A")

# elif user_grade >= B:
#     print("B")

# elif user_grade >= C:
#     print("C")

# elif user_grade >= D:
#     print("C")

# elif user_grade >= D:
#     print("D")

# else:
#     print("F")




#שאלה 3 
# לבקש גיל ולבדוק את המשתמש (ילד- מתבגר- או - מבוגר- )


# Age = float(input("Enter your Age: "))

# if Age < 0:
#     print("invalid age")

# elif Age < 12:
#     print("child")

# elif Age < 18:
#     print("teenager")

# else:
#     print("adult")



#שאלה 4 
#לבקש שני מספרים ולהדפיס את הגדול מבניהם 

# num1 = float(input("Enter a Number "))
# num2 = float(input("Enter a Number "))

# if num1 < num2:
#     print("num2 is bigger number")

# elif num1 == num2:
#     print("equal")

# else:
#     print("num1 is bigger number ")

    
#שאלה 5
#לכתוב תוכנית שבודקת האם המספר שווה או מוזר 

#לקבל מהממשתמש
# num = input("Enter a Number: ")

# # כאן בודקים אם הסוג הוא מספר 
# if type(int(num)) != int:
#     print("invalid value")

# sum = 0 
# for i in range(len(num)):

# # כאן בודקים אם הערך זוגי 
#     if i % 2 == 0:
#         sum += int(num[i])

#         print ("the sum of digits on even positions is: ", sum) 



#שאלה 6
#להדפיס אתכל המספרים בין (בין 1-10 )

# for i in range (1, 11):
#     print(i)




#שאלה 7
# להדפיס רק מספרים שלמים בין 1 -20    

# for daniel in  range(1, 21):
#     if daniel % 2 == 0:
#         print(daniel)




#שאלה 8 

#משתנה + קלט מהמשתמש 
# N = int(input("Enter N: "))  # שואלים את המשתמש מספר, והופכים אותו למספר שלם
# total = 0                    # הקופה ריקה (הסכום מתחיל ב-0)

# for i in range(1, N + 1):    # סופרים 1,2,3,...,N
#     total += i               # מוסיפים לקופה את המספר הנוכחי

# print(total)                 # מדפיסים את הסכום






#מחשבון
                                                ####### קלט: המספר הראשון ######
# num1 = float(input("Enter the first number: "))
                                                ######  קלט: סימן פעולה (+ - * /): ######
# operator = input("Enter an operator (+ - * /): ")
                                                ######קלט: המספר השני ######                            
# num2 = float(input("Enter the second number: "))
                                                ###### חיבור #####
# if  operator == "+":
#     print (int(num1 + num2))
                                                ###### חיסור #####
# elif operator == "-":
#      print (int(num1 - num2))
                                                ###### כפל #####
# elif operator == "*":
#      print (int(num1 * num2))
                                                ######חילוק:(בדיקה נגד חלוקה באפס #####)
# elif operator == "/":
#     if num2 != 0:
#          print (int(num1 / num2))
                                                ####### אופרטור לא מוכר #####
# else:
#    print ("Error! Division by zero")









# import math     

# radius = float(input("Enter the radius of the circle: "))

# circumference = 2 * math.pi * radius
# print (f"The circumference of the circle is:  {round (circumference, 2)}cm")
