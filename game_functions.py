import sys

import pygame


def check_events():
    """Respond to keypresses and mouse events"""

    for event in pygame.event.get():
        # If the user closes the window, quits the program
        if event.type == pygame.QUIT:
            sys.exit()
