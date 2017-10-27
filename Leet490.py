
def MazeSolver(maze, src, dst):
    """
    type maze: List[List[int]]
    type src, dst: (int,int)
    """
    rows, cols  = len(maze), len(maze[0])
    if not rows:
        return False
    #BFS search to find all possible reachable points
    row_delta, col_delta = (-1, 1, 0, 0), (0, 0, -1, 1,)
    directions = {}
    for each in zip(row_delta, col_delta, ("u", "d", "l", "r")): # up, down, left, right
        directions[each[2]] = each[0:2]

    cand = [src]
    reach_dict = [[{} for i in xrange(cols)] for j in xrange(rows)]
    explored = [[0 for i in xrange(cols)] for j in xrange(rows)]

    def dirSearch(direction, src):
        if direction in reach_dict[src[0]][src[1]]:
            return reach_dict[src[0]][src[1]][direction]
        delta = directions[direction]
        
        if src[0]+delta[0] < 0 or src[0]+delta[0] > rows-1 or src[1]+delta[1] < 0 or src[1]+delta[1] > cols-1 or maze[src[0]+delta[0]][src[1]+delta[1]] == 1:
           return src
        else:
            temp = dirSearch(direction, (src[0]+delta[0],src[1]+delta[1]))
            reach_dict[src[0]][src[1]][direction] = temp
            return temp
    while len(cand):
        new_cand = []
        for each in cand:
            explored[each[0]][each[1]] = 1
            for direction in ("u", "d", "l", "r"):
                temp = dirSearch(direction, each)
                if temp == dst:
                    return True
                if temp == src:
                    continue
                if not explored[temp[0]][temp[1]]:
                    new_cand.append(temp)
        cand = new_cand 
    return False
            
maze = [ [0,0,1,0,0],[0, 0, 0, 0, 0],[0, 0, 0, 1, 0],[1, 1, 0, 1, 1],[0, 0, 0, 0, 0]]
src = (0,4)
dst = (3,2)
print MazeSolver(maze, src, dst)
   


    

