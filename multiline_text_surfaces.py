"""Pygame multi-line text sample
Copyright 2017, Sjors van Gelderen
"""

import pygame


# Process pygame events
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


# Main program logic
def program():
    # Initialize pygame
    size = (width, height) = (800, 600)
    pygame.init()
    screen = pygame.display.set_mode(size)

    # Define colors
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Load font
    font = pygame.font.Font(None, 30)

    # Generate lines
    lines = [ "This is line {}".format(i) for i in range(10) ]

    # Generate surfaces
    text_surfaces = [ font.render(line, 1, white) for line in lines ]

    # Main loop
    while process_events():
        # Clear the screen
        screen.fill(black)
        
        # Blit the text surfaces
        for index, surface in enumerate(text_surfaces):
            screen.blit(surface, (16, index * surface.get_height()))
        
        # Switch buffers
        pygame.display.flip()


# Run the program
program()
