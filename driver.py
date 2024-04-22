
from game import Game
from agent import Agent
import random


if __name__ == '__main__':

    # diverse attitude set
    attitude_set_0 = ['tit_for_tat', 'tester', 'joss', 'tit_for_two_tats', 
                      'confrontational', 'random']

    # forgiving attitude set
    attitude_set_1 = ['tit_for_tat', 'tester', 'tit_for_two_tats', 'joss']

    # confrontational data set
    attitude_set_2 = ['tester', 'confrontational', 'random']

    # ---------------------------------------------------------------------- #

    creativity = []
    timliness = []
    quality = []
    profit = []
     
    for i in range(10):            
        agent_0 = Agent('developer', random.choice(attitude_set_0))
        agent_1 = Agent('manager', random.choice(attitude_set_0))
        game = Game(agent_0, agent_1, 10)
        results = game.do_game()
        creativity.append(results[0])
        timliness.append(results[1])
        quality.append(results[2])
        profit.append(results[3])
    print('\x1b[38;5;202m  ')
    game.print_board()
 
    for i in range(10):            
        agent_0 = Agent('manager', random.choice(attitude_set_0))
        agent_1 = Agent('stakeholder', random.choice(attitude_set_0))
        game = Game(agent_0, agent_1, 10)
        results = game.do_game()
        creativity.append(results[0])
        timliness.append(results[1])
        quality.append(results[2])
        profit.append(results[3])
    print('\x1b[38;5;207m  ')
    game.print_board()
 
    for i in range(10):            
        agent_0 = Agent('stakeholder', random.choice(attitude_set_0))
        agent_1 = Agent('customer', random.choice(attitude_set_0))
        game = Game(agent_0, agent_1, 10)
        results = game.do_game()
        creativity.append(results[0])
        timliness.append(results[1])
        quality.append(results[2])
        profit.append(results[3])
    print('\x1b[38;5;226m  ')
    game.print_board()

    for i in range(10):            
        agent_0 = Agent('customer', random.choice(attitude_set_0))
        agent_1 = Agent('developer', random.choice(attitude_set_0))
        game = Game(agent_0, agent_1, 10)
        results = game.do_game()
        creativity.append(results[0])
        timliness.append(results[1])
        quality.append(results[2])
        profit.append(results[3]) 
    print('\x1b[38;5;40m  ')
    game.print_board()

    # print results
    print('\x1b[38;5;39m  ')
    print(f'     RESULTS with Agent Attitudes -> {attitude_set_0}')
    print(f'        Average Creativity -> {sum(creativity) / len(creativity)}')
    print(f'        Average Timliness  -> {sum(timliness) / len(timliness)}')
    print(f'        Average Quality    -> {sum(quality) / len(quality)}')
    print(f'        Average Profit     -> {sum(profit) / len(profit)}')
    
    # -------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------

    creativity = []
    timliness = []
    quality = []
    profit = []
     
    for i in range(10):            
        agent_0 = Agent('developer', random.choice(attitude_set_0))
        agent_1 = Agent('manager', random.choice(attitude_set_0))
        game = Game(agent_0, agent_1, 10)
        results = game.do_game()
        creativity.append(results[0])
        timliness.append(results[1])
        quality.append(results[2])
        profit.append(results[3])
 
    for i in range(10):            
        agent_0 = Agent('manager', random.choice(attitude_set_1))
        agent_1 = Agent('stakeholder', random.choice(attitude_set_1))
        game = Game(agent_0, agent_1, 10)
        results = game.do_game()
        creativity.append(results[0])
        timliness.append(results[1])
        quality.append(results[2])
        profit.append(results[3])
 
    for i in range(10):            
        agent_0 = Agent('stakeholder', random.choice(attitude_set_1))
        agent_1 = Agent('customer', random.choice(attitude_set_1))
        game = Game(agent_0, agent_1, 10)
        results = game.do_game()
        creativity.append(results[0])
        timliness.append(results[1])
        quality.append(results[2])
        profit.append(results[3])

    for i in range(10):            
        agent_0 = Agent('customer', random.choice(attitude_set_1))
        agent_1 = Agent('developer', random.choice(attitude_set_1))
        game = Game(agent_0, agent_1, 10)
        results = game.do_game()
        creativity.append(results[0])
        timliness.append(results[1])
        quality.append(results[2])
        profit.append(results[3]) 

    # print results
    print('\x1b[38;5;10m  ')
    print(f'     RESULTS with Agent Attitudes -> {attitude_set_1}')
    print(f'        Average Creativity -> {sum(creativity) / len(creativity)}')
    print(f'        Average Timliness  -> {sum(timliness) / len(timliness)}')
    print(f'        Average Quality    -> {sum(quality) / len(quality)}')
    print(f'        Average Profit     -> {sum(profit) / len(profit)}')
    
    # -------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------

    creativity = []
    timliness = []
    quality = []
    profit = []
     
    for i in range(10):            
        agent_0 = Agent('developer', random.choice(attitude_set_2))
        agent_1 = Agent('manager', random.choice(attitude_set_2))
        game = Game(agent_0, agent_1, 10)
        results = game.do_game()
        creativity.append(results[0])
        timliness.append(results[1])
        quality.append(results[2])
        profit.append(results[3])
 
    for i in range(10):            
        agent_0 = Agent('manager', random.choice(attitude_set_1))
        agent_1 = Agent('stakeholder', random.choice(attitude_set_1))
        game = Game(agent_0, agent_1, 10)
        results = game.do_game()
        creativity.append(results[0])
        timliness.append(results[1])
        quality.append(results[2])
        profit.append(results[3])
 
    for i in range(10):            
        agent_0 = Agent('stakeholder', random.choice(attitude_set_1))
        agent_1 = Agent('customer', random.choice(attitude_set_1))
        game = Game(agent_0, agent_1, 10)
        results = game.do_game()
        creativity.append(results[0])
        timliness.append(results[1])
        quality.append(results[2])
        profit.append(results[3])

    for i in range(10):            
        agent_0 = Agent('customer', random.choice(attitude_set_1))
        agent_1 = Agent('developer', random.choice(attitude_set_1))
        game = Game(agent_0, agent_1, 10)
        results = game.do_game()
        creativity.append(results[0])
        timliness.append(results[1])
        quality.append(results[2])
        profit.append(results[3]) 

    # print results
    print('\x1b[38;5;203m  ')
    print(f'     RESULTS with Agent Attitudes -> {attitude_set_2}')
    print(f'        Average Creativity -> {sum(creativity) / len(creativity)}')
    print(f'        Average Timliness  -> {sum(timliness) / len(timliness)}')
    print(f'        Average Quality    -> {sum(quality) / len(quality)}')
    print(f'        Average Profit     -> {sum(profit) / len(profit)}')
