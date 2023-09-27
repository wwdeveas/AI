class Problem:
    def __init__ (self):
        #fill in with cities and distances not ABC and nums
        #to actuall make go call after def in other file
        self.graph = {'Chicago': ['Indianapolis': 182, 'Cleveland': 345, 'Detroit': 283], 'Indianapolis': ['Columbus': 176], 
                      'Cleveland': ['Detroit': 169, ], 'D': [], 'E': ['F':3], 'F': [] }
        
        self.start = 'Chicago'
        self.goal = ['Boston']
    def initialState (self):
        return self.start
    def isGoal (self, node):
        return node in self.goal
    def transition (self, node):
        return self.graph[node]
    