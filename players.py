from tile import *
import random
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


    def discard_random_tile(self):

        print("b discard ", len(self.hand))
        random_pick = random.randint(0, 13)
        self.discards = self.discards + [self.hand[random_pick]]
        discard = self.hand[random_pick]
        self.hand.pop(random_pick)
        print("a discard ", len(self.hand))
        return discard
    
    def defensive_discard(self):
        pass
