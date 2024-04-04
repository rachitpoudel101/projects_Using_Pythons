import pygame
import random

# === constants ===  # PEP8: UPPER_CASE_NAMES

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

FPS = 60
FPS = 120

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# === classes ===  # PEP8: CamelCaseNames

# empty

# === functions ===  # PEP8: lower_case_names

# empty

# === main ===

pygame.init()

screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )

# set some color at start 
snake_head_color = 'red'
snake_tail_color = 'green'

change_colors = False

# --- mainloop ---

clock = pygame.time.Clock()

running = True

while running:

    # --- events ---
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            change_colors = True

    # --- changes/moves/updates ---

    if change_colors:
        # select random color
        snake_head_color = random.choice(['red', 'yellow', 'gray50'])  # select new color
        snake_tail_color = random.choice(['green', 'blue', 'gray25'])  # select new color

        change_colors = False
        
    # --- draws ---

    screen.fill(BLACK)

    # draw head    
    pygame.draw.rect(screen, snake_head_color, (100, 100, 48, 48))
    
    # draw tail
    for x in range(150, 700, 50):
        pygame.draw.rect(screen, snake_tail_color, (x, 100, 48, 48))
    
    pygame.display.flip()

    # --- FPS ---

    dt = clock.tick(FPS) 
    #pygame.display.set_caption(f'{dt:.2f} ms')
    
# --- end ---

pygame.quit()