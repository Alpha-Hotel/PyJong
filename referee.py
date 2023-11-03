from collections import Counter 
import random
from tile import *

class Referee:

    
    def check_tenpai(func):

        def tenpai(*args):
            if True:  #TODO Write tenpai check algorithm
                return
            else:
                return func(player)

        return tenpai

    def check_if_number(func): #decorator
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
                print("chi")
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
            if len(pc_list) == 2:  #check Pon

                if i == 3:
                    pc_decision = input("Do you want to call pon? y/n")

                    if pc_decision == "y":
                        players[i].closed_hand = False
                        players[i].hand = players[i].hand + [current_discard]
                        return players[i], i  #TODO add headbump
                        pon_tiles = 0
                        while pon_tiles < 3:
                            tiles = [tile for tile in player.hand if tile is current_discard]
                            tile_index = player.hand.index(tiles[0])
                            player.hand[tile_index].lock()
                            pon_tiles += 1
                    else:

                        return None

                else:
                    pass
                if random.randint(0, 1) == 1:
                    players[i].closed_hand = False
                    players[i].hand = players[i].hand + [current_discard]
                    return players[i], i  #TODO add headbump

                else:
                    return None

            elif len(pc_list) == 3:  #check Kan
                return None

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

                                return None
                        
                        else:
                            
                            if random.randint(0,1)==1:
                                print("AI player ", players[i], "called chi on: ", current_discard)
                                players[i].closed_hand = False
                                players[i].hand=players[i].hand + [current_discard]
                                return players[i], i #TODO add headbump

                            else:

                                print("AI player didn't call chi on: ", current_discard, ". What a rookie.")
                                return None

                               
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
            pc_decision_chi = int(pc_decision_chi)
            player.closed_hand = False
            player.hand=player.hand + [current_discard]
            for i in range(3):
                tiles = [tile for tile in player.hand if chi_choices[pc_decision_chi][i] is tile]
                tile_index = player.hand.index(tiles[0])
                print(tiles)
                player.hand[tile_index].lock()

            #for i in range(len(player.hand)): print(player.hand[i], "is", player.hand[i].locked)
            #TODO add lock here
            return player 
        else: 
            return None

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




    
