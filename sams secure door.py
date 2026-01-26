CORRECT_RFID = "123456"
CORRECT_PIN = "7890"

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    rfid = input("Enter RFID card ID: ")
    pin = input("Enter PIN: ")

    if rfid == CORRECT_RFID and pin == CORRECT_PIN:
        print("Access granted")
        break
    else:
        attempts += 1

        if attempts == 1:
            print("Try again")
        elif attempts == 2:
            print("1 more attempt")
        else:
            print("ALARM! Security has been notified.")
