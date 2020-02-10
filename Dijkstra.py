"""
You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall.
Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach
the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and
right. You cannot move through walls. You cannot wrap around the edges of the board.

This solution uses an implementation of Dijkstra's algorithm.
"""
import heapq
import pygame as pg
import sys
from pygame.rect import Rect

SCALE = 100
FONT_SCALE = 0.33
bg_colour = (255, 255, 255)
wall_colour = font_colour = (0, 0, 0)
path_colour = (0, 0, 255)
node_colour = (0, 255, 0)


"""
start_pos = (3, 0)
end_pos = (0, 0)
dijkstra_maze = [[0, 0, 0, 0],
                 [1, 1, 0, 1],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]"""


start_pos = (5, 0)
end_pos = (5, 5)
dijkstra_maze = [[0, 0, 0, 0, 0, 1],
                 [1, 1, 0, 1, 0, 1],
                 [0, 0, 0, 1, 0, 0],
                 [0, 1, 1, 0, 0, 1],
                 [0, 1, 0, 0, 1, 1],
                 [0, 1, 0, 0, 0, 0]]


class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.dist = 0  # Number of nodes from the start point

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.dist < other.dist

    def __gt__(self, other):
        return self.dist > other.dist

    def __str__(self):
        return str(self.position) + " at " + str(self.dist)


def dijkstra(maze, start, end):
    start_node = Node(None, start)
    end_node = Node(None, end)

    # Heapq will use the first element of the tuple as the custom sorting element
    open_heap = [start_node]
    closed_list = []

    while len(open_heap) > 0:
        # Get the first item from the heap
        current_node = heapq.heappop(open_heap)
        closed_list.append(current_node)

        # If the current node is the end node, the best path has been found
        if current_node == end_node:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        # Find all children of the current node that are not walls or outside maze bounds
        adjacent_poses = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for new_pos in adjacent_poses:
            invalid = False
            node_pos = (current_node.position[0] + new_pos[0], current_node.position[1] + new_pos[1])

            # If the new node is outside of the bounds of the maze
            if node_pos[0] > (len(maze) - 1) or node_pos[0] < 0 or node_pos[1] > (len(maze[0]) - 1) or node_pos[1] < 0:
                continue

            # If the new node is a wall, ignore it
            if maze[node_pos[0]][node_pos[1]]:
                continue

            # If the node already exists in the open list:
            for open_node in open_heap:
                if open_node.position == node_pos:
                    invalid = True
                    break
            if invalid:
                continue

            # If the node already exists in the closed list (it can only be in the closed list if it has the same
            # or a lesser dist value):
            for closed_node in closed_list:
                if closed_node.position == node_pos:
                    invalid = True
                    break
            if invalid:
                continue

            new_node = Node(current_node, node_pos)
            new_node.dist = current_node.dist + 1
            open_heap.append(new_node)

        # Resort the heap with the new nodes in it
        heapq.heapify(open_heap)

    # No path from start to end
    print("Cannot find path")
    return None


def get_pos_rect(row, column):
    x = row * SCALE
    y = column * SCALE
    new_rect = Rect(x, y, SCALE, SCALE)
    return new_rect


def draw_maze(result=None):
    if result is None:
        result = []

    # Generating the pygame maze graphic
    pg.init()
    size = width, height = len(dijkstra_maze[0]) * SCALE, len(dijkstra_maze) * SCALE
    screen = pg.display.set_mode(size)
    screen.fill(bg_colour)

    # Drawing the path to the screen:
    for i, row in enumerate(dijkstra_maze):
        for j, val in enumerate(row):
            if val:
                pg.draw.rect(screen, wall_colour, get_pos_rect(j, i))

    for pos in result:
        pg.draw.rect(screen, path_colour, get_pos_rect(pos[1], pos[0]))

    if result:
        pg.draw.rect(screen, node_colour, get_pos_rect(start_pos[1], start_pos[0]))
        pg.draw.rect(screen, node_colour, get_pos_rect(end_pos[1], end_pos[0]))

        # Marking the start and end of the maze
        fnt = pg.font.SysFont("ariel", int(SCALE * FONT_SCALE))

        start_text = fnt.render("Start", True, font_colour)
        start_x = int(start_pos[1] * SCALE + SCALE / 2 - start_text.get_width() / 2)
        start_y = int(start_pos[0] * SCALE + SCALE / 2 - start_text.get_height() / 2)
        screen.blit(start_text, (start_x, start_y))

        end_text = fnt.render("End", True, font_colour)
        end_x = int(end_pos[1] * SCALE + SCALE / 2 - end_text.get_width() / 2)
        end_y = int(end_pos[0] * SCALE + SCALE / 2 - end_text.get_height() / 2)
        screen.blit(end_text, (end_x, end_y))

    # Drawing the maze to screen
    pg.display.update()


def main():
    result = dijkstra(dijkstra_maze, start_pos, end_pos)
    print("Path:")
    print(result)

    draw_maze(result)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()


if __name__ == "__main__":
    main()
