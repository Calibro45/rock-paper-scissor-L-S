# Write your code below this line 👇
import random
import banner


# Function for comparison the lizard Spock win/lose
def lizardSpock(value1, value2):
    if value1 == 3 and value2 == 4:
        return True
    if value1 == 3 and value2 == 0:
        return False
    if value1 == 3 and value2 == 2:
        return False
    if value1 == 4 and value2 == 1:
        return False
    if value1 == 4 and value2 == 3:
        return False


def rock_paper_scissor():
    print(banner.title)

    choices = [
        banner.rock,
        banner.paper,
        banner.scissors,
        banner.lizard,
        banner.spock
    ]
    user_choice = input(
        "What do you choose? Type 0 for Rock, 1 for paper, 2 for Scissors, 3 for Lizard or 4 for Spock.\n")

    # check the user input before game start
    if user_choice >= "0" and user_choice <= "4":

        # Transform integer
        user_number = int(user_choice)

        # Generate a random number for the pc
        computer_choice = random.randint(0, 4)

        print(f"You choose \n{choices[user_number]}")
        print(f"Computer Choose: \n{choices[computer_choice]}")

        if user_number == 0 and computer_choice == 2:
            print(banner.win)
        elif user_number == 0 and computer_choice == 1:
            print(banner.lose)
        elif user_number == 2 and computer_choice == 0:
            print(banner.lose)
        elif user_number > computer_choice:
            if lizardSpock(user_number, computer_choice) == True:
                print(banner.win)
            elif lizardSpock(user_number, computer_choice) == False:
                print(banner.lose)
            else:
                print(banner.win)
        elif computer_choice > user_number:
            if lizardSpock(computer_choice, user_number) == True:
                print(banner.lose)
            elif lizardSpock(computer_choice, user_number) == False:
                print(banner.win)
            else:
                print(banner.lose)
        elif user_number == computer_choice:
            print(banner.draw)

        play_again = input(
            "Do you want to play again? Type 'y' or 'n':"
        ).lower()
        if play_again == "y":
            rock_paper_scissor()
        else:
            print(banner.game_over)

    else:
        print(f"You type wrong input.\n {banner.game_over}")


rock_paper_scissor()