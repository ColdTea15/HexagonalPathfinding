import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from heapq import heappop, heappush

# Define the map elements
map_elements = [
    ['.', '.', '.', '.', '.', 'R2', '.', '.', '.', '.'],
    ['.', '.', '#', 'T', 'O', '.', 'O', 'O', '.', '.'],
    ['O', 'R1', '.', 'O', '.', '#', 'O', 'T', '.', 'T'],
    ['.', '.', 'O', '.', 'O', '.', '.', 'R2', '#', '.'],
    ['.', '#', '.', '#', 'T', '.', '#', '.', 'O', '.'],
    ['S', '.', '.', '.', 'R1', '.', '.', '.', '.', '.'],
]

# Define the colors
colors = {
    'S': 'blue',
    'T': 'orange',
    '#': 'purple',
    'O': 'grey',
    'R1': 'green',
    'R2': 'green',
    '.': 'white'
}

# Directions for hexagonal grid movement
directions = {
    0: [(0, 1), (-1, 1), (-1, 0), (0, -1), (1, 0), (1, 1)],  # Even row adjustments
    1: [(0, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0)]  # Odd row adjustments
}

# Function to compute heuristic: Manhattan distance on a hex grid
def hexagonal_heuristic(a, b):
    x1, y1 = a
    x2, y2 = b
    z1, z2 = -x1-y1, -x2-y2
    return max(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))

# A* search algorithm for hexagonal grid
def a_star_search(start, goal):
    open_set = []
    heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: hexagonal_heuristic(start, goal)}

    while open_set:
        _, current = heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(current)  # add the start node
            return path[::-1]  # return reversed path

        current_x, current_y = current
        row_type = current_y % 2
        for dx, dy in directions[row_type]:
            neighbor = (current_x + dx, current_y + dy)
            if 0 <= neighbor[0] < len(map_elements) and 0 <= neighbor[1] < len(map_elements[0]):
                neighbor_type = map_elements[neighbor[0]][neighbor[1]]
                if neighbor_type == 'O' or neighbor_type == '#':
                    continue
                if not (dx == 0 or dy == 0 or (dx + dy == 0)):  # Prevent invalid movements
                    continue
                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + hexagonal_heuristic(neighbor, goal)
                    heappush(open_set, (f_score[neighbor], neighbor))

    return None  # No valid path

# Visualization function
def create_hexagon(center, color, label=None):
    hexagon = patches.RegularPolygon(center, numVertices=6, radius=0.5, orientation=np.radians(30), edgecolor='black', facecolor=color)
    ax.add_patch(hexagon)
    if label:
        ax.text(center[0], center[1], label, ha='center', va='center', color='black', fontsize=8)

def draw_path(path, color):
    for i in range(len(path)-1):
        start = path[i]
        end = path[i+1]
        start_x, start_y = start
        end_x, end_y = end
        x1 = start_y * 0.75
        y1 = start_x * (3**0.5) / 2
        if start_y % 2 == 1:
            y1 += (3**0.5) / 4
        x2 = end_y * 0.75
        y2 = end_x * (3**0.5) / 2
        if end_y % 2 == 1:
            y2 += (3**0.5) / 4
        ax.plot([x1, x2], [y1, y2], color=color, linewidth=2)

# Define start and treasure locations from the grid
start_pos = (5, 0)
treasures = [(1, 3), (2, 7), (2, 9), (4, 4)]

# Calculate paths and print textual output
paths = []
complete_path = [start_pos]  # start from the initial starting position
for treasure in treasures:
    path = a_star_search(start_pos, treasure)
    if path:
        paths.append(path)
        start_pos = treasure  # update start position after reaching each treasure
        complete_path.extend(path[1:])  # extend the complete path, skip the starting point to avoid repetition

# Redraw the map and paths
fig, ax = plt.subplots(figsize=(10, 10))
for row in range(len(map_elements)):
    for col in range(len(map_elements[row])):
        element = map_elements[row][col]
        color = colors[element]
        x = col * 0.75
        y = row * (3**0.5) / 2
        if col % 2 == 1:
            y += (3**0.5) / 4
        create_hexagon((x, y), color, label=element)

path_colors = ['red', 'blue', 'green', 'magenta']
for idx, path in enumerate(paths):
    draw_path(path, path_colors[idx])
    print(f"Path to treasure {idx+1}: {path}")

# Print the complete path
print("Complete path:", complete_path)

plt.legend(handles=[patches.Patch(facecolor=color, edgecolor='black', label=label) for label, color in colors.items()], bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
ax.set_xlim(-1, len(map_elements[0]) * 0.75 + 1)
ax.set_ylim(-1, len(map_elements) * (3**0.5) / 2 + 1)
ax.set_aspect('equal')
plt.title('Map of the Virtual World with Optimal Paths')
ax.axis('off')
plt.show()