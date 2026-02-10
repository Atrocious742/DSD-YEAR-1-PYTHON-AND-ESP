#dict of appointments
people = {
    "P001": {
        "first_name": "Alice",
        "last_name": "Johnson",
        "email": "alice.johnson@example.com",
        "phone": "+1-555-123-4567",
        "role": "customer",
        "bookings": ["B1001", "B1003"]
    },
    "P002": {
        "first_name": "Mark",
        "last_name": "Chen",
        "email": "mark.chen@example.com",
        "phone": "+1-555-987-6543",
        "role": "customer",
        "bookings": []
    },
    "P003": {
        "first_name": "Sofia",
        "last_name": "Rossi",
        "email": "sofia.rossi@example.com",
        "phone": "+39-333-456-7890",
        "role": "staff",
        "bookings": ["B1002"]
    }
}



#booking system for the prototype
def book_appointment():
    print("1. Book an appointment")
    print("2. find an appointment")
    print("3. cancel an appointment")
    print("4. exit")
    #choice for what the user wants to do
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        date = input("Enter the date of the appointment (YYYY-MM-DD): ")
        time = input("Enter the time of the appointment (HH:MM): ")
        email = input("Enter your email: ")
        phone = input("Enter your phone number: ")
        role = input("Enter your role (customer/staff): ")
        number_of_bookings = int(input("Enter the number of bookings: "))
        print(f"Appointment booked for {name} {last_name} on {date} at {time} and other details consist of email: {email}, phone: {phone}, role: {role}, number of bookings: {number_of_bookings}.")
        book_appointment()
    elif choice == "2":
        name = input("Enter your first name: ")
        print(f"Finding appointment for {name}...")
        
        appointment = next(
    (appt for appt in people.values()
     if appt["first_name"] == name),
    None
    )
        print(appointment)
    elif choice == "3":
        name = input("Enter your name: ")
        print(f"Cancelling appointment for {name}...")
    elif choice == "4":
        print("Exiting the booking system.")
    else:
        print("Invalid choice. Please try again.")
#run the booking system
if __name__ == "__main__":
    book_appointment()

book_appointment()