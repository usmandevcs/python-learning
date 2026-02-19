import pygame
import sys # sys is needed to exit the program cleanly

# 1. Initialize Pygame
pygame.init()

# 2. Define constants for the window size
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame Window")

# 3. Set up the game loop
running = True
while running:
    # 4. Handle events (e.g., user input)
    for event in pygame.event.get():
        # If the user clicks the close button, exit the loop
        if event.type == pygame.QUIT:
            running = False

    # 5. Game logic goes here (e.g., move sprites)

    # 6. Fill the screen with a color (e.g., black)
    SCREEN.fill((0, 0, 0)) # RGB value for black

    # 7. Update the display to show the changes
    pygame.display.flip()

# 8. Quit Pygame when the loop is over
pygame.quit()
sys.exit()
