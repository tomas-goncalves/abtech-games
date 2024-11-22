import pygame

# Use pygame to get inputs

# Initialize Pygame
pygame.init()


def init():
    global canvas
    # Set up the canvas
    canvas = pygame.display.set_mode((350, 350))
    pygame.display.set_caption("DMX Key Input")

def update():
    return []

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
