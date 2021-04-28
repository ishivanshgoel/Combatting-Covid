import json

import os
my_absolute_dirpath = os.path.abspath(os.path.dirname(__file__))

class Statesdata:
    def __init__(self):
        statesdata = open(f'{my_absolute_dirpath}/statesdata.json',)
        states = json.load(statesdata)
        self.statesdata = states['states']
    
    # list of states
    def getStates(self):
        data = self.statesdata
        states = []
        for i in range(len(data)):
            states.append(data[i]['state'])
        return states
    
    # list of districts
    def getDistricts(self, state):
        data = self.statesdata
        for i in range(len(data)):
            if(data[i]['state']==state):
                return data[i]['districts']
        # for invalid entry
        return []
            
