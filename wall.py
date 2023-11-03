from tile import *
import random


def progress_wind(wind):

  if wind == "East Wind":

    return "South Wind"

  elif wind == "South Wind":

    return "West Wind"

  elif wind == "West Wind":

    return "North Wind"

  elif wind == "North Wind":

    return "East Wind"

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
