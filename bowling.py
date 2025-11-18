# lists of all things to buy 
food = {"chicken nuggets" : "£5.00" , "burger" : "£5.99", "hotdog" : "3.99"}
drinks = {"water" : "£0.00" , "coke" : "£2.99", "sprite" : "£2.99"}
sides = {"fench-fries" : "£1.99" , "beans" : "£2.99", "mushy peas" : "£0.99"}
sauces = ["ketchup" , "mayonase" , "barbercue"]
lanes = {"1" : "avalable" ,
        "2" : "avalable",
        "3" : "unavalable",
        "4" : "unavalible",
        "5" : "avalible",
        "6" : "unavalibe",
        "7" : "avalable" ,
        "8" : "avalable",
        "9" : "unavalable",
        "10" : "unavalible",
        "11" : "avalible",
        "12" : "unavalibe",}
mealdeal = food["chicken nuggets"] + drinks["coke"] + sides["fench-fries"] 
mealdealprice = "£5.00"

#menu of choices
def menu():
    print(".................")
    print("welcome to the menu")
    print(".................")
    print("what would you like to do today?")
    print(".................")
    print("1 for bowling lanes")
    print("2 for food")
    print("3 for bill of the whole experiance ")
    print("4 for checking out of a lane")
    print(".................")
    option = int(input("what option would you like to choose? "))
    userChoice(option)

def userChoice(option):
    #checking for correct option
    if option == 1:
        lane()
    elif option == 2:
        meal()
    elif option == 3:
        bill()
    elif option == 4:
        exitlane()
    else:
        print("incorrect number, try again")

def lane():
    print(".................")
    print("lanes that are avalable are: ")
    print(lanes)
    print(".................")
    bowl = int(input("what lane would you like: "))
    if bowl == 1 or 2 or 5 or 7 or 8 or 11:
        foods = input("the lane you want is avalable would you like any food with it")
        if foods == "yes":
            meal()
        elif foods == "no":
            print("returning to menu")
            menu()
        else:
            print("invalid input")

def meal():
    items = []

    print(".................")
    print("welcome to the meal menu")
    print(".................")
    print("our main corses consist of: ")
    print(food)
    order = input("what would you like to have as a main: ")
    if order == "chicken nuggets":
        print("we have a meal deal offer: ")
        print("chicken nuggets with fries and a coke")
        offer = input("would you like it")
        if offer == "yes":
            print("that will be")
            print(mealdealprice)
            print(".................")
            all = input("is that everything: ")
            if all == "yes":
                print("returning to main menu")
                menu()
            else:
                side()
        else:
            side()
    else:
        side()
    items

def side():
    print("what side do you want:")
    print(sides)
    print(".................")
    option = input("what side would you like")
    if option == sides["fench-fries"] or sides["beans"] or sides["mushy peas"]:               
        print("order accepted")
        print(".................")
        drink = input("would you like a drink with that? ")
        if drink == "yes":
            liquid(items)
        else:
            menu()
    else:
        print("order denied")
        print(".................")
        meal()

def liquid(items):
    print("what would you like to drink: ")
    print(drinks)
    if drinks == drinks["coke"] or drinks["sprite"] or drinks["water"]:
        print("order accepted")
        appe
    else:
        print("order denied")
    items.append(items)

def total(items):


menu()
                
        









liquid(items) #pass items list

def liquid(items):
    print("what would you like to drink: (Type no if you don't) ")
    print(drinks)
    if drinks == drinks["coke"] or drinks["sprite"] or drinks["water"]:
        print("order accepted")
        items.append(drinks)
    elif drinks.lower == "no":
        menu():

    else:
        print("not a vaild option")
        liquid(items)
    
def side(items):
    print("what would you like to drink: ")
    print(drinks)
    if drinks == sides["fench-fries"] or sides["beans"] or sides["mushy peas"]:
        print("order accepted")
        appe
    else:
        print("order denied")
    items.append(items)










    
    