# Hexagonal Grid Pathfinding Visualization

This project implements an A* pathfinding algorithm on a hexagonal grid map with obstacles, treasures, and special tiles. It visualizes the map and the optimal paths from a starting position to multiple treasure locations using Matplotlib.

## Features

- **Hexagonal Grid Map:** A custom map represented as a 2D list with hexagonal tiles.
- **Map Elements:**
  - `S`: Start position (blue)
  - `T`: Treasure (orange)
  - `#`: Obstacle (purple)
  - `O`: Ocean or impassable tile (grey)
  - `R1`, `R2`: Road or path tiles (green)
  - `.`: Empty tile (white)
- **A* Pathfinding Algorithm:** Calculates the shortest path on a hexagonal grid while avoiding obstacles.
- **Hexagonal Heuristic:** Uses a hexagonal distance heuristic suitable for hex grids.
- **Visualization:**
  - Map tiles drawn as colored hexagons.
  - Paths drawn in distinct colors between start and treasures.
  - Legend explaining tile colors.

## Requirements

- Python 3.x
- Matplotlib
- NumPy

You can install the dependencies with:

```bash
pip install matplotlib numpy
```

## Usage

1. Run the Python script to visualize the map and paths:

```bash
A_Star_Virtual_World.py
```

2. The program will print the individual paths to each treasure and the complete combined path.

3. A graphical window will display the hexagonal map with colored tiles and the paths drawn on top.

## How It Works

- The map is defined as a 2D array of symbols.
- Each tile type has a specific color for visualization.
- The A* search algorithm is adapted for hexagonal grids, using an appropriate heuristic.
- The algorithm finds paths from the start position to each treasure in sequence.
- The results are plotted using Matplotlib's hexagon patches and lines for paths.

## Customization

- Modify the `map_elements` array to change the map layout.
- Add or remove treasures in the `treasures` list.
- Adjust tile colors in the `colors` dictionary.
- Change path colors by editing the `path_colors` list.

## License

This project is provided under the MIT License.

---

Feel free to reach out if you have questions or want to contribute!
