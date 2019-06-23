import requests
import json
import math

class Maze():
    def __init__(self, maze, A, B):
        self.w = len(maze)
        self.h = len(maze[0])
        self.maze = maze
        self.start = (A[1], A[0])
        self.goal = (B[1], B[0])
        self.open = [(self.start[0], self.start[1], 0)]
        self.closed = []
        self.path = ""

    def heuristic(self, x, y):
        return math.sqrt((self.goal[0] - x) ** 2 + (self.goal[1] - y) ** 2)

    def addToOpen(self, node, path):
        g = len(self.path) + 1
        h = self.heuristic(node[0], node[1])
        f = g + h
        self.open.append((node.x, node.y, f))

    def removeFromOpen(self):
        least_f = self.open[0][2]
        candidate = None
        for node in self.open:
            if least_f >= node[2]:
                least_f = node[2]
                candidate = node
        return candidate

                 
    def assertBounds(self, value):
        try:
            if value[0] >= 0 and value[1] >= 0 and value[0] < self.h and value[1] < self.w:
                return True
        except:
            return False
        return False

    def findNeighbors(self, pos):
        total = []

        if self.assertBounds([pos[0] - 1, pos[1]]):
            N = self.maze[pos[0] - 1][pos[1]]
            if N == ' ':
                total.append("N")
        if self.assertBounds([pos[0], pos[1] - 1]):
            W = self.maze[pos[0]][pos[1] - 1]
            if W == ' ':
                total.append("W")
        if self.assertBounds([pos[0] + 1, pos[1]]):
            S = self.maze[pos[0] + 1][pos[1]]
            if S == ' ':
                total.append("S")
        if self.assertBounds([pos[0], pos[1] + 1]):
            E = self.maze[pos[0]][pos[1] + 1]
            if E == ' ':
                total.append("E")

        # print("N: {} W: {} S: {} E: {}".format(N, W, S, E))

        return total

    def showMaze(self):
        print(self.start)
        for i in range(len(self.maze)):
            print(self.maze[i])

    def solve(self):
        while self.open:
            q = self.removeFromOpen()
            self.open.remove(q)
            possibleMoves = self.findNeighbors((q[0], q[1]))
            for move in possibleMoves:
                if move == 'N':
                    N = (pos[0] - 1, pos[1], f)
                

            print(possibleMoves)



data = json.loads(requests.get(
    "https://api.noopschallenge.com/mazebot/random?maxSize=10").content.decode("utf-8"))

print(data)
maze = Maze(data["map"], data["startingPosition"], data["endingPosition"])
maze.showMaze()
maze.findNeighbors(maze.start)
maze.solve()