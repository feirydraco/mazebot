import urllib, json, urllib.request, numpy as np
from point import Point
from solver import Solver

baseurl = "https://api.noopschallenge.com"

def get_maze(qurl=baseurl+'/mazebot/random'):
    with urllib.request.urlopen(qurl) as url:
        question = json.loads(url.read().decode())
        return question
def post(qurl, qanswer) :
    head={'Content-Type': 'application/json'}
    
    answer = qanswer.encode('utf8')
    
    try :
        req = urllib.request.Request(qurl, data=answer, headers=head)
        res = urllib.request.urlopen(req)
        response = json.load(res)

        return response
    
    except urllib.error.HTTPError as e:
        response = json.load(e)
        return response


if __name__ == '__main__':
    # maze = get_maze() #use to get random maze
    #saved instance of a maze
    maze = {'name': 'Maze #147 (10x10)', 'mazePath': '/mazebot/mazes/IE31RerHgi4hw2MrTCJjXdxvDkbJiUjTQ-YeqQiRRTU', 'startingPosition': [8, 9], 'endingPosition': [4, 6], 'message': 'When you have figured out the solution, post it back to this url in JSON format. See the exampleSolution for more information.', 'exampleSolution': {'directions': 'ENWNNENWNNS'}, 'map': [['X', 'X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', 'X', ' ', ' ', 'X', ' ', 'X', 'X', ' '], [' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', 'X', ' '], [' ', ' ', 'X', 'X', 'X', ' ', 'X', ' ', ' ', ' '], ['X', ' ', 'X', ' ', ' ', ' ', 'X', ' ', 'X', ' '], [' ', ' ', 'X', 'X', 'X', 'X', 'X', ' ', ' ', ' '], ['X', ' ', 'X', ' ', 'B', ' ', 'X', ' ', 'X', ' '], [' ', ' ', 'X', 'X', 'X', ' ', 'X', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', 'X', ' '], [' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ', 'A', ' ']]}
    for key, value in maze.items():
        print("{}: {}".format(key, value))
    solver_obj = Solver(maze)
    solver_obj.display_maze()
    start_x, start_y = maze['startingPosition'][0], maze['startingPosition'][1]
    Solver = Point(start_x, start_y)
    print(Solver)


