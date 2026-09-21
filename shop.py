print ("Let's buy something")

def go_shopping():
    print()
    print("What do you want to buy?")
    print("1. Sword")
    print("2. Apple")
 
    choice = int(input("Choose what to buy (1/2): "))
 
    if choice == 1:
        print("you bought a sword!")
        return "Sword"
    elif choice == 2:
        print("you bought an apple!")
        return "Apple"
    else:
        print("You haven't chosen")

    def shop():
    print('Welcome to the shop')
    print('Decide what to buy!')

    choice = str(input('Hammer or apple? (1 or 2): '))

    if (choice == '1'):
        print('Now you can go back to forest and kill the dragon')
    if (choice == '2'):
        print('Turn back and forget the forest')

    print('end game')