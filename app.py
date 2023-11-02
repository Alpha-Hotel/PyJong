import random
from collections import Counter 

#NOTE most of these attributes are arbitrary for the time being, just there to mark things that need to be added. This shit is going to suck
# I've defined open and closed versions of each hand for hands that score differently when open and closed. I've also defined the yakuman as a
# separate group since they behave differently. Any time I reference "check" and a boolean value, I'm referring to the necessary output of such a check.

############ -------------   YAKU   ------------- ############

class yaku:
   
    name = ""
    menzen_req = True
    default_shape_req = True
    tsumo_req = False
    han_value = 0
   
class riichi(yaku):

    name = "Riichi"
    default_shape_req = False
    point_check = True
    han_value = 1

class dbl_riichi(yaku):

    name = "Double Riichi"
    dbl_point_check = True
    no_interrupt = True
    first_round = True
    han_value = 2

class chiitoitsu(yaku):

    name = "Seven Pairs"
    default_shape_req = False
    seven_pair_check = True
    han_value = 2

class closed_sanshoku(yaku):

    name = "Mixed Triple Sequence"
    triple_seq_check = True
    han_value = 2

class open_sanshoku(yaku):

    name = "Mixed Triple Sequence"
    menzen_req = False
    triple_seq_check = True
    han_value = 1    

class tanyao(yaku):
   
    name = "All Simples"
    menzen_req = False
    simples_check = True
    han_value = 1

class closed_pure_straight(yaku):

    name = "Pure Straight"
    #No extra tiles from the suit the straight is in are allowed, eg 1-9 and a pair of 3s
    duplicate_check = False
    han_value = 2

class open_pure_straight(yaku):

    name = "Pure Straight"
    menzen_req = False
    #No extra tiles from the suit the straight is in are allowed, eg 1-9 and a pair of 3s
    duplicate_check = False
    han_value = 1

class pure_dbl_seq(yaku):

    name = "Pure Double Sequence"
    dup_seq_check = True
    han_value = 1

class pinfu(yaku):

    name = "Pinfu"
    fu_check = False
    dbl_sided_wait = True
    han_value = 1

class menzen_tsumo(yaku):

    name = "Menzen Tsumo"
    tsumo_req = True
    default_shape_req = False
    han_value = 1

class ippatsu(yaku):

    name = "Ippatsu"
    no_interrupt = True
    same_round_check = True
    riichi_req = True
    han_value = 1

class dbl_pure_dbl_seq(yaku):

    name = "Two Pure Double Sequences"
    dbl_dup_seq_check = True
    han_value = 3

class toitoi(yaku):

    name = "All Triplets"
    menzen_req = False
    four_pons_check = True
    #something here to say "if it's closed and self draw, yakuman instead" gonna add the yakuman to the yakuman class and work it out later
    han_value = 2

class san_ankou(yaku):

    name = "Three Concealed Triplets"
    menzen_req = False
    triple_concealed_pon_check = True
    han_value = 2

class sanshoku_doukou(yaku):

    name = "Tri Color Triplets"
    menzen_req = False
    three_suit_identical_pon_check = True
    han_value = 2

class sankantsu(yaku):

    name = "Three Kans"
    menzen_req = False
    triple_kan_check = True
    han_value = 2

class yakuhai(yaku):

    number_of_pons = 0
    name = "Yakuhai"
    menzen_req = False
    applicable_honor_pon_check = True
    han_value = number_of_pons

class open_chanta(yaku):

    name = "Outside Hand"
    menzen_req = False
    term_honor_present_all_sets = True
    han_value = 1

class closed_chanta(yaku):

    name = "Outside Hand"
    term_honor_present_all_sets = True
    han_value = 2

class open_junchan(yaku):

    name = "Junchan"
    menzen_req = False
    term_present_all_sets = True
    han_value = 2

class closed_junchan(yaku):

    name = "Junchan"
    menzen_req = False
    term_present_all_sets = True
    han_value = 3

class honrou(yaku):

    name = "All Terminals and Honors"
    menzen_req = False
    default_shape_req = False
    #NOTE: this yaku and all triplets/seven pairs will always be scored together, so total hand value will be 4
    terminal_honor_pon_check = True
    han_value = 2

class shousangen(yaku):

    name = "Little Three Dragons"
    menzen_req = False
    dragon_pon_check = True
    #NOTE: this yaku will always score 2 hand, but the hand wil always be worth 4 han because the two dragon triplets are scored separately.
    han_value = 2

class open_honitsu(yaku):

    name = "Half Flush"
    menzen_req = False
    #NOTE: Can be seven pairs
    default_shape_req = False
    honitsu_check = True
    han_value = 2

class closed_honitsu(yaku):

    name = "Half Flush"
    #NOTE: Can be seven pairs
    default_shape_req = False
    honitsu_check = True
    han_value = 3

class open_chinitsu(yaku):

    name = "Flush"
    menzen_req = False
    #NOTE: Can be seven pairs
    default_shape_req = False
    single_suit_check = True
    han_value = 5

class closed_chinitsu(yaku):

    name = "Flush"
    #NOTE: Can be seven pairs
    default_shape_req = False
    single_suit_check = True
    han_value = 6

############ -------------   YAKUMAN   ------------- ############

class yakuman:

    name = ""
    yakuman_tsumo_req = False
    yakuman_menzen_req = False
    limit_hand = True
    dbl_limit_hand = False

class suuankou(yakuman):

    name = "Four Concealed Triplets"
    yakuman_tsumo_req = True
    yakuman_menzen_req = True
    three_concealed_pon_check = True
    shanpon_wait = True

class tanki_suuankou(yakuman):

    name = "Four Concealed Triplets, Single Tile Wait"
    yakuman_menzen_req = True
    four_concealed_pon_check = True
    shanpon_wait = False
    dbl_limit_hand = True

class daisangen(yakuman):

    name = "Three Big Dragons"
    triple_dragon_pon_check = True

class shousuushii(yakuman):

    name = "Little Four Winds"
    #NOTE three wind triplets and one pair
    three_wind_pons_check = True
    fourth_wind_pair_check = True

class daisuushii(yakuman):

    name = "Big Four Winds"
    four_wind_pons_check = True
    dbl_limit_hand = True

class tsuuiisou(yakuman):

    name = "All Honors"
    all_honor_check = True

class chinroutou(yakuman):

    name = "All Terminals"
    all_terminals_check = True

class all_green(yakuman):

    name = "All Green"
    all_green_check = True

class nine_gates(yakuman):

    name = "Nine Gates"
    yakuman_menzen_req = True
    #NOTE this will suck to write
    nine_gates_check = True
    true_nine_gates_check = False

class true_nine_gates(yakuman):

    name = "True Nine Gates"
    yakuman_menzen_req = True
    nine_gates_check = True
    true_nine_gates_check = True
    dbl_limit_hand = True

class suukantsu(yakuman):

    name = "Four Kans"
    four_kan_check = True

class tenhou(yakuman):

    name = "Blessing of Heaven"
    yakuman_menzen_req = True
    yakuman_tsumo_req = True
    #NOTE stuff here to make sure the dealer is the one who drew, on the first draw of the round
    dealer_first_draw = True

class chiihou(yakuman):

    name = "Blessing of Earth"
    yakuman_menzen_req = True
    yakuman_tsumo_req = True
    yakuman_no_interrupt_check = True
    #NOTE stuff here to make sure the player is the one who drew, with no interrupts from any calls including closed kans
    player_first_draw = True

class renhou(yakuman):

    name = "Blessing of Man"
    yakuman_menzen_req = True
    yakuman_no_interrupt_check = True
    #NOTE Just for winning off someone else's discard in the first round, again with no interrupts
    yakuman_first_round = True

class Tile:
    name = "Generic Tile"
    term = False
    honor = False
    locked = False
    suit = ''
    edge = {}
    dora = False
    def full_repr(self):
        return f"""*********\n{self.name}\nTerminal: {self.term}\nHonor: {self.honor}\nSuit: {self.suit}\nEdges: {self.edge}\nDora: {self.dora}\n*********"""
    def __repr__(self):
        return f"{self.name}"
    def update_dora(self):
        self.dora = True

############ -------------   MAN   ------------- ############

class Man_1(Tile):
    def update_dora(self):
        self.dora = True
    name = "Man_1"
    suit = "Man"
    term = True
    edge = {"Man_2"}

class Man_2(Tile):
    name = "Man_2"
    suit = "Man"
    edge = {"Man_3, Man_1"}

class Man_3(Tile):
    name = "Man_3"
    suit = "Man"
    edge = {"Man_2, Man_4"}

class Man_4(Tile):
    name = "Man_4"
    suit = "Man"
    edge = {"Man_3, Man_5"}

class Man_5(Tile):
    name = "Man_5"
    suit = "Man"
    edge = {"Man_4, Man_6"}

class Man_6(Tile):
    name = "Man_6"
    suit = "Man"
    edge = {"Man_5, Man_7"}

class Man_7(Tile):
    name = "Man_7"
    suit = "Man"
    edge = {"Man_6, Man_8"}

class Man_8(Tile):
    name = "Man_8"
    suit = "Man"
    edge = {"Man_7, Man_9"}

class Man_9(Tile):
    name = "Man_9"
    suit = "Man"
    edge = {"Man_8"}
    term = True

############ -------------   SOU   ------------- ############

class Sou_1(Tile):
    name = "Sou_1"
    suit = "Sou"
    term = True
    edge = {"Sou_2"}

class Sou_2(Tile):
    name = "Sou_2"
    suit = "Sou"
    edge = {"Sou_3, Sou_1"}

class Sou_3(Tile):
    name = "Sou_3"
    suit = "Sou"
    edge = {"Sou_2, Sou_4"}

class Sou_4(Tile):
    name = "Sou_4"
    suit = "Sou"
    edge = {"Sou_3, Sou_5"}

class Sou_5(Tile):
    name = "Sou_5"
    suit = "Sou"
    edge = {"Sou_4, Sou_6"}

class Sou_6(Tile):
    name = "Sou_6"
    suit = "Sou"
    edge = {"Sou_5, Sou_7"}

class Sou_7(Tile):
    name = "Sou_7"
    suit = "Sou"
    edge = {"Sou_6, Sou_8"}

class Sou_8(Tile):
    name = "Sou_8"
    suit = "Sou"
    edge = {"Sou_7, Sou_9"}

class Sou_9(Tile):
    name = "Sou_9"
    term = True
    suit = "Sou"
    edge = {"Sou_8"}

############ -------------   PIN   ------------- ############

class Pin_1(Tile):
    name = "Pin_1"
    suit = "Pin"
    term = True
    edge = {"Pin_2"}

class Pin_2(Tile):
    name = "Pin_2"
    suit = "Pin"
    edge = {"Pin_3, Pin_1"}

class Pin_3(Tile):
    name = "Pin_3"
    suit = "Pin"
    edge = {"Pin_2, Pin_4"}

class Pin_4(Tile):
    name = "Pin_4"
    suit = "Pin"
    edge = {"Pin_3, Pin_5"}

class Pin_5(Tile):
    name = "Pin_5"
    suit = "Pin"
    edge = {"Pin_4, Pin_6"}

class Pin_6(Tile):
    name = "Pin_6"
    suit = "Pin"
    edge = {"Pin_5, Pin_7"}

class Pin_7(Tile):
    name = "Pin_7"
    suit = "Pin"
    edge = {"Pin_6, Pin_8"}

class Pin_8(Tile):
    name = "Pin_8"
    suit = "Pin"
    edge = {"Pin_7, Pin_9"}

class Pin_9(Tile):
    name = "Pin_9"
    term = True
    suit = "Pin"
    edge = {"Pin_8"}


############ -------------   DRAGONS   ------------- ############

class Green_Dragon(Tile):
    name = "Green Dragon"
    suit = "Dragon"
    honor = True

class Red_Dragon(Tile):
    name = "Red Dragon"
    suit = "Dragon"
    honor = True

class White_Dragon(Tile):
    name = "White Dragon"
    suit = "Dragon"
    honor = True

############ -------------   WINDS   ------------- ############

class North_Wind(Tile):
    name = "North Wind"
    suit = "Wind"
    honor = True

class East_Wind(Tile):
    name = "East Wind"
    suit = "Wind"
    honor = True

class South_Wind(Tile):
    name = "South Wind"
    suit = "Wind"
    honor = True

class West_Wind(Tile):
    name = "West Wind"
    suit = "Wind"
    honor = True

tile_dict = {
    "Man_1":Man_1,
    "Man_2":Man_2,
    "Man_3":Man_3,
    "Man_4":Man_4,
    "Man_5":Man_5,
    "Man_6":Man_6,
    "Man_7":Man_7,
    "Man_8":Man_8,
    "Man_9":Man_9,
    "Sou_1":Sou_1,
    "Sou_2":Sou_2,
    "Sou_3":Sou_3,
    "Sou_4":Sou_4,
    "Sou_5":Sou_5,
    "Sou_6":Sou_6,
    "Sou_7":Sou_7,
    "Sou_8":Sou_8,
    "Sou_9":Sou_9,
    "Pin_1":Pin_1,
    "Pin_2":Pin_2,
    "Pin_3":Pin_3,
    "Pin_4":Pin_4,
    "Pin_5":Pin_5,
    "Pin_6":Pin_6,
    "Pin_7":Pin_7,
    "Pin_8":Pin_8,
    "Pin_9":Pin_9,
    "Green Dragon": Green_Dragon,
    "White Dragon": White_Dragon,
    "Red Dragon": Red_Dragon,
    "North Wind": North_Wind,
    "South Wind": South_Wind,
    "West Wind": West_Wind,
    "East Wind": East_Wind,
}

class Wall:

    def __init__(self):
        self.all_tiles = []
        self.deadwall = []
        self.deadwall_start = int
        self.deadwall_end = int
        self.dora_name = ''
        self.dora_tiles = []
        self.build_wall()
        self.break_wall()
        self.check_dora()
        self.set_dora()


    def build_wall(self):
        self.all_tiles = [Man_1(), Man_2(), Man_3(), Man_4(), Man_5(), Man_6(), Man_7(), Man_8(), Man_9(),
                            Pin_1(),Pin_2(),Pin_3(),Pin_4(), Pin_5(), Pin_6(), Pin_7(), Pin_8(), Pin_9(),
                            Sou_1(), Sou_2(), Sou_3(), Sou_4(), Sou_5(), Sou_6(), Sou_7(), Sou_8(), Sou_9(),
                            Green_Dragon(), Red_Dragon(), White_Dragon(),
                            East_Wind(), South_Wind(), West_Wind(), North_Wind()
                            ]*4
        random.shuffle(self.all_tiles)
   
    def break_wall(self):
        roll = random.randint(0,135)
        self.deadwall_start = roll-14
        self.deadwall_end = roll
        if self.deadwall_start < 0:
            self.deadwall = self.all_tiles[self.deadwall_start:]+ self.all_tiles[:self.deadwall_end]
        else:
            self.deadwall = self.all_tiles[self.deadwall_start:self.deadwall_end]
   
    def check_dora(self):
        dora_inidcator = self.deadwall[-6]
        if dora_inidcator.honor == False:
            number = int(dora_inidcator.name[-1])
            if number == 9:
                number = 1
            else:
                number = number + 1
            self.dora_name = dora_inidcator.name[:-1]+str(number)
       
        elif dora_inidcator.suit == "Dragon":
            if dora_inidcator.name == "White Dragon":
                self.dora_name = "Green Dragon"
            elif dora_inidcator.name == "Green Dragon":
                self.dora_name = "Red Dragon"
            elif dora_inidcator.name == "Red Dragon":
                self.dora_name = "White Dragon"
       
        elif dora_inidcator.suit == "Wind":
            self.dora_name = progress_wind(dora_inidcator.name)
       

   
    def set_dora(self):
        self.dora_tiles = [tile for tile in self.all_tiles if tile.name == self.dora_name]
        for tile in self.dora_tiles:
            tile.update_dora()
           

    def update_prevalent_wind(self):
        self.p_wind = "South Wind"


def check_tenpai(func):
    def tenpai(*args):
        if True: #TODO Write tenpai check algorithm
            return
        else:
            return func(player)
    return tenpai

def check_furiten(func):
    def furiten(*args):
        if True: #TODO Write furitan check algorithm
            return None
        else:
            func(player)
            return
    return furiten



def progress_wind(wind):
    if wind == "East Wind":
        return "South Wind"
    elif wind == "South Wind":
        return "West Wind"
    elif wind == "West Wind":
        return "North Wind"
    elif wind == "North Wind":
        return "East Wind"

class Player:
    def __init__(self):
        self.seat_wind = ''
        self.hand = list()
        self.open_hand = list()
        self.discards = list()
        self.closed_hand = True
        self.current_draw = ''
        self.sort_step = 0
        self.i = 0
       
   
    def wipe_hand(self):
        self.hand = []

    def update_wind(self):
        self.seat_wind= progress_wind(self.seat_wind)
    def discard_tile(self):
        pass
    def draw_tile(self, next_tile):
        self.current_draw = next_tile.name
        self.hand = self.hand + [next_tile]
    def test(self, wall):
        self.hand = [Red_Dragon(), Man_2(), East_Wind(), Red_Dragon(), Pin_8(), West_Wind(), Green_Dragon(), Man_8(),
        Pin_6(), Man_1(), Sou_8(), Pin_4(), Pin_6()]
        pass

    def sort_info(self):
        sort_dict = [{'Name': '', 'Value': 0}, {'Name': '', 'Value': 0}, {'Name': '', 'Value': 0},
        {'Name': '', 'Value': 0}, {'Name': '', 'Value': 0}, {'Name': '', 'Value': 0}, {'Name': '', 'Value': 0},
        {'Name': '', 'Value': 0}, {'Name': '', 'Value': 0}, {'Name': '', 'Value': 0}, {'Name': '', 'Value': 0},
        {'Name': '', 'Value': 0}, {'Name': '', 'Value': 0}, {'Name': '', 'Value': 0}]
        for i in range(len(self.hand)):

            if len(self.hand[i].name) == 5:
                if self.hand[i].name[0] == 'M':
                    sort_dict[i]['Name'] = self.hand[i].name
                    sort_dict[i]['Value'] = int(self.hand[i].name[4])
                elif self.hand[i].name[0] == 'P':
                    sort_dict[i]['Name'] = self.hand[i].name
                    sort_dict[i]['Value'] = (int(self.hand[i].name[4]) + 9)
                elif self.hand[i].name[0] == 'S':
                    sort_dict[i]['Name'] = self.hand[i].name
                    sort_dict[i]['Value'] = (int(self.hand[i].name[4]) + 18)
            else:
                if self.hand[i].name[0] == 'R':
                    sort_dict[i]['Name'] = self.hand[i].name
                    sort_dict[i]['Value'] = 28
                elif self.hand[i].name[0] == 'W' and self.hand[i].name[1] == 'h':
                    sort_dict[i]['Name'] = self.hand[i].name
                    sort_dict[i]['Value'] = 29
                elif self.hand[i].name[0] == 'G':
                    sort_dict[i]['Name'] = self.hand[i].name
                    sort_dict[i]['Value'] = 30
                elif self.hand[i].name[0] == 'N':
                    sort_dict[i]['Name'] = self.hand[i].name
                    sort_dict[i]['Value'] = 31
                elif self.hand[i].name[0] == 'E':
                    sort_dict[i]['Name'] = self.hand[i].name
                    sort_dict[i]['Value'] = 32
                elif self.hand[i].name[0] == 'S' and self.hand[i].name[3] == 't':
                    sort_dict[i]['Name'] = self.hand[i].name
                    sort_dict[i]['Value'] = 33
                elif self.hand[i].name[0] == 'W' and self.hand[i].name[1] == 'e':
                    sort_dict[i]['Name'] = self.hand[i].name
                    sort_dict[i]['Value'] = 34
        return sort_dict

    def sort_method(self, x):
        return x["Value"]
     
           
    def sort_hand(self):
        sort_dict = self.sort_info()
        sort_dict.sort(key=self.sort_method)
        self.hand =[tile_dict[tile["Name"]]() for tile in sort_dict if tile["Name"] in tile_dict.keys()]


class Game:
    def __init__(self):
        self.just_discarded = ''
        self.pc = Player()
        self.cpu = [Player(), Player(), Player()]
        self.set_east()
        self.first_dealer = self.east_num
        self.players = self.cpu + [self.pc]
        self.wall = Wall()
        self.current_discard = ''
        self.referee = self.Referee()
        self.ai = self.AI()
        self.p_wind = "East Wind"

    def rebuild_wall(self):
        self.wall=Wall()
        self.current_discard = ''
        for i in range(4):
            self.players[i].wipe_hand()
        self.play()
   

    def check_exhaustive_draw(self):
        if self.next_index(self.last_index) == self.wall.deadwall_start:
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
        #For checking if the player was the discarder of the tile, so I can't call pon on my own discard. lol
        self.just_discarded = 'P3'        
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
                self.players[num].hand = self.players[num].hand+[self.wall.all_tiles[self.next_index(self.last_index)]]
                self.last_index=self.next_index(self.last_index)
                num=self.next_num(num)

    def set_east(self):
        wind_list = ["East Wind", "South Wind", "West Wind", "North Wind"]
        self.east_num = random.randint(0,3)
        wind_list = wind_list[self.east_num:]+wind_list[:self.east_num]
        for i in range(3):
            self.cpu[i].seat_wind = wind_list[i]
        self.pc.seat_wind=wind_list[3]

    def drawing_phase(self, current_player):
       
        self.players[current_player].draw_tile(self.wall.all_tiles[self.next_index(self.last_index)])
        self.players[current_player].sort_hand()

    def play(self):
        self.initial_deal()
        current_player = self.east_num
        print("***** NEW HAND *****")
        self.print_hands()
        while True:
            self.drawing_phase(current_player)            
            if not current_player == 3: #AI turn
                self.current_discard, self.players[current_player] = self.ai.discard_random_tile(self.players[current_player])
            else: # Player Character Turn
                self.choose_tile()
            self.players[current_player].sort_hand()
            self.last_index=self.next_index(self.last_index)
            #TODO Riichi #
            self.referee.check_riichi(self.players[current_player])
            p, n = self.referee.run_checks(self.players, self.current_discard)
            if not p is None:
                self.players[n] = p
                self.current_discard, self.players[n] = self.ai.discard_random_tile(self.players[n])
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
   
    class AI:
       

        def discard_random_tile(self, player):

            self.just_discarded = 'AI'
            random_pick = random.randint(0, 13)
            player.discards = player.discards + [player.hand[random_pick]]
            discard = player.hand[random_pick]
            player.hand.pop(random_pick)
            return discard, player


    class Referee:
       

        def run_checks(self, players, current_discard):
            ron = self.check_ron(players,current_discard)
            pk = None
            changed = None
            chi = None
            if ron == None:
                x = self.check_pon_kan(players, current_discard)
                if not x is None:
                    pk, changed = x
            if pk == None:
                x = self.check_chi(players, current_discard)
                if not x is None:
                    chi, changed = x
            else:
                return pk[changed], changed
            if chi:
                
                return chi[changed], changed
            else:
                return None, None



        def check_pon_kan(self, players, current_discard):
            for i in range(4):

                pc_list = [tile for tile in players[i].hand if tile.name == current_discard.name]
                             
                if len(pc_list) == 2: #check Pon
                    #print(players[i].hand, pc_list, len(pc_list))
                    if i == 3:
                        pc_decision = input("Do you want to call pon? y/n   ")
                        if pc_decision == "y":
                            players[i].closed_hand = False
                            players[i].hand=players[i].hand + [current_discard]
                            return players, i #TODO add headbump
                        else:
                            return None, None
                    else:
                        if random.randint(0,1)==1:
                            print("Player ", players[i], "called pon!")
                            players[i].closed_hand = False
                            players[i].hand=players[i].hand + [current_discard]
                            return players, i #TODO add headbump
                        else:
                            print("Player ", players[i], "didn't call pon.", "            -FOR TESTING DUH-")
                            return None, None
                           

                elif len(pc_list) == 3: #check Kan
                    #print(players[i].hand, pc_list, len(pc_list))
                    #pc_decision = input("Do you want to call kan? y/n")
                    return None, None
   
       
        def check_chi(self, players, current_discard):

           
            new_list = []
            #lmao im so funny
            cheese_list_1 = []
            cheese_list_2 = []
            cheese_list_3 = []
            adjacency_check = False
            list_length = int(len(new_list))

            if current_discard.name[4].isdigit():
                for i in range(4):

                    new_list = []
                    # clears list so there's no overlap between checking hands for chi chances (Yeah I know it's only for the pplayer to the right of the discard,
                    # but im a fucking idiot and can't figure out how to pull the person who discarded into this function. lmfao)
                    #TODO: fix it lmao

                    this_tile = []

                    
                    print(new_list)

                    for tile in players[i].hand:
                        
                        this_tile = [tile.name]

                        if tile.name[0] == current_discard.name[0] and tile.name[4].isdigit():
                            
                            for j in range(list_length):
                                if (int(new_list[j][4]) == (int(this_tile[4]) + 1)) or (int(new_list[j][4]) == (int(this_tile[4]) - 1)):
                                    adjacency_check = True
                                else:
                                    adjacency_check = False


                            if (int(tile.name[4]) == (int(current_discard.name[4]) + 1)):
                               
                                new_list = new_list + this_tile
                                print(new_list)

                            if (int(tile.name[4]) == (int(current_discard.name[4]) - 1)):
                               
                                new_list = new_list + this_tile
                                print(new_list)

                            if (int(tile.name[4]) == (int(current_discard.name[4]) + 2) and adjacency_check == True):
                               
                                new_list = new_list + this_tile
                                print(new_list)

                            if (int(tile.name[4]) == (int(current_discard.name[4]) - 2) and adjacency_check == True):
                               
                                new_list = new_list + this_tile
                                print(new_list)

                        #normally set to    2                    and                    2

                        if len(new_list) >= 2 and len(set(Counter(new_list).keys())) >= 2:
                           
                            if i == 3:
                                pc_decision_chi = input("Do you want to call chi? y/n   ")

                                if pc_decision_chi == "y":

                                    if len(set(Counter(new_list).keys())) >= 3:

                                        print("Chose a set to chi with.")

                                        for k in range(len(int(new_list))):
                                            if k == 0:
                                                return

                                            if new_list[k] == new_list[k-1]:
                                                return

                                            if int(new_list[k][4]) == (int(new_list[k+2][4] - 2)):
                                                cheese_list_1 = cheese_list_1 + new_list[k-2] + new_list[k]

                                            if int(new_list[k][4]) == (int(new_list[k+2][4] - 1)):
                                                cheese_list_2 = cheese_list_2 + new_list[k-1] + new_list[k]
                                            print(cheese_list_1, " x ", cheese_list_2, " x ", cheese_list_3, " x ", )

                                    current_discard_list = [current_discard]
                                    players[i].closed_hand = False
                                    players[i].hand=players[i].hand + [current_discard]
                                    return players, i #TODO add headbump

                                else:

                                    return None, None
                            
                            else:
                                
                                if random.randint(0,1)==1:
                                    print("AI player ", players[i], "called chi on: ", current_discard)
                                    players[i].closed_hand = False
                                    players[i].hand=players[i].hand + [current_discard]
                                    return players, i #TODO add headbump

                                else:

                                    print("AI player didn't call chi on: ", current_discard, ". What a rookie.")
                                    return None, None

                           
                    pass
                pass
           

           
       
       
        def check_locked_hand(self, hand):
            if len([tile for tile in hand if tile.locked] == 13):
                return True
            else:
                return False
       
       
       
        @check_tenpai
        def check_riichi(self, player):
            pc_decision = input("Do you want to call riichi? y/n")
            pass
       
        @check_furiten
        @check_tenpai
        def check_ron(self, current_discard):
            pass

    ### Helper Functions ###
    def next_index(self, num):
        if num + 1 > 135:
            return 0
        else:
            return num + 1

    def next_num(self, number):
            if number == 3:
                return 0
            else:
                return number+1

    def next_tile(self):
        return self.wall.all_tiles[self.next_index(self.last_index)]    

    def progress_seat_winds(self):
        for player in self.players:
            player.update_wind()
            self.print_seat_winds()
        self.east_num = self.players.index([player for player in self.players if player.seat_wind == "East Wind"][0])

       

   
   

if __name__ == "__main__":
   g = Game()
   g.play()
