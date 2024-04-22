

class Agent():
    def __init__(self, position, attitude):
        self.position = position
        self.attitude = attitude 
        self.prev_moves = []    

    # agent attitude types
    #   
    #   trusting -> if the opposing agent has cooperated the past two times, cooperate
    #   tit_for_tat -> cooperate on the first round, then do whatever the opponent did last
    #   tester -> defect on the first move, if opponent retaliates, cooperate rest of time
    #   joss -> tit_for_tat, but %10 of the time, defect instead of cooporating
    #   tit_for_two_tats -> defect only when the opponent has defected twice in a row
    #   confrontational -> defect every second turn
    #   random -> randomly choose to defect or cooperate 
