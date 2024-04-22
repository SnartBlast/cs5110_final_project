
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
        if (self.agent_0.positon == 'developer'):

        elif (self.agent_0.position == 'manager'):

        elif (self.agent_0.position == 'stakeholder'):

        elif (self.agent_0.position == 'customer'):
        
        

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
