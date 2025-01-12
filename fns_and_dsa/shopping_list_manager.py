def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip() # Remove leading/trailing whitespace

        if choice == "1":
            # Prompt for and add an item
            input_item = input("Enter the item: ").strip()
            shopping_list.append(input_item)
            pass
        elif choice == "2":
            # Prompt for and remove an item
            input_item = input("Enter the item: ").strip().lower()  
            if input_item in shopping_list:
                shopping_list.remove(input_item)
            else:
                print("Item not found")
            pass
        elif choice == "3":
            # Display the shopping list
            print("\nShopping List:")
            for item in shopping_list:
                print(item)
            print()
            pass
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
