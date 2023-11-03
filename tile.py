
class Tile:

  name = "Generic Tile"

  term = False

  honor = False

  locked = False

  suit = ''

  edge = {}

  dora = False

  def lock(self):
      self.locked = True

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

  edge = {"Man_3", "Man_1"}


class Man_3(Tile):

  name = "Man_3"

  suit = "Man"

  edge = {"Man_2", "Man_4"}


class Man_4(Tile):

  name = "Man_4"

  suit = "Man"

  edge = {"Man_3", "Man_5"}


class Man_5(Tile):

  name = "Man_5"

  suit = "Man"

  edge = {"Man_4", "Man_6"}


class Man_6(Tile):

  name = "Man_6"

  suit = "Man"

  edge = {"Man_5", "Man_7"}


class Man_7(Tile):

  name = "Man_7"

  suit = "Man"

  edge = {"Man_6", "Man_8"}


class Man_8(Tile):

  name = "Man_8"

  suit = "Man"

  edge = {"Man_7", "Man_9"}


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

  edge = {"Sou_3", "Sou_1"}


class Sou_3(Tile):

  name = "Sou_3"

  suit = "Sou"

  edge = {"Sou_2", "Sou_4"}


class Sou_4(Tile):

  name = "Sou_4"

  suit = "Sou"

  edge = {"Sou_3", "Sou_5"}


class Sou_5(Tile):

  name = "Sou_5"

  suit = "Sou"

  edge = {"Sou_4", "Sou_6"}


class Sou_6(Tile):

  name = "Sou_6"

  suit = "Sou"

  edge = {"Sou_5", "Sou_7"}


class Sou_7(Tile):

  name = "Sou_7"

  suit = "Sou"

  edge = {"Sou_6", "Sou_8"}


class Sou_8(Tile):

  name = "Sou_8"

  suit = "Sou"

  edge = {"Sou_7", "Sou_9"}


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

  edge = {"Pin_3", "Pin_1"}


class Pin_3(Tile):

  name = "Pin_3"

  suit = "Pin"

  edge = {"Pin_2", "Pin_4"}


class Pin_4(Tile):

  name = "Pin_4"

  suit = "Pin"

  edge = {"Pin_3", "Pin_5"}


class Pin_5(Tile):

  name = "Pin_5"

  suit = "Pin"

  edge = {"Pin_4", "Pin_6"}


class Pin_6(Tile):

  name = "Pin_6"

  suit = "Pin"

  edge = {"Pin_5", "Pin_7"}


class Pin_7(Tile):

  name = "Pin_7"

  suit = "Pin"

  edge = {"Pin_6", "Pin_8"}


class Pin_8(Tile):

  name = "Pin_8"

  suit = "Pin"

  edge = {"Pin_7", "Pin_9"}


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
