class Players:

    def players_names(self):
        playres_list = []
        no_of_players = int(input("enter the number of players: "))
        self.score = 0
        for i in range(0,no_of_players):
            name = input("enter player name:\n")
            playres_list.append(name)

    def play_1(self):
        chosen_player = random.choice(list_players)
        print(f"It's your turn {chosen_player}")
        choose = input(f"{chosen_player} choose TRUTH OR DARE")
        game(choose)
        done = input(f"does the player has done the {choose} yes or no ?: ")
        check_score(done)

    def game(self, choose):
        if choose == "TRUTH":
            task = random.choice(list_truths)
            print(task)
        elif choose == "DARE":
            task = random.choice(list_dares)
            print(task)
        else:
            print("entered wrong input")

    def check_score(self, done):
        if done == "yes":
            self.score += 1
            print(f"your score is {self.score} ")
        else:
            print(f"your score is {self.score} ")



play = Players()
play.players_names()