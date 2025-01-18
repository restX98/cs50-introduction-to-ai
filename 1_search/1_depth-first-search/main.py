from typing import List


class Node:
    def __init__(self, state, parent, action):
        """Initialize a Node with state, parent and action"""
        self.state = state
        self.parent = parent
        self.action = action


class Frontier:
    def __init__(self):
        """Initialize a Frontier"""
        self.frontier = []

    def add(self, node: Node):
        self.frontier.append(node)

    def remove(self) -> Node:
        return self.frontier.pop()

    def is_empty(self) -> bool:
        return len(self.frontier) == 0

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)


class Maze:
    def __init__(self, filepath):
        self.actions = {
            "up": lambda cordx: (cordx[0] - 1, cordx[1]),
            "down": lambda cordx: (cordx[0] + 1, cordx[1]),
            "left": lambda cordx: (cordx[0], cordx[1] - 1),
            "right": lambda cordx: (cordx[0], cordx[1] + 1),
        }

        with open(filepath) as file:
            maze = file.read()

        if maze.count("A") != 1:
            raise Exception("maze must have exactly one start point")
        if maze.count("B") != 1:
            raise Exception("maze must have exactly one goal")

        rows = maze.splitlines()
        self.height = len(rows)
        self.width = max(len(row) for row in rows)

        self.wall = []
        for i in range(self.height):
            self.wall.append([])
            for ii in range(self.width):
                char = rows[i][ii]
                if char == "#":
                    self.wall[i].append(True)
                elif char == "A":
                    self.start = (i, ii)
                    self.wall[i].append(False)
                elif char == "B":
                    self.goal = (i, ii)
                    self.wall[i].append(False)
                elif char == " ":
                    self.wall[i].append(False)
                else:
                    raise Exception("Maze not valid!")

    def starting_node(self) -> Node:
        if hasattr(self, "starting_node"):
            self.starting_node = Node(self.start, None, None)
        return self.starting_node

    def neighbors(self, node: Node) -> List[Node]:
        eligible = []
        for action, callback in self.actions.items():
            (r, c) = callback(node.state)
            # TODO: replace wall array with bool matrix to avoid continuous iteration on it
            if 0 <= r < self.height and 0 <= c < self.width and not self.wall[r][c]:
                eligible.append(Node((r, c), node, action))

        return eligible

    def print(self, solution):
        solution = solution[0] if solution is not None else None
        print()
        for i, row in enumerate(self.wall):
            for j, col in enumerate(row):
                if col:
                    print("#", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def output_image(
        self, solution, filename="maze.png", show_solution=True, show_explored=False
    ):
        from PIL import Image, ImageDraw

        cell_size = 50
        cell_border = 2

        # Create a blank canvas
        img = Image.new(
            "RGBA", (self.width * cell_size, self.height * cell_size), "black"
        )
        draw = ImageDraw.Draw(img)

        solution = solution if solution is not None else None
        for i, row in enumerate(self.wall):
            for j, col in enumerate(row):
                # Walls
                if col:
                    fill = (40, 40, 40)

                # Start
                elif (i, j) == self.start:
                    fill = (255, 0, 0)

                # Goal
                elif (i, j) == self.goal:
                    fill = (0, 171, 28)

                # Solution
                elif solution is not None and show_solution and (i, j) in solution[0]:
                    fill = (0, 0, 255)

                # Explored
                elif solution is not None and show_explored and (i, j) in solution[2]:
                    fill = (255, 128, 0)

                # Empty cell
                else:
                    fill = (237, 240, 252)

                # Draw cell
                draw.rectangle(
                    (
                        [
                            (j * cell_size + cell_border, i * cell_size + cell_border),
                            (
                                (j + 1) * cell_size - cell_border,
                                (i + 1) * cell_size - cell_border,
                            ),
                        ]
                    ),
                    fill=fill,
                )

        img.save(filename)


class MazeSolver:
    def __init__(self, maze: Maze):
        self.maze = maze
        self.frontier = Frontier()

    def solve(self):
        # Init explored list
        self.explored = []

        # Addind starting node
        self.frontier.add(self.maze.starting_node())

        while True:
            # 1. If the frontier is empty:
            if self.frontier.is_empty():
                # Stop. There is no solution to the problem.
                return "No solution found"

            # 2. Remove a node from the frontier.
            #    This is the node that will be considered.
            node = self.frontier.remove()

            # 3. If the node contains the goal state:
            if node.state == maze.goal:
                path = []
                actions = []
                while node.parent is not None:
                    path.append(node.state)
                    actions.append(node.action)
                    node = node.parent
                # Add initial node
                path.append(node.state)
                actions.append(node.action)

                path.reverse()
                actions.reverse()
                self.solution = (path, actions, self.explored)
                return
            else:
                # Expand the node (find all the new nodes that could be reached from this node), and add resulting nodes to the frontier.
                for neighbor in self.maze.neighbors(node):
                    if (
                        not self.frontier.contains_state(neighbor.state)
                        and neighbor.state not in self.explored
                    ):
                        self.frontier.add(neighbor)

                # Add the current node to the explored set.
                self.explored.append(node.state)


if __name__ == "__main__":
    filenames = ["maze", "maze1", "maze2", "maze3"]
    prj_path = "./1_search/1_depth-first-search/"

    for filename in filenames:
        maze = Maze(f"{prj_path}mazes/{filename}.txt")
        maze.print(None)

        solver = MazeSolver(maze)
        solver.solve()
        maze.print(solver.solution)
        maze.output_image(
            solver.solution, f"{prj_path}plots/{filename}.png", True, True
        )
