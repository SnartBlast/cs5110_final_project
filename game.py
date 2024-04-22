import random


class Game():
    def __init__(self, agent_0, agent_1, rounds):
        # initialize class with agent class 
        self.agent_0 = agent_0
        self.agent_1 = agent_1
        self.agent_0_moves = []
        self.agent_1_moves = []
        self.rounds = rounds

        # score 
        self.creativity = 0
        self.quality = 0
        self.timliness = 0
        self.profit = 0


    def do_game(self):
        # perform a series of rounds between the two agents  
        multiplier = 0

        for i in range(self.rounds):
            move_0 = self.agent0_next_move()
            move_1 = self.agent1_next_move()
            self.agent_0_moves.append(move_0)
            self.agent_1_moves.append(move_1)
#            print(f'move 0 -> {move_0}')
#            print(f'move 1 -> {move_1}\n')
 
            if (self.agent_0.position == 'developer'):
                # if both cooperate
                if (move_0 == 1 and move_1 == 1):
                    self.quality += multiplier
                    multiplier += 1
                # if one cooperates
                elif (move_0 == 0 and move_1 == 1):
                    self.creativity += 1
                    self.timliness -= 1
                elif (move_0 == 1 and move_1 == 0):
                    self.creativity -= 1
                    self.timliness += 1
                # if both defect
                else:
                    muliplier = 0

            elif (self.agent_0.position == 'manager'):
                # if both cooperate
                if (move_0 == 1 and move_1 == 1):
                    self.timliness += multiplier
                    multiplier += 1
                # if one cooperates
                elif (move_0 == 0 and move_1 == 1):
                    self.quality += 1
                    self.profit -= 1
                elif (move_0 == 1 and move_1 == 0):
                    self.quality -= 1
                    self.profit += 1
                # if both defect
                else:
                    muliplier = 0

            elif (self.agent_0.position == 'stakeholder'):
                # if both cooperate
                if (move_0 == 1 and move_1 == 1):
                    self.profit += multiplier
                    multiplier += 1
                # if one cooperates
                elif (move_0 == 0 and move_1 == 1):
                    self.timliness += 1
                    self.creativity -= 1
                elif (move_0 == 1 and move_1 == 0):
                    self.timliness -= 1
                    self.creativity += 1
                # if both defect
                else:
                    muliplier = 0

            elif (self.agent_0.position == 'customer'):
                # if both cooperate
                if (move_0 == 1 and move_1 == 1):
                    self.creativity += multiplier
                    multiplier += 1
                # if one cooperates
                elif (move_0 == 0 and move_1 == 1):
                    self.profit += 1
                    self.quality -= 1
                elif (move_0 == 1 and move_1 == 0):
                    self.profit -= 1
                    self.quality += 1
                # if both defect
                else:
                    muliplier = 0

        return [self.creativity, self.timliness, self.quality, self.profit]


    def report(self):
        # report the score of the rounds of the game
        print(f'Creativity -> {self.creativity}') 
        print(f'   Quality -> {self.quality}') 
        print(f' Timliness -> {self.timliness}') 
        print(f'    Profit -> {self.profit}') 
 

    def agent0_next_move(self):
        # IF TIT FOR TAT
        if (self.agent_0.attitude == 'tit_for_tat'):
            if (len(self.agent_0_moves) == 0):
                return 1
            else:
                return self.agent_1_moves[-1] 

        # IF TESTER
        elif (self.agent_0.attitude == 'tester'):
            if (len(self.agent_0_moves) == 0):     
                return 0
            else:
                if (len(self.agent_1_moves) == 1):
                    # if retaliate 
                    if (self.agent_1_moves[0] == 0):
                        return 1
                    else:
                        return 0
                else:
                    if (len(self.agent_1_moves) > 1):
                        return self.agent_1_moves[-1]
                    else:
                        return 1

        # IF JOSS
        elif (self.agent_0.attitude == 'joss'):
            if (len(self.agent_0_moves) == 0):
                return 1
            else:
                if (random.randint(1, 10) == 1):
                    return 0
                else:
                    if (len(self.agent_0_moves) >= 1):
                        return self.agent_0_moves[-1] 
                    else:
                        return 1

        # IF TIT FOR TWO TATS
        elif (self.agent_0.attitude == 'tit_for_two_tats'):
            if (len(self.agent_1_moves) >= 2):  
                if (self.agent_1_moves[-1] == 0 and self.agent_1_moves[-2] == 0):
                    return 0
                else:
                    return 1
            else:
                return 1

        # IF CONFRONTATIONAL
        elif (self.agent_0.attitude == 'confrontational'):
            if (len(self.agent_1_moves) == 0):
                return 1
            else:
                return len(self.agent_1_moves) % 2 

        # IF RANDOM
        elif (self.agent_0.attitude == 'random'):
            return random.randint(0, 1)
        


    def agent1_next_move(self):
        # given the agent attitude and previous moves, determine next move
        # IF TIT FOR TAT
        if (self.agent_1.attitude == 'tit_for_tat'):
            if (len(self.agent_1_moves) == 0):
                return 1
            else:
                return self.agent_0_moves[-1] 

        # IF TESTER
        elif (self.agent_1.attitude == 'tester'):
            if (len(self.agent_0_moves) == 0):     
                return 0
            else:
                if (len(self.agent_0_moves) == 2):
                    # if retaliate 
                    if (self.agent_0_moves[-1] == 0):
                        return 1
                    else:
                        return 0
                else:
                    if (len(self.agent_0_moves) > 1):
                        return self.agent_0_moves[-1]
                    else:
                        return 1

        # IF JOSS
        elif (self.agent_1.attitude == 'joss'):
            if (len(self.agent_1_moves) == 0):
                return 1
            else:
                if (random.randint(1, 10) == 1):
                    return 0
                else:
                    if (len(self.agent_0_moves) >= 1):
                        return self.agent_0_moves[-1] 
                    else:
                        return 1

        # IF TIT FOR TWO TATS
        elif (self.agent_1.attitude == 'tit_for_two_tats'):
            if (len(self.agent_0_moves) >= 2):  
                if (self.agent_0_moves[-1] == 0 and self.agent_0_moves[-2] == 0):
                    return 0
                else:
                    return 1
            else:
                return 1

        # IF CONFRONTATIONAL
        elif (self.agent_1.attitude == 'confrontational'):
            if (len(self.agent_0_moves) == 0):
                return 1
            else:
                return len(self.agent_0_moves) % 2 

        # IF RANDOM
        elif (self.agent_1.attitude == 'random'):
            return random.randint(0, 1)
        

    def print_board(self):
        # print game board
        string = f'                   {self.agent_0.position}\n'
        string += '               COOP         DEFECT\n'
        string += '        --------------------------------\n'
        
        # if developer
        if (self.agent_0.position == 'developer'):
            string += '    CO  | + quality    | + creativity  |\n'
            string += '    OP  |              | - timeliness  |\n'
            string += f'        |--------------|---------------| {self.agent_1.position}\n'
            string += '   DEF  | - creativity | - quality     |\n'
            string += '   ECT  | + timliness  |               |\n'
            string += '        --------------------------------'

        # if manager
        elif (self.agent_0.position == 'manager'):
            string += '    CO  | + timliness  | + quality     |\n'
            string += '    OP  |              | - profit      |\n'
            string += f'        |--------------|---------------| {self.agent_1.position}\n'
            string += '   DEF  | - quality    | - timliness   |\n'
            string += '   ECT  | + profit     |               |\n'
            string += '        --------------------------------'

        # if stakeholder
        elif (self.agent_0.position == 'stakeholder'):
            string += '    CO  | + profit     | + timliness   |\n'
            string += '    OP  |              | - creativity  |\n'
            string += f'        |--------------|---------------| {self.agent_1.position}\n'
            string += '   DEF  | - timliness  | - profit      |\n'
            string += '   ECT  | + creativity |               |\n'
            string += '        --------------------------------'
        
        # if customer
        elif (self.agent_0.position == 'customer'):
            string += '    CO  | + creativity | + profit      |\n'
            string += '    OP  |              | - quality     |\n'
            string += f'        |--------------|---------------| {self.agent_1.position}\n'
            string += '   DEF  | - profit     | - creativity  |\n'
            string += '   ECT  | + quality    |               |\n'
            string += '        --------------------------------'
    
        print(string)
