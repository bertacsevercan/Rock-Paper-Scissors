
from random import choice

user_name = input("Enter your name: ")
txt_file = open("rating.txt")
print("Hello,", user_name)
rating = 0
for line in txt_file.readlines():
    line_ = line.split()
    if user_name in line_:
        rating = int(line_[1])
option_ = input().split(",")
print("Okay, let'S start")
while True:
    if option_[0] == "":
        user = input()
        option = ["rock", "paper", "scissors"]
        user_wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
        com = choice(option)
        if user == "!exit":
            print("Bye!")
            break

        elif user == "!rating":
            print("Your rating:", rating)

        elif user not in option and user != "!rating":
            print("Invalid input")

        elif user_wins[user] == com:
            rating += 100
            print(f"Well done. Computer chose {com} and failed")

        elif user == com:
            rating += 50
            print(f"There is a draw ({com})")

        elif user_wins[user] != com:
            print(f"Sorry, but computer chose {com}")
    else:
            a_list = []
            user = input()
            com = choice(option_)
            try:
                a_list.extend(option_[option_.index(user)+1:])
                a_list.extend(option_[:option_.index(user)])
                left_com_win = a_list[:len(a_list)//2]
                right_com_lose = a_list[len(a_list)//2:]
            except(ValueError):
                pass

            if user == "!rating":
                print("Your rating:", rating)
            elif user == "!exit":
                print("Bye!")
                break

            elif user not in option_:
                print("Invalid input")

            else:
                if com in right_com_lose:
                    rating += 100
                    print(f"Well done. Computer chose {com} and failed")

                elif user == com:
                    rating += 50
                    print(f"There is a draw ({com})")

                elif com in left_com_win:
                    print(f"Sorry, but computer chose {com}")




txt_file.close()
