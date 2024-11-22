import pygame
import random
import sys

# Initialize Pygame
pygame.init()


def init():
    global canvas
    # Set up the canvas
    canvas = pygame.display.set_mode((350, 900))
    pygame.display.set_caption("DMX Output")

# Generate random data (2D array: 18 rows, 7 columns)


# Define colors
def get_color(value):
    """Map a value between 0 and 1 to a shade of gray."""
    intensity = int(value)
    return (intensity, intensity, intensity)  # RGB tuple

# Main loop
last_key = ''

def get_input():
    global last_key
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # exit
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == last_key:
                last_key = None
        if event.type == pygame.KEYDOWN:
            last_key = event.key
    # Convert last key into string
    return pygame.key.name(last_key) if last_key else None

def update(data):
    global canvas
    if canvas is None:
        return

    canvas.fill((0, 0, 0))  # Black background

    # Draw the data
    cell_width = canvas.get_width() // 7
    cell_height = canvas.get_height() // 18


    for row in range(len(data)):
        for col in range(len(data[row])):
            value = data[row][col]
            color = get_color(value)
            x = col * cell_width
            y = row * cell_height
            pygame.draw.rect(canvas, color, (x, y, cell_width, cell_height))

    # Update the display
    pygame.display.update()

def quit():
    # Quit Pygame
    pygame.quit()
