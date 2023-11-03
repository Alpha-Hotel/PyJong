from players import *
from referee import *

class Generic_Test_Suite:
    '''Generic_Test_Suite with stringify function'''
    def __init__(self, ref):
        self.name = "Generic"
    
    def str_test(self, li):
        return f"{self.name} Tests:\n{sum(li)} out of {len(li)} tests passed."

class Referee_Test_Suite(Generic_Test_Suite):
    '''Suite for testing referee module'''
    def __init__(self, ref):
        self.name="Referee"
        self.player = Player()
        self.run_tests(ref)
        
    def run_tests(self, ref):
        '''Run tests is set up to run the all of the tests that have been written. It will
        then print information about the test pass rate
        '''
        print(self.str_test([self.test_chi_1(ref.check_chi),
        self.test_chi_2(ref.check_chi),
        self.test_chi_3(ref.check_chi)]))
    def test_chi_1(self, check_chi):
        self.player.hand = [Sou_2(),Sou_3()]
        player, _ = check_chi([self.player], Sou_4(), True)
        x = [tile.name for tile in player.hand]
        if x in [['Sou_2', 'Sou_3', 'Sou_4'], ['Sou_2', 'Sou_3']]:
            return True
        else:
            return False
    def test_chi_2(self, check_chi):
        self.player.hand = [Sou_4(),Sou_5(),Sou_5(),Sou_6(), Sou_7()]
        player, _ = check_chi([self.player], Sou_6(), True)
        x = [tile.name for tile in player.hand]
        if x in [['Sou_4', 'Sou_5', 'Sou_5', 'Sou_6', 'Sou_7', 'Sou_6'], ['Sou_4', 'Sou_5', 'Sou_5', 'Sou_6', 'Sou_7']]:
            return True
        else:
            return False
    def test_chi_3(self, check_chi):
        self.player.hand = [Sou_4(),Sou_5(),Sou_5(),Sou_6(), Sou_7()]
        x = check_chi([self.player], Red_Dragon(), True)
        if x is None:
            return True
        else:
            return False
    

if __name__ == "__main__":
    Referee_Test_Suite(Referee())
