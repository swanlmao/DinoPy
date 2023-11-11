import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
GROUND_HEIGHT = 50
DINO_SIZE = 50
OBSTACLE_SIZE = 30
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dino Game")

# Load images
dino_image = pygame.Surface((DINO_SIZE, DINO_SIZE))
dino_image.fill(WHITE)

obstacle_image = pygame.Surface((OBSTACLE_SIZE, OBSTACLE_SIZE))
obstacle_image.fill(WHITE)

# Initial positions
dino_y = SCREEN_HEIGHT - GROUND_HEIGHT - DINO_SIZE
dino_x = 50

obstacle_x = SCREEN_WIDTH
obstacle_y = SCREEN_HEIGHT - GROUND_HEIGHT - OBSTACLE_SIZE

# Variables
jumping = False
jump_count = 12
gravity = 1
speed = 5
score = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                jumping = True

    keys = pygame.key.get_pressed()
    if jumping:
        if jump_count >= -12:
            neg = 1
            if jump_count < 0:
                neg = -1
            dino_y -= (jump_count ** 2) * 0.25 * neg
            jump_count -= 1
        else:
            jumping = False
            jump_count = 12

    # Apply gravity
    if not jumping and dino_y < SCREEN_HEIGHT - GROUND_HEIGHT - DINO_SIZE:
        dino_y += gravity

    # Move obstacle
    obstacle_x -= speed
    if obstacle_x < 0:
        obstacle_x = SCREEN_WIDTH
        obstacle_y = random.randint(SCREEN_HEIGHT - GROUND_HEIGHT - OBSTACLE_SIZE - DINO_SIZE, SCREEN_HEIGHT - OBSTACLE_SIZE)
        score += 1
        speed += 0.2

    # Check for collisions
    dino_rect = pygame.Rect(dino_x, dino_y, DINO_SIZE, DINO_SIZE)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, OBSTACLE_SIZE, OBSTACLE_SIZE)

    if dino_rect.colliderect(obstacle_rect):
        print("Game Over. Your score:", score)
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (0, SCREEN_HEIGHT - GROUND_HEIGHT, SCREEN_WIDTH, GROUND_HEIGHT))

    screen.blit(dino_image, (dino_x, dino_y))
    screen.blit(obstacle_image, (obstacle_x, obstacle_y))

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)
 