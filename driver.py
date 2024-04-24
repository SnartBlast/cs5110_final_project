
from game import Game
from agent import Agent
import random


if __name__ == '__main__':

    # diverse attitude set
    attitude_set_0 = ['tit_for_tat', 'tester', 'joss', 'tit_for_two_tats', 
                      'confrontational', 'random', 'always_d', 'yes_man', 'trusting']

    # forgiving attitude set
    attitude_set_1 = ['tit_for_tat', 'trusting', 'tit_for_two_tats', 'joss', 'yes_man']

    # confrontational data set
    attitude_set_2 = ['tester', 'confrontational', 'random', 'always_d']

    # ---------------------------------------------------------------------- #

    creativity = []
    timliness = []
    quality = []
    profit = []
     
    for i in range(100):            
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
 
    for i in range(100):            
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
 
    for i in range(100):            
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

    for i in range(100):            
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
    avg_create = sum(creativity) / len(creativity)
    avg_time = sum(timliness) / len(timliness)
    avg_quality = sum(quality) / len(quality)
    avg_profit = sum(profit) / len(profit)
    print('\x1b[38;5;39m  ')
    print('     RESULTS with Diverse Agent Attitudes')
    print(f'     {attitude_set_0}\n')
    print(f'        Average Creativity -> {avg_create}')
    print(f'        Average Timliness  -> {avg_time}')
    print(f'        Average Quality    -> {avg_quality}')
    print(f'        Average Profit     -> {avg_profit}')
    print(f'                     Total -> {round(avg_create + avg_time + avg_quality + avg_profit, 4)}')
    
    # -------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------

    creativity = []
    timliness = []
    quality = []
    profit = []
     
    for i in range(100):            
        agent_0 = Agent('developer', random.choice(attitude_set_1))
        agent_1 = Agent('manager', random.choice(attitude_set_1))
        game = Game(agent_0, agent_1, 10)
        results = game.do_game()
        creativity.append(results[0])
        timliness.append(results[1])
        quality.append(results[2])
        profit.append(results[3])
 
    for i in range(100):            
        agent_0 = Agent('manager', random.choice(attitude_set_1))
        agent_1 = Agent('stakeholder', random.choice(attitude_set_1))
        game = Game(agent_0, agent_1, 10)
        results = game.do_game()
        creativity.append(results[0])
        timliness.append(results[1])
        quality.append(results[2])
        profit.append(results[3])
 
    for i in range(100):            
        agent_0 = Agent('stakeholder', random.choice(attitude_set_1))
        agent_1 = Agent('customer', random.choice(attitude_set_1))
        game = Game(agent_0, agent_1, 10)
        results = game.do_game()
        creativity.append(results[0])
        timliness.append(results[1])
        quality.append(results[2])
        profit.append(results[3])

    for i in range(100):            
        agent_0 = Agent('customer', random.choice(attitude_set_1))
        agent_1 = Agent('developer', random.choice(attitude_set_1))
        game = Game(agent_0, agent_1, 10)
        results = game.do_game()
        creativity.append(results[0])
        timliness.append(results[1])
        quality.append(results[2])
        profit.append(results[3]) 

    # print results
    avg_create = sum(creativity) / len(creativity)
    avg_time = sum(timliness) / len(timliness)
    avg_quality = sum(quality) / len(quality)
    avg_profit = sum(profit) / len(profit)
    print('\x1b[38;5;10m  ')
    print('     RESULTS with Collaborative Agent Attitudes')
    print(f'     {attitude_set_1}\n')
    print(f'        Average Creativity -> {avg_create}')
    print(f'        Average Timliness  -> {avg_time}')
    print(f'        Average Quality    -> {avg_quality}')
    print(f'        Average Profit     -> {avg_profit}')
    print(f'                     Total -> {round(avg_create + avg_time + avg_quality + avg_profit, 4)}')
       
    # -------------------------------------------------------------------------------------
    # -------------------------------------------------------------------------------------

    creativity = []
    timliness = []
    quality = []
    profit = []
     
    for i in range(100):            
        agent_0 = Agent('developer', random.choice(attitude_set_2))
        agent_1 = Agent('manager', random.choice(attitude_set_2))
        game = Game(agent_0, agent_1, 10)
        results = game.do_game()
        creativity.append(results[0])
        timliness.append(results[1])
        quality.append(results[2])
        profit.append(results[3])
 
    for i in range(100):            
        agent_0 = Agent('manager', random.choice(attitude_set_2))
        agent_1 = Agent('stakeholder', random.choice(attitude_set_2))
        game = Game(agent_0, agent_1, 10)
        results = game.do_game()
        creativity.append(results[0])
        timliness.append(results[1])
        quality.append(results[2])
        profit.append(results[3])
 
    for i in range(100):            
        agent_0 = Agent('stakeholder', random.choice(attitude_set_2))
        agent_1 = Agent('customer', random.choice(attitude_set_2))
        game = Game(agent_0, agent_1, 10)
        results = game.do_game()
        creativity.append(results[0])
        timliness.append(results[1])
        quality.append(results[2])
        profit.append(results[3])

    for i in range(100):            
        agent_0 = Agent('customer', random.choice(attitude_set_2))
        agent_1 = Agent('developer', random.choice(attitude_set_2))
        game = Game(agent_0, agent_1, 10)
        results = game.do_game()
        creativity.append(results[0])
        timliness.append(results[1])
        quality.append(results[2])
        profit.append(results[3]) 

    # print results
    avg_create = sum(creativity) / len(creativity)
    avg_time = sum(timliness) / len(timliness)
    avg_quality = sum(quality) / len(quality)
    avg_profit = sum(profit) / len(profit)
    print('\x1b[38;5;203m  ')
    print('     RESULTS with Confrontational Agent Attitudes')
    print(f'     {attitude_set_2}\n')
    print(f'        Average Creativity -> {avg_create}')
    print(f'        Average Timliness  -> {avg_time}')
    print(f'        Average Quality    -> {avg_quality}')
    print(f'        Average Profit     -> {avg_profit}')
    print(f'                     Total -> {round(avg_create + avg_time + avg_quality + avg_profit, 4)}')
