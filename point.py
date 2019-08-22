class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.directions = []
        self.locations = [[x, y]]
        self.visited = [[x, y]]
    
    def xy(self) :
        return [self.x, self.y]
    
    def N(self) :          
        self.y -= 1
        self.directions += 'N'        
        self.record()
    
    def S(self) :
        self.y += 1
        self.directions += 'S'
        self.record()

    def E(self) :
        self.x += 1
        self.directions += 'E'
        self.record()

    def W(self) :
        self.x -= 1
        self.directions += 'W'
        self.record()

    def set_at(self, index) :       
        self.x = self.locations[index][0]
        self.y = self.locations[index][1]
        self.locations = self.locations[0:index + 1]
        self.directions = self.directions[0:index ]
                
    def record(self) :
        self.locations.append([self.x, self.y])
        self.visited.append([self.x, self.y])

    def get_moves(self) :
        return [self.N, self.S, self.E, self.W]
    
    def clone(self) :
        myclone = Point(self.x, self.y)
        
        for i in self.directions :
            myclone.directions.append(i)
        
        for j in self.locations :
            myclone.locations.append([j[0], j[1]])
            
        for k in self.visited :
            myclone.visited.append([k[0], k[1]])
        
        return myclone
    
    def __str__(self) :
        return '(' + str(self.x) + ',' + str(self.y) + ')'  + self.directions[-1] #+ self.visited