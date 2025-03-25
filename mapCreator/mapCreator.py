import json
import os

import pygame

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1800, 1000
BASE_WIDTH, BASE_HEIGHT = 32, 32
ZOOM_MIN, ZOOM_MAX = 0.1, 2.0
SCROLL_SPEED = 10
MAP_SIZE = 200  # 200x200 tile grid

# Rainbow Colors
TILE_TYPES = {
    0: pygame.Color(0, 0, 0),       # Black (empty space)
    1: pygame.Color(255, 0, 0),     # Red
    2: pygame.Color(255, 165, 0),   # Orange
    3: pygame.Color(255, 255, 0),   # Yellow
    4: pygame.Color(0, 255, 0),     # Green
    5: pygame.Color(0, 255, 255),   # Cyan
    6: pygame.Color(0, 0, 255),     # Blue
    7: pygame.Color(75, 0, 130),    # Indigo
    8: pygame.Color(148, 0, 211),   # Violet
    9: pygame.Color(255, 0, 255),   # Magenta
    10: pygame.Color(255, 255, 255) # White
}


# Map State
class Map:
    def __init__(self, size):
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]
        self.zoom = 1.0
        self.view_x = 0
        self.view_y = 0
        self.selected_tile = 1

    def load(self, filename="map.json"):
        """Load the map from a JSON file."""
        if os.path.exists(filename):
            with open(filename, "r") as f:
                self.grid = json.load(f)
                print("Map loaded successfully.")
        else:
            print("No map file found, starting with an empty map.")

    def save(self, filename="map.json"):
        """Save the current map to a JSON file in row-separated format."""
        with open(filename, "w") as f:
            f.write("[\n")
            for i, row in enumerate(self.grid):
                row_str = json.dumps(row)
                if i < len(self.grid) - 1:
                    f.write(f"    {row_str},\n")
                else:
                    f.write(f"    {row_str}\n")
            f.write("]\n")
        print("Map saved successfully (row-separated format).")

    def scroll(self, dx, dy):
        """Scroll the map by delta x and delta y."""
        self.view_x = max(0, min(self.view_x + dx, self.size * BASE_WIDTH * self.zoom - SCREEN_WIDTH))
        self.view_y = max(0, min(self.view_y + dy, self.size * BASE_HEIGHT * self.zoom - SCREEN_HEIGHT))

    def zoom_in(self):
        """Zoom in with upper limit."""
        self.zoom = min(self.zoom + 0.1, ZOOM_MAX)

    def zoom_out(self):
        """Zoom out with lower limit."""
        self.zoom = max(self.zoom - 0.1, ZOOM_MIN)

    def clear(self):
        """Clear the map by setting all tiles to 0."""
        self.grid = [[0 for _ in range(self.size)] for _ in range(self.size)]
        print("Map cleared successfully.")


# Pygame Initialization
def init_pygame():
    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Map Creator")
    return window


# Draw the grid efficiently
def draw_grid(window, game_map):
    grid_w, grid_h = int(BASE_WIDTH * game_map.zoom), int(BASE_HEIGHT * game_map.zoom)

    # Calculate visible tile range to avoid unnecessary rendering
    start_x = max(game_map.view_x // grid_w, 0)
    start_y = max(game_map.view_y // grid_h, 0)
    end_x = min((game_map.view_x + SCREEN_WIDTH) // grid_w + 1, game_map.size)
    end_y = min((game_map.view_y + SCREEN_HEIGHT) // grid_h + 1, game_map.size)

    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            color = TILE_TYPES.get(game_map.grid[y][x], TILE_TYPES[0])
            pygame.draw.rect(
                window,
                color,
                (
                    x * grid_w - game_map.view_x,
                    y * grid_h - game_map.view_y,
                    grid_w,
                    grid_h
                )
            )


# Handle mouse interactions (placement and removal)
def handle_mouse(game_map, placing):
    """Handle continuous tile placement or removal."""
    x, y = pygame.mouse.get_pos()
    grid_w, grid_h = int(BASE_WIDTH * game_map.zoom), int(BASE_HEIGHT * game_map.zoom)

    grid_x = (x + game_map.view_x) // grid_w
    grid_y = (y + game_map.view_y) // grid_h

    if 0 <= grid_x < game_map.size and 0 <= grid_y < game_map.size:
        buttons = pygame.mouse.get_pressed()

        if placing:
            if buttons[0]:  # Left click -> Place tile
                game_map.grid[grid_y][grid_x] = game_map.selected_tile
            elif buttons[2]:  # Right click -> Remove tile
                game_map.grid[grid_y][grid_x] = 0


# Handle keyboard inputs
def handle_keys(game_map):
    """Handle key presses for scrolling, tile selection, and clearing."""
    keys = pygame.key.get_pressed()

    # Scroll with arrow keys
    if keys[pygame.K_LEFT]:
        game_map.scroll(-SCROLL_SPEED, 0)
    if keys[pygame.K_RIGHT]:
        game_map.scroll(SCROLL_SPEED, 0)
    if keys[pygame.K_UP]:
        game_map.scroll(0, -SCROLL_SPEED)
    if keys[pygame.K_DOWN]:
        game_map.scroll(0, SCROLL_SPEED)

    # Tile selection with number keys
    for i in range(10):
        if keys[pygame.K_0 + i]:
            game_map.selected_tile = i if i != 0 else 10

    # Clear the map with the 'C' key
    if keys[pygame.K_c]:
        game_map.clear()


# Main game loop
def main():
    window = init_pygame()
    clock = pygame.time.Clock()

    game_map = Map(MAP_SIZE)
    game_map.load()

    running = True
    placing = False

    while running:
        window.fill((255, 255, 255))  # Clear the screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_map.save()
                pygame.quit()
                return

            # Handle mouse zoom events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:  # Scroll up -> Zoom in
                    game_map.zoom_in()
                elif event.button == 5:  # Scroll down -> Zoom out
                    game_map.zoom_out()

                # Start placing/removing on click
                if event.button in (1, 3):
                    placing = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button in (1, 3):
                    placing = False

        # Handle continuous mouse interactions
        if placing:
            handle_mouse(game_map, placing)

        # Handle keyboard inputs (including clearing)
        handle_keys(game_map)

        # Draw and update
        draw_grid(window, game_map)

        pygame.display.flip()
        clock.tick(60)


# Run the program
if __name__ == "__main__":
    main()
