# Developer: Wellington
# Data: 18/09/2021
# Description: Scrip developed to simulate a calculator by using methods and functions
# it's a part of course Python Fundamentos at DSA


# Create a calculator method
def operations(parameter):

    # Here we have some simple function which will doing the math operations
    def addtion(n1, n2):
        return n1+n2

    def subtraction(n1, n2):
        return n1-n2

    def multiplication(n1, n2):
        return n1*n2

    def division(n1, n2):
        return n1/n2

    # Create a serie of condition that will access the math optons
    if parameter == 1:
        print('\n')
        print('----------You chose the addtion operation-------')
        print('\n')

        n1 = int(input("Informe the first number: "))
        n2 = int(input("Informe the second number: "))
        #addtion = lambda n1,n2: n1 + n2

        #Call the function math which was create above
        addtion = addtion(n1,n2)
        print('\n')
        print('The addtion will be %s'%(addtion))

    elif parameter == 2:
        print('\n')
        print('----------You chose the subtraction operation-------')
        print('\n')

        n1 = int(input("Informe the first number: "))
        n2 = int(input("Informe the second number: "))
        #subtraction = lambda n1,n2: n1 + n2
        subtraction = subtraction(n1,n2)
        print('The subtraction will be %s'%(subtraction))
        print('\n')
    elif parameter == 3:
        print('\n')
        print('----------You chose the multiplication operation-------')
        print('\n')

        n1 = int(input("Informe the first number: "))
        n2 = int(input("Informe the second number: "))
        #multiplication = lambda n1,n2: n1 + n2
        multiplication = multiplication(n1,n2)
        print('\n')
        print('The multiplication will be %s'%(multiplication))
    elif parameter == 4:
        print('\n')
        print('----------You chose the division operation-------')
        print('\n')

        n1 = int(input("Informe the first number: "))
        n2 = int(input("Informe the second number: "))
        #division = lambda n1,n2: n1 + n2
        division = division(n1,n2)
        print('\n')
        print('The division will be %s'%(division))

        # Condition else create if the user did not type any of the options above
    else:
        print(' Option unvaliable. The program will be finish')

# Create a dictionary with key and value which means the operation that this program has.
collections_actions = {1:'addtion',
                       2:'subtraction',
                       3:'multiplication',
                       4:'division'}

# This loop will print the options on the screen
for i,j in collections_actions.items():
    print(str(i) +" - "+ str(j))

print('\n')

# Ask for the user to enter oque option which had described above.
ope = int(input("Inform by type one number to start the calculation: "))

# Call the method by passing the option chose for the user.
operations(ope)
