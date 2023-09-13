#deel1 input format
# age_str = input('What is your age? ')
# print(f'Your age is {age_str}')


#deel 2 #connection if else statements
# print("Which type of connection do you want to use?[4G, 5G, Wifi open]:")

# thisdict = {
#   "4g": False,
#   "5g": False,
#   "wifi open": False
# }
# connection_str = input('What connection do you use? ')

# if (connection_str.lower() not in thisdict):
#     print("invalid option, there will be no connection made.")
# else:
#     thisdict[connection_str] = True
#     print(thisdict)
#     if(thisdict["wifi open"] is True):
#         print("You have chosen for the 'Wifi open' option , we would like to point out that the owner of this connection can read the data from this connection.")
#         is_checked = ("Do you still want to make use of this connection?[Yes/No]:")
#         if(is_checked.lower() == "yes"):
#             is_checked = True
#         if(is_checked):
#             print('You have chosen for "wifi open"')
#             print(f"U bent verbonden via {connection_str}")
#         else:
#             print("You are not connect!")
#     else:
#         print(f"U bent verbonden via {connection_str}")

#deel 3 patient TB conclusions
# print('Patient exposed to TB')
# first_question = input("Is the patient an adult or a child? [Adult/Child]")
# question_result_child = False
# question_result_adult = False

# if (first_question.lower() == "child"):
#     question_result_child = True

# if (first_question.lower() == "adult"):
#     question_result_adult = True

# if (question_result_child == False and question_result_adult == True):
#     if(question_result_adult == True):
#         adult_question_1 = input("Has common TB symtoms?[Yes/No]")
#         if(adult_question_1.lower() == "yes"):
#             print('Treat as likely TB patient and perform full TB exam.')
#         elif(adult_question_1.lower() == "no"):
#             print('Have patient report back if unwell, return in 1 month for checkup')
#         else:
#             print("Abort, Unknow input")
# elif (question_result_child == True and question_result_adult == False):
#     if(question_result_child == True):
#         child_question_1 = input('Can TB test be given?[Yes/No]')
#         if(child_question_1.lower()== 'yes'):
#             print("Administer TB test.")
#             print("Assess TB test results and child's condition.")
#         elif(child_question_1.lower() =='no'):
#             child_question_2 = input('Child well? [Yes/No]')
#             if(child_question_2.lower() == 'yes'):
#                 print('6 months preventive isoniazid.')
#                 print('Have parent bring in if child shows any symptoms.')
#             else:
#                 print('take full history examine for TB, if Tb likely diagnosis, treat for TB, if other diagnosis more likely, treat as needed and watch for TB symptoms.')
#         else: 
#             print("Abort, unknown input.")
# else:
#     print("Abort, unknown input.")
    
#deel 4 flowchart shopping cart
# print('Shopping cart')
# print('Would you like to pay online or offline?')
# payment_method = input('Please choose [Offline/Online]')

# question_result_online = False
# question_result_offline = False

# if (payment_method.lower() == "online"):
#     question_result_online = True
#     print('Online, place purchase order.')

# elif (payment_method.lower() == "offline"):
#     question_result_offline = True
#     print('Offline, place purchase order.')

# else:
#     print('Abort, unknown input.')
#     exit(1)
    
# admin_check = input('Admin User? [Yes/No]')

# if (admin_check.lower() == "yes"):
#     admin_check = True
# elif (admin_check.lower() == "no"):
#     admin_check = False
#     rule_check = input('Approvel rules? [Approved/Rejected]')
# else:
#     print('Abort, unknown input.')
#     exit(1)

# #online
# if (question_result_online == True and admin_check == True):
#     details = ""
#     rule_check = "approved"
#     while (details == ""):
#         details = input('Enter payment details.')
#         if (details == ""): #zorgt ervoor dat hij niet verder gaat als er geen input is
#             details = str('geen input')
#             exit(1)
#         print('Place order.')
# if (question_result_online == True and admin_check == False and rule_check.lower() == "approved"):
#     details = ""
#     while (details == ""):
#         details = input('Enter payment details.')
#         if (details == ""): #zorgt ervoor dat hij niet verder gaat als er geen input is
#             details = str('geen input')
#             exit(1)
#         print('Place order.')
# if(question_result_online == True and admin_check == False and rule_check.lower() == "rejected"):
#     print('Purchase order rejected.')
    
# #offline
# if (question_result_offline == True and admin_check == True):
#     rule_check = "approved"
#     print('Order created automatically.')

# if (rule_check.lower() != "approved" and rule_check.lower() != "rejected"):
#     print('Abort, unknown input.')

# if (question_result_offline == True and admin_check == False and rule_check.lower() == "approved"):
#     print('Order created automatically.')
# if (question_result_offline == True and admin_check == False and rule_check.lower() == "rejected"):
#     print('Purchase order rejected.')
    
# deel 5 flowchart met lijst bestellen

def capitalize_list(list):
    '''Capitalizes all strings in a list'''
    for i in range(len(list)):
        list[i] = list[i].capitalize()
    text = " ".join(list)
    return text
''' '''

    
burger_choice = "Hamburger, Cheese burger, Big Mac, Quarter Pounder"
warm_drink_choice = "Coffee, Cappucino, Hot Chocolate"
cold_drink_choice = "Coco Cola, Cola Zero, 7-Up, Fanta, Fristi"


print("Welcome to Mac Donald's")

# here_there
here_there = input ("Would you like to eat here or take away? [Eat here/Take away]")
if(here_there.lower() == "eat here"):
    here_there = True
    
    
elif(here_there.lower() == "take away"):
    here_there = False
    
else:
    print("Abort, unknown input.")
    exit(1)

# burgers_drinks
burgers_drinks = input("Burger or a drink? [Burger/Drink]")
if(burgers_drinks.lower() == "burger"):
    burgers_drinks = True
    if(burgers_drinks):
        burgerchoice = input("Burger choice: [Hamburger, Cheese burger, Big Mac, Quarter Pounder]:")
        print(capitalize_list(burgerchoice.split(" ")))
        print(burger_choice.split(", "))
        if(capitalize_list(burgerchoice.split(" ")) in burger_choice.split(", ")):
            print(burgerchoice.split(" ").capitalize())
            if(burgerchoice == "Quarter Pounder"):
                add_cheese = input("Would you like to add cheese? [Yes/No]:")
                if(add_cheese.lower() == "yes"):
                    add_cheese = True
                    if(add_cheese):
                        print("Cheese added to Quarter Pounder.")
                elif(add_cheese.lower() == "no"):
                    add_cheese = False
                    if(add_cheese == False):
                        print("No cheese added to Quarter Pounder.")
    
elif(burgers_drinks.lower() == "drink"):
    burgers_drinks = False
    if(burgers_drinks == False):
        warm_cold = input("Warm or cold drink? [Warm/Cold]")
        if(warm_cold.lower() == "warm"):
            warm_cold = True
            if(warm_cold):
                warmdrinkchoice = input("Warm drink: [Coffee, Cappucino, Hot Chocolate]:")
                if(warmdrinkchoice.split(" ").capitalize() in warm_drink_choice):
                    print(warmdrinkchoice.capitalize())
                else:
                    print("Abort, unknown input.")
        elif(warm_cold.lower() == "cold"):
            warm_cold = False
            if(warm_cold == False):
                colddrinkchoice = input("Cold drink: [Coco Cola, Cola Zero, 7-Up, Fanta, Fristi]:")
                if colddrinkchoice.split(" ").capitalize() in cold_drink_choice:
                    print(colddrinkchoice.capitalize())
            else:
                print("Abort, unknown input.")
        
        else:
            print("Abort, unknown input.")
            exit(1)
            
else:
    print("Abort, unknown input.")
    exit(1)
    
