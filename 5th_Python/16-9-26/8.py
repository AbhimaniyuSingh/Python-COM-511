cart = []
while True:
    print("1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Exit")
    choice = input("Enter your choice :")
    if choice == 1:
        item = input("Enter item to add: ")
        cart.append(item)
        print(f"{item} added to cart.")
    elif choice == 2:
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
            
        else:
            print(f"{item} not found in cart.")
    elif choice == 3:
        print("Items in cart:", cart)
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")