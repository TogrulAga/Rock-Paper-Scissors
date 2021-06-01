from random import choice


class RPS:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.computer_choice = None
        self.user_choice = None
        self.user_name = ""
        self.user_rating = 0
        self.losers = None
        self.winners = None
        self.greet()
        self.read_user_rating()
        self.get_choices()
        self.play()

    def greet(self):
        self.user_name = input("Enter your name: ")
        print(f"Hello, {self.user_name}")

    def read_user_rating(self):
        with open("rating.txt") as ratings:
            for line in ratings:
                if self.user_name == line.split()[0]:
                    self.user_rating = int(line.split()[1])
                    return

    def get_choices(self):
        choices = input()
        self.choices = choices.split(sep=',') if choices != "" else self.choices
        print("Okay, let's start")

    def losers_winners(self):
        index = self.choices.index(self.user_choice) - len(self.choices) // 2
        self.losers = (self.choices[index:] + self.choices[:index])[0:len(self.choices) // 2]
        self.winners = (self.choices[index:] + self.choices[:index])[len(self.choices) // 2 + 1:]

    def play(self):
        while True:
            self.get_input()
            if self.user_choice == "!exit":
                return
            self.losers_winners()
            self.computer_play()
            self.show_result()

    def get_input(self):
        while True:
            self.user_choice = input()
            if self.user_choice in self.choices:
                break
            elif self.user_choice == "!exit":
                print("Bye!")
                break
            elif self.user_choice == "!rating":
                print(f"Your rating: {self.user_rating}")
            else:
                print("Invalid input")
                continue

    def computer_play(self):
        self.computer_choice = choice(self.choices)

    def show_result(self):
        if self.computer_choice == self.user_choice:
            print(f"There is a draw ({self.computer_choice})")
            self.user_rating += 50
        elif self.computer_choice in self.winners:
            print(f"Sorry, but the computer chose {self.computer_choice}")
        elif self.computer_choice in self.losers:
            print(f"Well done. The computer chose {self.computer_choice} and failed")
            self.user_rating += 100


rps = RPS()
