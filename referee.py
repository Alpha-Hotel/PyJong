from collections import Counter 
import random
from tile import *
from players import *
class Referee:

    
    def check_tenpai(func):

        def tenpai(*args):
            if True:  #TODO Write tenpai check algorithm
                return
            else:
                return func(player)

        return tenpai

    def check_if_number(func):
        pass
        """
        def tenpai(*args):
            if True:  #TODO Write tenpai check algorithm
                return
            else:
                return func(player)

        return tenpai"""

    def check_furiten(func):

        def furiten(*args):

            if True:  #TODO Write furitan check algorithm

                return None

            else:

                print('here')

                func(player)

                return furiten()

        return furiten

    
    def run_checks(self, players, current_discard, test:bool):
        ron = self.check_ron(players,current_discard)

        pk = None
        changed = None
        chi = None
        if ron == None:
            x = self.check_pon_kan(players, current_discard,test)
            if not x is None:
                pk, changed = x
                print("pon/kan")
                return pk, changed
            x = self.check_chi(players, current_discard,test)
            if not x is None:
                chi, changed = x
                return chi, changed
            else: 
                return None
        else:
            pass #TODO
            #somebody called ron
        


    def check_pon_kan(self, players, current_discard, test:bool):

        for i in range(len(players)):
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
                pass
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

    def check_chi(self, players, current_discard, test):
            '''Check if it is possible for any of the players to call chi on the current discard.'''
            if current_discard.name[4].isdigit(): #Non-honor
                for i in range(len(players)): 
                    new_list = [tile for tile in players[i].hand if current_discard.name in tile.edge] #tiles adjacent to current discard
                    for node in new_list:
                        new_list = new_list + [tile for tile in players[i].hand if node.name in tile.edge and not tile.name == current_discard.name ]
                        #tiles adjacent to tiles adjacent to current discard

                    if len(new_list) >= 2 and len(set(Counter(new_list).keys())) >= 2:
                        if i == 3 or test: #player decisions
                            player = self.player_chi_choice(players[i], new_list, current_discard)
                            if not player == None:
                                return player, i #TODO add headbump
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

                               
    def player_chi_choice(self, player, new_list, current_discard):
        '''Function for checking if the player wants to call chi on one of all possible combinations.'''
        two_to_left = [tile for tile in new_list if int(tile.name[-1]) == int(current_discard.name[-1])-2]
        one_to_left = [tile for tile in new_list if int(tile.name[-1]) == int(current_discard.name[-1])-1]
        two_to_right = [tile for tile in new_list if int(tile.name[-1]) == int(current_discard.name[-1])+2]
        one_to_right = [tile for tile in new_list if int(tile.name[-1]) == int(current_discard.name[-1])+1]
        chi_choices = []
        if two_to_left and one_to_left:
            chi_choices.append([two_to_left[0], one_to_left[0], current_discard])
        if one_to_left and one_to_right:
            chi_choices.append([ one_to_left[0], current_discard, one_to_right[0]])
        if one_to_right and two_to_right:
            chi_choices.append([ current_discard, one_to_right[0], two_to_right[0]])
        pc_decision_chi = input(self.str_chi_options(chi_choices))
        if not pc_decision_chi == "n":
            player.closed_hand = False
            player.hand=player.hand + [current_discard]
            #TODO add lock here
        return player 

    def str_chi_options(self, chi_choices):
        '''Creates "pretty" string for asking a user whether they want to call chi'''
        string = "\nChoose from the following Chi options:\n"
        for choice in range(len(chi_choices)):
            string += f"{choice}: {chi_choices[choice][0]}, {chi_choices[choice][1]}, {chi_choices[choice][2]}\n"
        string += f"n: Don't call Chi\n"
        return string

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



class Referee_Test_Suite:
    def __init__(self, ref):
        self.player = Player()
        self.run_tests(ref)
        
    def run_tests(self, ref):
        '''Run tests is set up to run the all of the tests that have been written. It will
        '''
        print(self.str_test([self.test_chi_1(ref.check_chi),
        self.test_chi_2(ref.check_chi)]))
    def test_chi_1(self, check_chi):
        self.player.hand = [Sou_2(),Sou_3()]
        player, _ = check_chi([self.player], Sou_4(), True)
        x = [tile.name for tile in player.hand]
        assert x == ['Sou_2', 'Sou_3', 'Sou_4'] or ['Sou_2', 'Sou_3']
        return True
    def test_chi_2(self, check_chi):
        self.player.hand = [Sou_4(),Sou_5(),Sou_5(),Sou_6(), Sou_7()]
        player, _ = check_chi([self.player], Sou_6(), True)
        x = [tile.name for tile in player.hand]
        assert x == ['Sou_4', 'Sou_5', 'Sou_5', 'Sou_6', 'Sou_7', 'Sou_6'] or ['Sou_4', 'Sou_5', 'Sou_5', 'Sou_6', 'Sou_7']
        return True
    def str_test(self, li):
        return f"{sum(li)} out of {len(li)} tests passed."

if __name__ == "__main__":
    test = Referee_Test_Suite(Referee())
    
