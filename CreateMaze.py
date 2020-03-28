# File: CreateMaze.py

from mazelib import Maze
from pgl import GWindow
import random

GWINDOW_WIDTH = 500
GWINDOW_HEIGHT = 300
MAZE_ROWS = 5
MAZE_COLS = 9
SQUARE_SIZE = 36

def CreateMaze():
    g = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    maze = Maze(MAZE_ROWS, MAZE_COLS, SQUARE_SIZE)
    x = (g.getWidth() - maze.getWidth()) / 2
    y = (g.getHeight() - maze.getHeight()) / 2
    createRandomMaze(maze)
    g.add(maze, x, y)

def createRandomMaze(maze):
    walls = maze.getWalls()
    random.shuffle(walls)
    for wall in walls:
        sq1,sq2 = wall.getSquares()
        g1 = find(sq1)
        g2 = find(sq2)
        if g1 == g2:
            wall.setColor("Black")
        else:
            wall.setColor("White")
            union(sq1, sq2)

def find(node):
    """Returns the representative of the set to which node belongs."""
    current_node = node
    while current_node._link: #while we have a parent, go to the next parent
	current_node = current_node.getLink()
    return current_node

def union(n1,n2):
    """Combines the sets containing these nodes into a single set."""
    rep1 = find(n1) #find the representative for each desired node
    rep2 = find(n2)
    #check the depth of each set to decide which to merge, merge smaller set with larger
    if rep1._rank < rep2._rank: #added rank variable to determine depth of set
        rep1._link = rep2
    elif rep2._rank < rep1._rank:
        rep2._link = rep1
    #if they're the same size, make one arbitrary set the parent, and increase rank by one. (adapted from CLRS, p. 571)
    elif rep1._rank == rep2._rank:
        rep2._link = rep1
        rep2._rank += 1

def randomColor():
    """
    Returns a random opaque color expressed as a string consisting
    of a "#" followed by six random hexadecimal digits.
    """
    str = "#"
    for i in range(6):
        str += random.choice(["0", "1", "2", "3", "4", "5", "6", "7",
                              "8", "9", "A", "B", "C", "D", "E", "F"])
    return str

# Startup code

if __name__ == "__main__":
    CreateMaze()
