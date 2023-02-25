from collections import deque

def parseMaze(input_file):

    maze = []
    vert = False

    # Open the file in read mode
    with open(input_file, 'r') as file:
        for line in file:

            newLine = []

            if vert == False:

                newLine.append("x")
                walls = line.split('+')
                walls = walls[1:-1]

                for cell in walls:
                    if cell == "---":
                        newLine.append("x")
                        newLine.append("x")
                    else:
                        newLine.append(0)
                        newLine.append("x")

                vert = True

            else:
                cells = line[0:163:2]

                for cell in cells:
                    if cell == "|":
                        newLine.append("x")
                    elif cell == " ":
                        newLine.append(str(0))
                    elif cell == "/":
                        newLine.append(str(0))
                    elif int(cell) > 0 and int(cell) < 10:
                        newLine.append(str(cell))

                vert = False
            
            maze.append(newLine)   

    return maze

def _get_neighbors(maze, cell):
    moves = [
        (-1,0),
        (1,0),
        (0,1),
        (0,-1)
    ]

    neighbors = []

    for move in moves:
        if len(maze) >= cell[0]+move[0] and cell[0]+move[0] > 0:
            if len(maze[cell[0]+move[0]]) >= cell[1]+move[1] and cell[1]+move[1] > 0:
                neighbor = (cell[0]+move[0],cell[1]+move[1])
                neighbors.append(neighbor)
            
    return neighbors

def _is_valid_move(maze, neighbor):
    if(len(maze) > neighbor[0] and len(maze[neighbor[0]]) > neighbor[1]):
        if maze[neighbor[0]][neighbor[1]] != "x":
            return True
        else:
            return False
    else:
        return False
    
def _reconstruct_path(maze, path, start, end):
    current_cell = end
    path_list = [current_cell]

    while current_cell != start:
        current_cell = path[current_cell]
        path_list.append(current_cell)

    path_list.reverse()

    return path_list

def solve(maze, start, end):
    # start = (0,1)
    # end = (20,20)

    visited = set()

    queue = deque()

    queue.append(start)

    path = {start: None}

    while queue:
        current_cell = queue.popleft()

        if current_cell == end:
            return _reconstruct_path(maze, path, start, end)
            print("Solved!")
        
        visited.add(current_cell)

        neighbors = _get_neighbors(maze, current_cell)

        for neighbor in neighbors:
                if neighbor not in visited and _is_valid_move(maze, neighbor):
                    queue.append(neighbor)
                    path[neighbor] = current_cell

    return None

def calculateTotal(maze, path):
    total = 0
    for node in path:
        value = int(maze[node[0]][node[1]])
        total = value + total

    return total


start = (0,1)
end = (1999,80)

# Call the function with the input file name
maze = parseMaze('maze.txt')

# for line in maze:
#     print(line)

soln = solve(maze, start, end)
total = calculateTotal(maze, soln)

print(soln)
print(total)