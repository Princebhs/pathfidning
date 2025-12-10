import os
from collections import deque

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

ROWS = 10
COLS = 10

# Grid with obstacles (1 = obstacle)
grid = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,1,1,1,0,0,0,1,1,0],
    [0,0,0,1,0,1,0,0,1,0],
    [0,1,0,0,0,1,0,0,0,0],
    [0,1,0,1,0,0,0,1,0,0],
    [0,0,0,1,0,0,1,1,0,0],
    [0,1,0,0,0,1,0,0,0,0],
    [0,1,1,1,0,1,0,1,1,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,0,1,0,0,0]
]

start = (0, 0)
goal = (9, 9)

def draw(grid, path=None):
    clear()
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) == start:
                print("P", end=" ")
            elif (r, c) == goal:
                print("G", end=" ")
            elif path and (r, c) in path:
                print("*", end=" ")
            elif grid[r][c] == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

def bfs(start, goal):
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        r, c = queue.popleft()

        if (r, c) == goal:
            break

        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < ROWS and 0 <= nc < COLS:
                if grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    parent[(nr, nc)] = (r, c)
                    queue.append((nr, nc))

    # Reconstruct path
    if goal not in parent:
        return None  # no path found

    path = []
    cur = goal
    while cur:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path

path = bfs(start, goal)
draw(grid, path)

if path:
    print("Path found!")
    print(path)
else:
    print("No path available.")
