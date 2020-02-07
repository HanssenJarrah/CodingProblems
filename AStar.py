"""
You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall.
Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach
the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and
right. You cannot move through walls. You cannot wrap around the edges of the board.

A* DOES NOT GUARANTEE THE SHORTEST PATH
"""
start_pos = (3, 0)
end_pos = (0, 0)
a_star_maze = [[0, 0, 0, 0],
               [1, 1, 0, 1],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]


class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __str__(self):
        return str(self.position) + " at " + str(self.g)


def a_star(maze, start, end):
    start_node = Node(None, start)
    end_node = Node(None, end)

    # Open and closed list of nodes:
    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:
        # Find the node in open with the lowest f value and move it to closed
        current_node = open_list[0]
        current_index = 0
        for i, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = i
        open_list.pop(current_index)
        closed_list.append(current_node)

        # If the current node is the end node, the path has been found
        if current_node == end_node:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        # Find all children of the current node that are not walls or outside maze bounds
        children = []
        adjacent_poses = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for new_position in adjacent_poses:
            node_pos = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # If the new node is outside of the bounds of the maze
            if node_pos[0] > (len(maze) - 1) or node_pos[0] < 0 or node_pos[1] > (len(maze[0]) - 1) or node_pos[1] < 0:
                continue

            # If the new node position is a wall, don't add it to children
            if not maze[node_pos[0]][node_pos[1]]:
                continue

            new_node = Node(current_node, node_pos)
            children.append(new_node)

        # Check the each child node to see if they are appropriate to add to the open list
        for child in children:
            # Check that the child is not in the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Set the child's heuristic g, h and f values
            child.g = current_node.g + 1
            child.h = (current_node.position[0] - end_node.position[0])**2 + \
                      (current_node.position[1] - end_node.position[1])**2
            child.f = child.g + child.h

            # Check the same node on a shorter path isn't currently in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # If all this is fine, append the child to the open list
            open_list.append(child)


def main():
    result = a_star(a_star_maze, start_pos, end_pos)
    print(result)


if __name__ == "__main__":
    main()












