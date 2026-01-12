import time

saved_cipher = ""
saved_shift = 0

def encrypt(plainText, shift):

    for ch in plainText:
        if ch.isdigit():
            print("Error: Numbers are not allowed in the input.")
            for i in range(5, 0, -1):
                time.sleep(1)
                return
    
    cipherText = ""
    for ch in plainText:
        if ch.isalpha():
            stayInAlphabet = ord(ch) + shift
            if ch.islower() and stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            if ch.isupper() and stayInAlphabet > ord('Z'):
                stayInAlphabet -= 26
            cipherText += chr(stayInAlphabet)
        else:
            cipherText += ch

    return cipherText

def decrypt(cipherText, shift):
    raw = ""
    for ch in cipherText:
        if ch.isalpha():
            stayInAlphabet = ord(ch) - shift
            if ch.islower() and stayInAlphabet < ord('a'):
                stayInAlphabet += 26
            if ch.isupper() and stayInAlphabet < ord('A'):
                stayInAlphabet += 26
            raw += chr(stayInAlphabet)
        else:
            raw += ch
    return raw

def caesarcipher():
    global saved_cipher
    global saved_shift

    print("main menu")
    print(".......................")
    print("1 encrypt a code")
    print("2 decrypt using password")
    option = int(input("what is your option: "))

    if option == 1:
        plainText = input("enter the message you want to encrypt: ")
        shift = int(input("set a password (shift number): "))
        cipherText = encrypt(plainText, shift)
        saved_cipher = cipherText
        saved_shift = shift
        print("Your ciphertext is:", cipherText)
        print("Your password is:", shift)
        time.sleep(2)
        caesarcipher()

    elif option == 2:
        if saved_cipher == "":
            print("No message stored. Encrypt something first.")
            time.sleep(2)
            caesarcipher()
        password = int(input("enter the password: "))
        if password == saved_shift:
            raw = decrypt(saved_cipher, password)
            print("Correct password.")
            print("Your decrypted message is:", raw)
        else:
            print("Incorrect password.")
        time.sleep(2)
        caesarcipher()

    else:
        print("invalid option, returning to menu in 5 seconds")
        time.sleep(5)
        caesarcipher()

caesarcipher()