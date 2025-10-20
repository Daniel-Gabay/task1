





# temp = int(input("enter the temp in your room: "))
# if temp > 28:
#     print("your room is hot! 22")

# elif temp <= 21:

#     print("your room is cold! 23")
# else: 
#     print("your room is ok! ")



A = 90 
B = 80 
C = 70 
D = 60 
E = 40
F = 0 


grade = float(input("grade (0-100): "))

if not 0 <= grade <= 100:
    print("out of range")

elif grade >= 90:
    print("B")

elif grade >= 80:
    print("C")

elif grade >= 70:
    print("D")

elif grade >= 60:
    print("E")

else:
    print("F")