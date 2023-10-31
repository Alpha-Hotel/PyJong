import random


class Yaku:

  name = "Generic Yaku"
  menzen_req = True
  normal_shape_req = True
  self_draw_req = False
  single_suit = False


class menzen_tsumo(Yaku):

  name = "Tsumo, Fully Concealed Hand"
  normal_shape_req = False
  self_draw_req = True

class chiitoitsu(Yaku):

  name = "Seven Pairs"
  normal_shape_req = False
  #something here for 7 pair determination, not sure wwhat yet
  


# Lol print(menzen_tsumo.name, 'menzen_req must be:', menzen_tsumo.menzen_req)


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
    "Man_1": Man_1,
    "Man_2": Man_2,
    "Man_3": Man_3,
    "Man_4": Man_4,
    "Man_5": Man_5,
    "Man_6": Man_6,
    "Man_7": Man_7,
    "Man_8": Man_8,
    "Man_9": Man_9,
    "Sou_1": Sou_1,
    "Sou_2": Sou_2,
    "Sou_3": Sou_3,
    "Sou_4": Sou_4,
    "Sou_5": Sou_5,
    "Sou_6": Sou_6,
    "Sou_7": Sou_7,
    "Sou_8": Sou_8,
    "Sou_9": Sou_9,
    "Pin_1": Pin_1,
    "Pin_2": Pin_2,
    "Pin_3": Pin_3,
    "Pin_4": Pin_4,
    "Pin_5": Pin_5,
    "Pin_6": Pin_6,
    "Pin_7": Pin_7,
    "Pin_8": Pin_8,
    "Pin_9": Pin_9,
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

    self.p_wind = "East"

    self.dora_name = ''

    self.dora_tiles = []

    self.build_wall()

    self.break_wall()

    self.check_dora()

    self.set_dora()

  def build_wall(self):

    self.all_tiles = [
        Man_1(),
        Man_2(),
        Man_3(),
        Man_4(),
        Man_5(),
        Man_6(),
        Man_7(),
        Man_8(),
        Man_9(),
        Pin_1(),
        Pin_2(),
        Pin_3(),
        Pin_4(),
        Pin_5(),
        Pin_6(),
        Pin_7(),
        Pin_8(),
        Pin_9(),
        Sou_1(),
        Sou_2(),
        Sou_3(),
        Sou_4(),
        Sou_5(),
        Sou_6(),
        Sou_7(),
        Sou_8(),
        Sou_9(),
        Green_Dragon(),
        Red_Dragon(),
        White_Dragon(),
        East_Wind(),
        South_Wind(),
        West_Wind(),
        North_Wind()
    ] * 4

    random.shuffle(self.all_tiles)

  def break_wall(self):

    roll = random.randint(0, 135)

    self.deadwall_start = roll - 14

    self.deadwall_end = roll

    if self.deadwall_start < 0:

      self.deadwall = self.all_tiles[
          self.deadwall_start:] + self.all_tiles[:self.deadwall_end]

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

      self.dora_name = dora_inidcator.name[:-1] + str(number)

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

    self.dora_tiles = [
        tile for tile in self.all_tiles if tile.name == self.dora_name
    ]

    for tile in self.dora_tiles:

      tile.update_dora()

  def update_prevalent_wind(self):

    self.p_wind = "South"


def check_tenpai(func):

  def tenpai(*args):

    if True:  #TODO Write tenpai check algorithm

      return

    else:

      return func(player)

  return tenpai


def check_furiten(func):

  def furiten(*args):

    if True:  #TODO Write furitan check algorithm

      return None

    else:

      print('here')

      func(player)

      return furiten()

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

    self.discards = list()

    self.closed_hand = True

    self.current_draw = ''

    self.sort_step = 0

    self.i = 0

  def update_wind(self):

    self.seat_wind = progress_wind(self.seat_wind)

  def discard_tile(self):

    pass

  def draw_tile(self, next_tile):

    print("before ", len(self.hand))

    self.current_draw = next_tile.name

    self.hand = self.hand + [next_tile]

    print("after ", len(self.hand))

  def test(self, wall):

    self.hand = [
        Red_Dragon(),
        Man_2(),
        East_Wind(),
        Red_Dragon(),
        Pin_8(),
        West_Wind(),
        Green_Dragon(),
        Man_8(),
        Pin_6(),
        Man_1(),
        Sou_8(),
        Pin_4(),
        Pin_6()
    ]

    pass

  def sort_info(self):

    sort_dict = [{
        'Name': '',
        'Value': 0
    }, {
        'Name': '',
        'Value': 0
    }, {
        'Name': '',
        'Value': 0
    }, {
        'Name': '',
        'Value': 0
    }, {
        'Name': '',
        'Value': 0
    }, {
        'Name': '',
        'Value': 0
    }, {
        'Name': '',
        'Value': 0
    }, {
        'Name': '',
        'Value': 0
    }, {
        'Name': '',
        'Value': 0
    }, {
        'Name': '',
        'Value': 0
    }, {
        'Name': '',
        'Value': 0
    }, {
        'Name': '',
        'Value': 0
    }, {
        'Name': '',
        'Value': 0
    }, {
        'Name': '',
        'Value': 0
    }]

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

    self.hand = [
        tile_dict[tile["Name"]]() for tile in sort_dict
        if tile["Name"] in tile_dict.keys()
    ]


class Game:

  def __init__(self):

    self.pc = Player()

    self.cpu = [Player(), Player(), Player()]

    self.set_east()

    self.players = self.cpu + [self.pc]

    self.wall = Wall()

    self.current_discard = ''

    self.referee = self.Referee()

    self.ai = self.AI()

  def print_hands(self):

    for i in range(4):

      print(
          f"Player {i}'s hand: {self.players[i].hand} {len(self.players[i].hand)}'\n"
      )

  def print_player_hand(self):

    print(
        f"Current Tile:   {self.players[3].current_draw}\tSeat Wind:   {self.players[3].seat_wind}\tDora:   {self.wall.dora_name}"
    )

    for i in range(14):

      print(f'''Tile {i} {self.players[3].hand[i]}''')

  def next_index(self, num):

    if num + 1 > 135:

      return 0

    else:

      return num + 1

  def next_num(self, number):

    if number == 3:

      return 0

    else:

      return number + 1

  def next_tile(self):

    return self.wall.all_tiles[self.next_index(self.last_index)]

  def initial_deal(self):

    self.last_index = self.wall.deadwall_end

    num = self.east_num

    counter = 0

    for i in range(4):  # Four players

      for j in range(3):  # 3 sets of four

        counter += 1

        print(counter)

        print(self.wall.all_tiles[self.last_index + 1:self.last_index + 5])

        if self.last_index + 4 > 135:

          print("greater than 135 ", self.last_index, " ",
                self.last_index - 130)

          self.players[
              num].hand = self.players[num].hand + self.wall.all_tiles[
                  self.last_index +
                  1:] + self.wall.all_tiles[:self.last_index - 131]

          self.last_index = self.last_index - 130

        else:

          self.players[num].hand = self.players[
              num].hand + self.wall.all_tiles[self.last_index +
                                              1:self.last_index + 5]

          self.last_index = self.last_index + 4

        num = self.next_num(num)

    num = self.east_num

    for i in range(4):

      print(self.wall.all_tiles[self.next_index(self.last_index)])

      self.players[num].hand = self.players[num].hand + [
          self.wall.all_tiles[self.next_index(self.last_index)]
      ]

      self.last_index = self.next_index(self.last_index)

      num = self.next_num(num)

  def set_east(self):

    wind_list = ["East Wind", "South Wind", "West Wind", "North Wind"]

    self.east_num = random.randint(0, 3)

    wind_list = wind_list[self.east_num:] + wind_list[:self.east_num]

    for i in range(3):

      self.cpu[i].seat_wind = wind_list[i]

    self.pc.seat_wind = wind_list[3]

  def play(self):

    current_player = self.east_num

    self.print_hands()

    while True:

      self.players[current_player].sort_hand()

      self.players[current_player].draw_tile(
          self.wall.all_tiles[self.next_index(self.last_index)])

      self.players[current_player].sort_hand()

      if not current_player == 3:

        #print("Player number: ",current_player)

        self.current_discard, self.players[
            current_player] = self.ai.discard_random_tile(
                self.players[current_player])

        self.last_index = self.next_index(self.last_index)

      else:  # TODO  list index

        self.last_index = self.next_index(self.last_index)

        #self.print_hands()

        self.print_player_hand()

        user_input = input("Which tile dumbass?   --")

        ##TODO Error Check Input

        user_input = int(user_input)

        self.pc.discards = self.pc.discards + [self.pc.hand[user_input]]

        self.current_discard = self.pc.hand[user_input]

        self.pc.hand.pop(user_input)

      #TODO Riichi #

      self.referee.check_riichi(self.players[current_player])

      p, n = self.referee.run_checks(self.players, self.current_discard)

      if not p is None:

        self.players[n] = p

        self.current_discard, self.players[n] = self.ai.discard_random_tile(
            self.players[n])

        current_player = self.next_num(n)

      else:

        current_player = self.next_num(current_player)

  class AI:

    def discard_random_tile(self, player):

      print("b discard ", len(player.hand))
      random_pick = random.randint(0, 13)
      player.discards = player.discards + [player.hand[random_pick]]
      discard = player.hand[random_pick]
      player.hand.pop(random_pick)
      print("a discard ", len(player.hand))
      return discard, player

  class Referee:

    def run_checks(self, players, current_discard):

      print(self.check_ron)
      ron = self.check_ron(players, current_discard)
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
        return pk[changed], changed

      else:
        return None, None

    def check_pon_kan(self, players, current_discard):

      for i in range(4):
        pc_list = [
            tile for tile in players[i].hand
            if tile.name == current_discard.name
        ]

        print(len(pc_list), current_discard.name)

        if len(pc_list) == 2:  #check Pon
          #print(players[i].hand, pc_list, len(pc_list))

          if i == 3:
            pc_decision = input("Do you want to call pon? y/n")

            if pc_decision == "y":
              players[i].closed_hand = False
              players[i].hand = players[i].hand + [current_discard]
              return players, i  #TODO add headbump

            else:

              return None, None

          else:

            if random.randint(0, 1) == 1:
              players[i].closed_hand = False
              players[i].hand = players[i].hand + [current_discard]
              return players, i  #TODO add headbump

            else:
              return None, None

        elif len(pc_list) == 3:  #check Kan
          #print(players[i].hand, pc_list, len(pc_list))
          #pc_decision = input("Do you want to call kan? y/n")
          return None, None

    def check_chi(self, player, current_discard):
      pass

    def check_exhaustive_draw(self):
      pass

    @check_tenpai
    def check_riichi(self, player):

      pc_decision = input("Do you want to call riichi? y/n")
      pass

    @check_furiten
    @check_tenpai
    def check_ron(self, current_discard):

      pass


if __name__ == "__main__":
  pass
  g = Game()
  g.initial_deal()
  g.play()
