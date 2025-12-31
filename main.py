import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score because your trash")
    else:
        print("The current high score is {} attempts" .format(min(attempts_list)))
    def start_game():
        random_number = int(random.randint(1, 10))  
        print("Hey Are you ready to enter the game of lucky gambling")
        player_name = input("what is username gonna be")
        wanna_play = input("Hi {} ready to gamble (Enter yes or NoOOOOOoooo0000)" format(player_name))
        attempts = 0
        show_score()
        while wanna_play.lower() == "yes":
            try:
                guess = int(input("Pick a numero between 1 and 10"))
                if int(guess) < 1 or int(guess) > 10:
                    raise ValueError("PIck a NuMeRo betWEEN 1 AND 10")
                if int(guess) == random_number:
                    print("-_-__-_- you won")
                    attempts += 1
                    attempts_list.append(attempts)
                    print(" I took you {} attempts" .format(attempts))
                    play_again = input("WOULD YOU LIKE to PLAY AGAIN <:(Enter yes/noooo im too scared)")
                    attempts = 0
                    show_score()
                    random_number = int(random.randint(1, 10))
                    if play_again.lower() == "noooo im too scared":
                        print("ha your too scared")
                        break
                elif int(guess) < random_number
                    print("its lower")
                    attempts += 1
                elif int(guess) > random_number
                    print("its higher")
                    attempts += 1
            except ValueError as err
            print("Oh tat is not valid") 
            print("({})" .format(err))
        else
            print("Thats cool have a nice day")    
            if__name__ == "__main__":
            start_game()

        
