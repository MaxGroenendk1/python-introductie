#deel1
# age_str = input('What is your age? ')
# print(f'Your age is {age_str}')


#deel 2
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

#deel3
print('Patient exposed to TB')
first_question = input("Is the patient an adult or a child? [Adult/Child]")
if (first_question.lower() == "child" | first_question.lower() == "adult"):
    if(first_question.lower() == "adult"):
        adult_question_1 = input("Has common TB symtoms?[Yes/No]")
        if(adult_question_1.lower() == "yes"):
            print('Treat as likely TB patient and perform full TB exam.')
        elif(adult_question_1.lower() == "no"):
            print('Have patient report back if unwell, return in 1 month for checkup')
        else:
            print("Abort, Unknow input")
    elif(first_question.lower() == "child"):
        child_question_1 = input('Can TB test be given?[Yes/No]')
        if(child_question_1.lower()== 'yes'):
            print("Administer TB test.")
            print("Assess TB test results and child's condition.")
        elif(child_question_1.lower() =='no'):
            child_question_2 = input('Child well? [Yes/No]')
            if(child_question_2.lower() == 'yes'):
                print('6 months preventive isoniazid.')
                print('Have parent bring in if child shows any symptoms.')
            else:
                print('take full history examine for TB, if Tb likely diagnosis, treat for TB, if other diagnosis more likely, treat as needed and watch for TB symptoms.')
        else: 
            print("Abort, unknown input.")
else:
    print("Abort, unknown input.")
    