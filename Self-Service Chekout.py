
#Individual Lab
#Byte & Brew Self-Service Kiosk Requirments
#At frist I will list a grettings as "Welcome to Byte & Brew" then will lists items and their prices.
#Then I will creat a loop that will allow the user to select items and add them to their order until they choose to complete the order.
#when the user selects items, then the program will add the price of the selected item to the total bill and display the current total.
#in between if the user did not put the correct input, the program will display an eror massage and ask the user to choose the right option from the listed manue.
#The program will continue to loop until the user selects the option to complete the order.
#At last the program will ask if the user have any cupon or not, if the user have a cupon then the program will ask the user to enter the cupon code and will apply the discount to the total bill.
#if the user don't have a copon or enter an invalid cupon coade, the program will display an eror massage and will not apply any discount to the total bill.
#at last the program will display the final total and a thank you massage to the user for visiting Byte & Brew.


total_bill = 0.00

while True:
    print("Welcome to Byte & Brew!")
    print("1. Black Coffee - 2.50")
    print("2. Vanilla Latte - 4.00")
    print("3. Blueberry Muffin - 3.00")
    print("4. Complete Order (Checkout)")

    try:
        choice = int(input("Select an item (1-4): "))
    except ValueError:
        print("Invalid selection. Please choose a valid menu item.")
        continue

    if choice == 1:
        total_bill += 2.50
        print("Added Black Coffee. Current total: ${:.2f}".format(total_bill))
    elif choice == 2:
        total_bill += 4.00
        print("Added Vanilla Latte. Current total: ${:.2f}".format(total_bill))
    elif choice == 3:
        total_bill += 3.00
        print("Added Blueberry Muffin. Current total: ${:.2f}".format(total_bill))
    elif choice == 4:
        has_coupon = input("Do you have a coupon code? (yes/no): ").lower()
        if has_coupon == "yes":
            coupon_code = input("Please enter your coupon code: ")
            if coupon_code == "10":
                total_bill *= 0.90
                print("Coupon applied! 10% discount.")
            else:
                print("Invalid coupon code. No discount applied.")
        print("Complete Order. Final total: ${:.2f}".format(total_bill))
        print("Thank you for visiting Byte & Brew!")
        break
