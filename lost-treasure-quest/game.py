def main():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself in a dark forest. You see a path to your left and a path to your right.")

    while True:
        print("\nWhat do you want to do?")
        print("1. Take the path to the left")
        print("2. Take the path to the right")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            print("You chose to take the path to the left. You encounter a wild animal!")
            print("Game over!")
            break
        elif choice == "2":
            print("You chose to take the path to the right. You find a treasure chest!")
            print("Congratulations, you win!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
