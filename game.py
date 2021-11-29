import random


empty=" "
wel="                                        \33[1m WELCOME  IN ROCK//PAPER//SCISSOR  GAME"
print(empty)
sel ="                     select your choice  :  ROCK    /    PAPER     /SCISSOR   "
print(wel)
print(sel)
name=input("enter player name  :")
print(empty)

draw = 0
you_win = 0
computer_win = 0
while True:

    y = input("select your choice     :").lower()
    print(empty)
    c = random.choice(["rock", "paper", "scissor"])

    print(name, "   :", y)
    print("computer   :", c)

    if y == c:
        print("       ############   draw  ############")
        draw=draw + 1
    elif y == "rock" and c == "scissor":
        print("       ############   you win  ############")
        you_win=you_win + 1
    elif y == "paper" and c == "rock":
        print("       ############   you win  ############")
        you_win = you_win + 1

    elif y == "scissor" and c == "paper":
        print("       ############   you win  ############")
        you_win = you_win + 1
    else:
        print("       ############   computer win  ############")
        computer_win= computer_win + 1
    again = input("want to play game [ y / n ] :")
    if again=="y":
        print("#"*100)

    else:
        print("total draw        :",draw)
        print("you win           :",you_win, " round")
        print("computer win      :",computer_win," round")
        print(empty)
        if computer_win==you_win:
            print("                               final result is draw")
        if  computer_win > you_win:
            print("                               computer win the game")
        if computer_win < you_win:
            print("                      " , name," win the game")
        print(empty)
        print("                                     ### ### ### THANK YOU ### ### ###   ")
        print(empty)
        print("#"*100)
        break