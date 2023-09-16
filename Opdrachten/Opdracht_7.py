# #rekenmachine

# # This function adds two numbers
# def add(x, y):
#     return x + y

# # This function subtracts two numbers
# def subtract(x, y):
#     return x - y

# # This function multiplies two numbers
# def multiply(x, y):
#     return x * y

# # This function divides two numbers
# def divide(x, y):
#     return x / y

# x = float(input("give first number: "))
# y = float(input("give second number: "))
# operator = input("declare operator [+,-,*,/]: ")
# if(operator == "+"):
#     print(add(x, y))
# if(operator == "-"):
#     print(subtract(x, y))
# if(operator == "*"):
#     print(multiply(x, y))
# if(operator == "/"):
#     print(divide(x, y))
from students_classrooms import students_per_classroom # zo importeer je de dataset

def get_excellent_students(list_of_students):
    #als hij meer dan één uitmuntend heeft of als alle resultaten beter dan "voldoende" zijn.
    uitstekende_studenten = []
    for i in range (0,len(list_of_students)):
        student = list_of_students[i]
        aantal_goed = 0 
        aantal_uitmuntend = 0 #hoevaak voldoende
        for vak in student['resultaten']: # ittereert over de dict van key resultaten
            resultaat = student['resultaten'][vak]
            print(resultaat)
            if(resultaat == "goed"):
                aantal_goed += 1
            if(resultaat == "uitmuntend"):
                aantal_uitmuntend += 1
                
        if(aantal_uitmuntend >= 2 or aantal_goed == 4):
            uitstekende_studenten.append(student)
    return uitstekende_studenten
print(len(get_excellent_students(students_per_classroom["SWDVT-1A"])))
                
                
    
# def get_most_excellent_classroom(list_of_classrooms):
#     #Welke klas(sen) hebben het hoogste percentage "excellent" studenten?
#     len(students)#aantal studenten per klas
#     x = 0
#     while (x <= len(students)):#aantal studenten excellent.
#         x = x + 1

# def get_best_scoring_classroom(list_of_classrooms):
#     #Welke klas heeft gemiddeld genomen over alle vakken de hoogste scores? Dit is een lastige. Stel voor het gemak dat een onvoldoende = 0 punten, voldoende 2 punten, goed 3 punten en uitstekend 4 punten.

# def get_failed_students(list_of_students, minimum_score = 4):
#     #Gegeven diezelfde manier van scoren: studenten met een score van 3 of minder punten moeten een inhaal opdracht doen. Welke studenten zijn dat en wat zijn hun resultaten?