from random import randint
from tile import *
from wall import *
from players import Player
from referee import *


class Game:
    def __init__(self):
        self.pc = Player()
        self.cpu = [Player(), Player(), Player()]
        self.set_east()
        self.first_dealer = self.east_num
        self.players = self.cpu + [self.pc]
        self.wall = Wall()
        self.current_discard = ''
        self.referee = Referee()
        self.p_wind = "East Wind"

    def rebuild_wall(self):
        self.wall=Wall()
        self.current_discard = ''
        for i in range(4):
            self.players[i].wipe_hand()
        self.play()
   

    def check_exhaustive_draw(self):
        if self.next_index() == self.wall.deadwall_start:
            print(f"You've hit exhaustive draw. I hope you're in tenpai, nerd.")
            return True
        else:
            return False

    def choose_tile(self):
        user_input = 99
        while not user_input in range(14):
            self.print_player_hand()
            user_input= input("Which tile dumbass?   --")
            if not user_input.isdigit():
                user_input = 99
            else:
                user_input = int(user_input)
        self.pc.discards = self.pc.discards + [self.pc.hand[user_input]]
        self.current_discard=self.pc.hand[user_input]
        self.pc.hand.pop(user_input)
       
        return

   

    def initial_deal(self):
        self.last_index= self.wall.deadwall_end
        num = self.east_num
        counter = 0

        for i in range(4): # Four players
            for j in range(3): # 3 sets of four
                counter+=1
                if self.last_index+4 > 135:
                    self.players[num].hand =self.players[num].hand + self.wall.all_tiles[self.last_index+1:] + self.wall.all_tiles[:self.last_index-131]
                    self.last_index=self.last_index-130
                else:
                    self.players[num].hand = self.players[num].hand+self.wall.all_tiles[self.last_index+1:self.last_index+5]
                    self.last_index=self.last_index+4
                num=self.next_num(num)
        num = self.east_num
        for i in range(4):
                self.players[num].hand = self.players[num].hand+[self.wall.all_tiles[self.next_index()]]
                self.last_index=self.next_index()
                num=self.next_num(num)

    def set_east(self):
        wind_list = ["East Wind", "South Wind", "West Wind", "North Wind"]
        self.east_num = random.randint(0,3)
        wind_list = wind_list[self.east_num:]+wind_list[:self.east_num]
        for i in range(3):
            self.cpu[i].seat_wind = wind_list[i]
        self.pc.seat_wind=wind_list[3]

    def drawing_phase(self, current_player):
       
        self.players[current_player].draw_tile(self.wall.all_tiles[self.next_index()])
        self.players[current_player].sort_hand()
        self.last_index=self.next_index()

    def play(self):
        self.initial_deal()
        current_player = self.east_num
        self.print_hands()
        while True:
            self.drawing_phase(current_player)            
            if not current_player == 3: #AI turn
                self.current_discard = self.players[current_player].discard_random_tile()
                print(self.players[current_player].hand, len(self.players[current_player].hand))
            else: # Player Character Turn
                self.choose_tile()
            self.players[current_player].sort_hand()
            self.last_index=self.next_index()
            #TODO Riichi #
            self.referee.check_riichi(self.players[current_player])
            x = self.referee.run_checks(self.players, self.current_discard, False)  
            print(x)            
            if not x is None:
                p, n = x
                self.players[n] = p
                self.current_discard = self.players[n].discard_random_tile()
                current_player = self.next_num(n)
            else:
                current_player = self.next_num(current_player)
            if self.check_exhaustive_draw():
                self.progress_seat_winds()
                self.rebuild_wall()
   
    ###### Game State Printing ######
    def print_hands(self):
        for i in range(4):
            print(f"Player {i}'s hand: {self.players[i].hand} {len(self.players[i].hand)}'\n")
   
    def print_player_hand(self):
        print(f"Current Tile:   {self.players[3].current_draw}\tSeat Wind:   {self.players[3].seat_wind}\t\tDora:   {self.wall.dora_name}")
        suit = self.players[3].hand[0].suit
        string = ''
        for i in range(14):
            if not self.players[3].hand[i].name == self.players[3].hand[i-1].name:
                if self.players[3].hand[i].suit in ["Sou", "Man", "Pin"] and i > 0:
                    if not int(self.players[3].hand[i].name[-1])== int(self.players[3].hand[i-1].name[-1]) +1:
                        string = string + "/|\   "
                else:
                    string = string + "/|\   "
            if not suit == self.players[3].hand[i].suit:
                string = string + "\n/|\   "
            string = string+f'''{i}: {self.players[3].hand[i]}  '''
            suit = self.players[3].hand[i].suit
        string = string + "/|\ "  
        print(string)
        return
           
   
    def print_seat_winds(self):
        print(f"The prevalent wind is {self.p_wind}. The first dealer was Player {self.first_dealer}")
        for i in range(4):
            print(f"Player {i}'s seat wind: {self.players[i].seat_wind}'\n")


    ### Helper Functions ###
    def next_index(self):
        if self.last_index + 1 > 135:
            return 0
        else:
            return self.last_index + 1

    def next_num(self, number):
            if number == 3:
                return 0
            else:
                return number+1

    def next_tile(self):
        return self.wall.all_tiles[self.next_index()]    

    def progress_seat_winds(self):
        for player in self.players:
            player.update_wind()
            self.print_seat_winds()
        self.east_num = self.players.index([player for player in self.players if player.seat_wind == "East Wind"][0])

       
  



if __name__ == "__main__":

  g = Game()
  g.play()
