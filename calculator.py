def calculator():  
    import math
    users_first_input = int(input("Enter first number: "))
    print("Square root of the first number is: ", math.sqrt(users_first_input))
    print("square of the first number is: ", math.pow(users_first_input, 2))
    print("Rounded first number is: ", round(users_first_input))
    area_of_circle = math.pi * (users_first_input ** 2)
    print("Area of a circle with the first number as the radius is: ", area_of_circle)
    main()

def dice_game():
    import random
    lives = 3
    while lives > 0:
        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        print("Random number between 1 and 6: ", num1)
        print("Random number between 1 and 6: ", num2)
        print("Sum of the two random numbers is: ", num1 + num2)
        num = num1 + num2
        if num >= 7 and num <= 11:
            print("You win!")
            break
        else:
            print("You lose!")
            lives -= 1
            print("Lives remaining: ", lives)
            if lives == 0:
                print("Game over!")
    main()

def age_calculator():
    import datetime
    print("Today's date is: ", datetime.datetime.now().strftime("%d/%m/%Y"))
    dob = input("Enter your date of birth (dd/mm/yyyy): ")
    dob = datetime.datetime.strptime(dob, "%d/%m/%Y")
    days_till_next_birthday = (dob.replace(year=datetime.datetime.now().year) - datetime.datetime.now()).days
    if days_till_next_birthday < 0:
        days_till_next_birthday += 365
    print("Days until your next birthday: ", days_till_next_birthday + 1)
    age = datetime.datetime.now().year - dob.year
    if (datetime.datetime.now().month, datetime.datetime.now().day) < (dob.month, dob.day):
        age -= 1
    print("Your age is: ", age)
    main()
def shop_sales():
    weekly_shop_sales = [120, 135, 150, 98, 175, 200, 143]
    mean_sales = sum(weekly_shop_sales) / len(weekly_shop_sales)
    print("Mean sales for the week: ", mean_sales)
    total_sales = sum(weekly_shop_sales)
    print("Total sales for the week: ", total_sales)
    highest_sales = max(weekly_shop_sales)
    print("Highest sales for the week: ", highest_sales)
    lowest_sales = min(weekly_shop_sales)
    print("Lowest sales for the week: ", lowest_sales)
    main()

def lucky_dip():
    import random
    import numpy as np 
    import math
    import datetime
    random_number = random.randint(1, 100)
    numbers_array = np.array([random_number])
    rounded_number = math.ceil(random_number)
    print("Today's date is: ", datetime.datetime.now().strftime("%d/%m/%Y"))
    print("Your lucky number is: ", rounded_number)
    main()

def main():
    print("Welcome to the main menu!")
    print("1. Calculator")
    print("2. Dice Game")
    print("3. Age Calculator")
    print("4. Shop Sales")
    print("5. lucky dip")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        calculator()
    elif choice == 2:
        dice_game()
    elif choice == 3:
        age_calculator()
    elif choice == 4:
        shop_sales()
    elif choice == 5:
        lucky_dip()
    elif choice == 6:
        print("Exiting the program. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")
        main()
main()