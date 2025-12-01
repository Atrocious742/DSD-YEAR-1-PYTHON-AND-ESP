print('PLAYER 1')
num1 = input("What is your score: ")
name1 = input("Name: ")

with open("score.txt", "w") as f:
    data = {"username": name1, "score": num1}
    f.write(str(data) + "\n")
    f.write(str(name1)+ "\n")