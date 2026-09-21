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