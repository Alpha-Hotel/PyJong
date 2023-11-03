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
