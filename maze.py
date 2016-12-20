import re

grid  = [[1,1,1,1,1,1,1,1],
         [1,0,3,0,0,0,1,1],
         [1,1,1,0,0,0,1,1],
         [1,0,0,0,1,0,0,1],
         [1,0,1,1,0,0,1,1],
         [1,0,1,0,0,1,0,1],
         [1,0,1,0,0,0,2,1],
         [1,1,1,1,1,1,1,1]]

def right():
    xpos, ypos = findplayer()
    if grid[xpos + 1][ypos] == 0:
        grid[xpos + 1][ypos] = 3
        grid[xpos][ypos] = 0
        printgrid()
    elif grid[xpos + 1][ypos] == 2:
        printgrid()
        print 'YOU WON'
    else:
        printgrid()
        print 'CANNOT MOVE'

def left():
    xpos, ypos = findplayer()
    if grid[xpos - 1][ypos] == 0:
        grid[xpos - 1][ypos] = 3
        grid[xpos][ypos] = 0
        printgrid()
    elif grid[xpos - 1][ypos] == 2:
        printgrid()
        print 'YOU WON'
    else:
        printgrid()
        print 'CANNOT MOVE'

def up():
    xpos, ypos = findplayer()
    if grid[xpos][ypos + 1] == 0:
        grid[xpos][ypos + 1] = 3
        grid[xpos][ypos] = 0
        printgrid()
    elif grid[xpos][ypos + 1] == 2:
        printgrid()
        print 'YOU WON'
    else:
        printgrid()
        print 'CANNOT MOVE'

def down():
    xpos, ypos = findplayer()
    if grid[xpos][ypos - 1] == 0:
        grid[xpos][ypos - 1] = 3
        grid[xpos][ypos] = 0
        printgrid()
    elif grid[xpos][ypos - 1] == 2:
        printgrid()
        print 'YOU WON'
    else:
        printgrid()
        print 'CANNOT MOVE'


def printgrid():
    for x in grid:
         print num_to_ascii(''.join(str(y) for y in x))
    

def findplayer():
    for x in grid:
        if 3 in x:
            return grid.index(x), x.index(3)

def exportgrid(filename='maze'):
    positions = ''
    for x in grid:
        for y in x:
            positions += str(y)
        positions += '\n'

    positions = num_to_ascii(positions)

    # write to file
    f = open(filename, 'w')
    f.write(positions)
    f.close

def importgrid(filename='maze'):
    grid = []
    with open(filename, 'r') as f:
        for line in f:
            xposition = ascii_to_num(line)
            newlist = list(xposition)
            newlist = [x for x in newlist if x != '\n']
            grid.append(newlist)
    
    grid = [x for x in grid if x != []]
    
def ascii_to_num(positions):
    positions = re.sub(' ', '0', positions)
    positions = re.sub('#', '1', positions)
    positions = re.sub('X', '2', positions)
    positions = re.sub('\.', '3', positions)
    return positions

def num_to_ascii(positions):
    'draw in a more visible way'
    positions = re.sub('0', ' ', positions)
    positions = re.sub('1', '#', positions)
    positions = re.sub('2', 'X', positions)
    positions = re.sub('3', '.', positions)
    return positions
    
