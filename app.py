from random import randint

class Game(object):
    def __init__(self,player,enemy):
        self.player = player
        self.enemy = enemy

    def play(self):
        p_hand = raw_input(">>input your hand goo,choki,pa\n").strip()
        e_hand = self.enemy.hand.rand_hand()
        self.handle_result(p_hand,e_hand)

    # handle result weather user win the game.
    def handle_result(self,p_hand,e_hand):
        print("""
        player: %s \n
        enemy: %s
        """ %(p_hand,e_hand))
        if p_hand == e_hand:
            self.output_msg("It's same , try again please\n")
            self.play()
        elif p_hand == "goo" and e_hand == "choki":
            self.output_msg("You win")
        elif p_hand == "choki" and e_hand == "pa":
            self.output_msg("you win")
        elif p_hand == "pa" and e_hand == "goo":
            self.output_msg("You win")
        else:
            self.output_msg("You lose")

    def output_msg(self,msg):
        print(msg)


class Hand(object):
    def __init__(self):
        self.types = ["goo","choki","pa"]

    def rand_hand(self):
        rand = randint(0,len(self.types)-1)
        return self.types[rand]

class Player(object):
    def __init__(self):
        self.hand = Hand()

class Enemy(object):
    def __init__(self):
        self.hand = Hand()


player = Player()
enemy = Enemy()

game = Game(player,enemy)
game.play()











