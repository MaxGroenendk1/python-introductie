#deel 1
# for i in range(1,31):

#     if(i % 3 == 0 and i % 5 != 0):
#         print("Fizz")
#     if(i % 5 == 0 and i % 3 != 0):
#         print("Buzz")
#     if(i % 3 == 0 and i % 5 == 0):
#         print("FizzBuzz")
#     elif(i % 3 != 0 and i % 5 != 0): 
#         print (i)

#deel 2
numbers = list(range(1,100))
#getallen N, Z, Q, R
# N = natuurlijke getallen: Alle positieve gehele getallen en het getal nul
# Z = gehele getallen: Alle getallen, onder en boven en gelijk aan 0, zonder decimalen achter de komma
# Q = rationale getallen: Alle getallen met meerdere decimalen achter de komma (Q = quotient = deling)
# irrationele getallen = wortel 2 of pi (oneindig veel decimalen achter de komma)
#getallen die niet als breuk geschreven kunnen worden noemen we irrationele getallen
# R = reële getallen: Rationele en irrationele getallen
    
def div(n):
    divisors = [] #lijst aangemaakt waar alle delers in kunnen
    for i in range(1, n + 1): #startend bij 1, gegeven getal +1)
        if n % i == 0: #kenmerk van een deler, zoja?
            divisors.append(i) # plak achter lijst.
    return sorted(divisors) #sorteer alle gevonden delers.

def is_prime(n):
    divisors = div(n) # <-- alle delers van geheel getal
    # een priemgetal heeft altijd maar 2 delers! niet meer en niet minder daarom 1 geen priem getal
    # if n == 1: # 1 blijkbaar geen priem getal, omdat het slechts 1 deler heeft zichzelf. Het statement is niet; "1 en zichzelf, daarom 2 delers (1 en "x = zichzelf") dus een priemgetal"
    #     return False
    # i.p.v if len(divisors) > 2:
    #     return False
    if len(divisors) != 2:
        return False
    return True

for i in numbers:
    if (is_prime(i) == True):
        print(f'{i} is a prime number')
    else:
        print(f'{i} is not a prime number')

# #deel 3
# # We hebben de random module nodig om willekeurige getallen te genereren
# import random
# # Totaal aantal getallen op de kaart zal hoogte x breedte zijn
# bingo_number_total = 4 ** 2
# # Daarna maken we een lijst met 99 getallen waar we uit gaan kiezen
# numbers_all = list(range(1, 100))
# # We gooien alle ballen door elkaar
# random.shuffle(numbers_all)
# # ..en pakken de eerste 16 getallen
# bingo_numbers = numbers_all[:bingo_number_total]

# amount_to_be_scratched = 50
# scratch_numbers_to_pick = list(range(1, 100)) # moet het zelfde zijn als de eerste gezette hoeveelheid getallen bij "numbers_all"
# random.shuffle(scratch_numbers_to_pick)
# scratched_numbers = scratch_numbers_to_pick[:amount_to_be_scratched]
# print(scratched_numbers)

# for i in range (0,len(scratched_numbers)):
#     for n in range(0, len(bingo_numbers)):
#         if (scratched_numbers[i] == bingo_numbers[n]):
#             bingo_numbers[n] = 0
#             #indien er een check gedaan dient te worden hier. wie als eerste bingo heeft
#         else:
#             pass
# first_quarter = bingo_numbers[:4]
# second_quarter = bingo_numbers[4:8]
# third_quarter = bingo_numbers[8:12]
# last_quarter = bingo_numbers[12:16]
# print(f'{first_quarter}\n{second_quarter}\n{third_quarter}\n{last_quarter}')

# bingo = False
# #horizontaal bingocheck
# if(sum(first_quarter) == 0):
#     bingo = True
# if(sum(second_quarter) == 0):
#     bingo = True
# if(sum(third_quarter) == 0):
#     bingo = True
# if(sum(last_quarter) == 0):
#     bingo = True
    
# #verticaal
# for z in range (0, len(first_quarter)):
#     if(first_quarter[z] == 0):
#         if(second_quarter[z] == 0):
#             if(third_quarter[z] == 0):
#                 if(last_quarter[z] == 0):
#                     bingo = True
# if(bingo):
#     print ("Bingo")  

#deel 4
print("To stop the program press '.'")
user_input = ""
while (user_input != "."):
    user_input = input("Please enter a number up until 100, press '.' to stop the program: ")
    if(user_input == "."):
        print("program has stopped")
        exit(1)
    else:
        print(is_prime(user_input))