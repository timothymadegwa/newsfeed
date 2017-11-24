import sys, os



# Main definition - constants

menu_actions  = {}



# =======================

#     MENUS FUNCTIONS

# =======================



# Main menu

def main_menu():

    os.system('clear')



    print ("WELCOME TO NEWS FEED,\n")

    print ("Choose what you want to do:")

    print ("1. VIEW POST")

    print ("2. CREATE POST")

    print ("3. COMMENT ON POST")

    print ("\n0. Quit")

    choice = input(" >>  ")

    exec_menu(choice)



    return



# Execute menu

def exec_menu(choice):

    os.system('clear')

    ch = choice.lower()

    if ch == '':

        menu_actions['main_menu']()

    else:

        try:

            menu_actions[ch]()

        except KeyError:

            print ("Invalid selection, please try again.\n")

            menu_actions['main_menu']()

    return



# Menu 1

def menu1():

    print ("VIEW !\n")

    print ("9. Back")

    print ("0. Quit")

    choice = input(" >>  ")

    exec_menu(choice)

    return





# Menu 2

def menu2():

    print ("CREATE !\n")

    print ("9. Back")

    print ("0. Quit")

    choice = input(" >>  ")

    exec_menu(choice)

    return



def menu3():

    print ("COMMENT !\n")

    print ("9. Back")

    print ("0. Quit")

    choice = input(" >>  ")

    exec_menu(choice)

    return





# Back to main menu

def back():

    menu_actions['main_menu']()



# Exit program

def exit():

    sys.exit()



# =======================

#    MENUS DEFINITIONS

# =======================



# Menu definition

menu_actions = {

    'main_menu': main_menu,

    '1': menu1,

    '2': menu2,

    '3': menu3,

    '9': back,

    '0': exit,

}



# =======================

#      MAIN PROGRAM

# =======================



# Main Program

if __name__ == "__main__":

    # Launch main menu

    main_menu()