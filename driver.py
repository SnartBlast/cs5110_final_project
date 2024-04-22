
from game import Game
from agent import Agent


if __name__ == '__main__':
    print('here!')
    agent_0 = Agent('developer', 'trusting')
    agent_1 = Agent('manager', 'trusting')
    agent_2 = Agent('stakeholder', 'trusting')
    agent_3 = Agent('customer', 'trusting')


    game_0 = Game(agent_0, agent_1)  
    game_1 = Game(agent_1, agent_2)  
    game_2 = Game(agent_2, agent_3)  
    game_3 = Game(agent_3, agent_0)  
    game_0.print_board()
    game_1.print_board()
    game_2.print_board()
    game_3.print_board()
     
