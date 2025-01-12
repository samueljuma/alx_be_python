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

        try:
            choice = int(input("Enter your choice: ").strip())  # Attempt to convert input to an integer
        except ValueError:
            print("\nInvalid input. Only numbers are valid.\n")
            continue  # Restart the loop

        if choice == 1:
          input_item = input("Enter the item: ").strip().lower()  
          if input_item in shopping_list:
              print(f'\n"{input_item}" is already in the shopping list.\n')
          else:
              shopping_list.append(input_item)
              print(f'\n"{input_item}" added to the shopping list.\n')
        elif choice == 2:
            # Prompt for and remove an item
            input_item = input("Enter the item: ").strip().lower()
            if input_item in shopping_list:
                shopping_list.remove(input_item)
                print(f'\n"{input_item}" removed from the shopping list.\n')
            else:
                print("\nItem not found in the shopping list.\n")
        elif choice == 3:
            # Display the shopping list
            if shopping_list:
                print("\nShopping List:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("\nThe shopping list is empty.")
            print()
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.\n")


if __name__ == "__main__":
    main()
