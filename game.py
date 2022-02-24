# Rock Paper Scissors
import random


class RPS:

    def __init__(self):
        self.player = ''
        self.computer = ''
        self.wins_against = {}
        self.default = {'rock': ['scissors'], 'paper': ['rock'], 'scissors': ['paper']}
        self.user_option = {}
        self.name = ''
        self.filename = 'rating.txt'
        self.file_content = {}
        self.score = 0

    def check_winner(self):
        if self.player == self.computer:
            print(f'There is a draw ({self.player})')
            self.score += 50
            # print(f'Current score: {self.score}')
        elif self.computer in self.wins_against.get(self.player):
            print(f"Well done. The computer chose {self.computer} and failed")
            self.score += 100
            # print(f'Current score: {self.score}')
        else:
            print(f"Sorry, but the computer chose {self.computer}")

    def play(self):
        while True:
            self.player = input()
            self.computer = random.choice(list(self.wins_against))
            if self.player == '!rating':
                print(f'Your rating: {self.score}')
            elif self.player == '!exit':
                print('Bye!')
                break
            elif self.player not in self.wins_against:
                print('Invalid input')
            else:
                self.check_winner()

    def update_user(self):
        self.name = input('Enter your name: ')
        print(f'Hello, {self.name}')
        # retrieve score from file if exists otherwise zero
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    user, points = line.split()
                    self.file_content[user] = int(points)
                    if user == self.name:
                        self.score = int(points)
                        # print(f'Starting score: {self.score}')
        except IOError:
            pass

    def game_option(self):
        option = input('Enter game choices (comma separated, no spaces) or press enter for default game: \n')
        # rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire
        if option == "":
            self.wins_against = self.default
        else:
            option = option.strip().split(',')  # need extra functionality to remove whitespaces.
            self.create_2(option)
        print("Okay, let's start")
        # print(self.wins_against)

    def create(self, option):
        for key in option:  # This did not work.
            count = int((len(option) - 1) / 2)  # num items that defeats you
            temp_1 = [x for x in option if option.index(x) < option.index(key)]
            temp_2 = [x for x in option if option.index(x) > option.index(key)]
            temp = temp_1 + temp_2
            values = temp[0:count]
            self.wins_against[key] = values  # assign key and values list to combo pairs
        return self.wins_against

    def create_2(self, option):
        # choice loses against count of items to the right
        # choice wins against count items to the left
        # Here function rotates to have key at index zero
        # At index zero it defeats the (n - 1)/2 elements at the end of the list
        for key in option:
            count = int((len(option) - 1) / 2)  # num items that defeats you
            idx = option.index(key)
            if idx == 0:
                temp = option[idx:]
            elif idx == len(option) - 1:
                temp = option[0:idx-1]
            else:
                temp = option[idx:] + option[0:idx]
            values = temp[-count:]
            self.wins_against[key] = values  # assign key and values list to combo pairs
        return self.wins_against


def main():
    my_game = RPS()
    my_game.update_user()
    my_game.game_option()
    my_game.play()


if __name__ == '__main__':
    main()
