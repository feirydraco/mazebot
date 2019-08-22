class Solver :
    def __init__(self, maze) :
        self.maze = maze #col x row  (like x,y)

    def display_maze(self, point=None):
        mymap = '\n'
        i = 0
        for row in self.maze['map']:
            j = 0    
            for cell in row :
                if point != None and [j,i] in point.locations and cell != 'A' and cell != 'B' : mymap += ' ='
                else:  
                    if cell == ' ': mymap += '_|'
                    else: mymap += ' ' + cell
                j += 1
            mymap += '\n'
            i += 1
        print(mymap)

    def solve(self, point, visualize=False, verbose=False, silent=False,  iterations=-1) :
        open_nodes = []
        closed_nodes = []
        while point.xy != self.maze['endingPosition'] :
            
            
            #neighbors ^v><^v><^v><^v><^v><^v><^v><^v><^v><^v><^v><^v><^v><
                #<TOP SECRET CODE>
            
            #move forward >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                #<TOP SECRET CODE>
            
            #backtrack <<<<<<<<<<<<<<<<<<<<<<<<<
                #<TOP SECRET CODE>
            
            #feedback ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                #<TOP SECRET CODE>
        
        #output ==================================>
            #<TOP SECRET CODE>
            
        return point.directions
    
