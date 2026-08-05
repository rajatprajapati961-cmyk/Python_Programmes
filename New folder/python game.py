import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
GRAY = (60, 60, 60)
GREEN = (0, 180, 0)
RED = (220, 50, 50)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Road settings
ROAD_WIDTH = 350
ROAD_X = (WIDTH - ROAD_WIDTH) // 2

# Player
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 90
player_x = WIDTH // 2 - PLAYER_WIDTH // 2
player_y = HEIGHT - 120
player_speed = 7

# Enemy
ENEMY_WIDTH = 50
ENEMY_HEIGHT = 90
enemy_x = random.randint(
    ROAD_X + 20,
    ROAD_X + ROAD_WIDTH - ENEMY_WIDTH - 20
)
enemy_y = -100
enemy_speed = 6

# Font
font = pygame.font.SysFont("Arial", 30)

score = 0
line_y = 0


def draw_car(x, y, color):
    pygame.draw.rect(
        screen,
        color,
        (x, y, PLAYER_WIDTH, PLAYER_HEIGHT),
        border_radius=8
    )

    pygame.draw.rect(
        screen,
        WHITE,
        (x + 10, y + 10, 30, 20),
        border_radius=5
    )

    pygame.draw.circle(screen, BLACK, (x + 10, y + 20), 6)
    pygame.draw.circle(screen, BLACK, (x + 40, y + 20), 6)
    pygame.draw.circle(screen, BLACK, (x + 10, y + 70), 6)
    pygame.draw.circle(screen, BLACK, (x + 40, y + 70), 6)


running = True

while running:

    clock.tick(FPS)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Keys
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed

    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Keep player on road
    if player_x < ROAD_X:
        player_x = ROAD_X

    if player_x > ROAD_X + ROAD_WIDTH - PLAYER_WIDTH:
        player_x = ROAD_X + ROAD_WIDTH - PLAYER_WIDTH

    # Move enemy
    enemy_y += enemy_speed

    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(
            ROAD_X + 20,
            ROAD_X + ROAD_WIDTH - ENEMY_WIDTH - 20
        )
        score += 1
        enemy_speed += 0.2

    # Collision
    player_rect = pygame.Rect(
        player_x,
        player_y,
        PLAYER_WIDTH,
        PLAYER_HEIGHT
    )

    enemy_rect = pygame.Rect(
        enemy_x,
        enemy_y,
        ENEMY_WIDTH,
        ENEMY_HEIGHT
    )

    if player_rect.colliderect(enemy_rect):
        running = False

    # Background
    screen.fill(GREEN)

    # Road
    pygame.draw.rect(
        screen,
        GRAY,
        (ROAD_X, 0, ROAD_WIDTH, HEIGHT)
    )

    # Road edges
    pygame.draw.line(
        screen,
        YELLOW,
        (ROAD_X, 0),
        (ROAD_X, HEIGHT),
        4
    )

    pygame.draw.line(
        screen,
        YELLOW,
        (ROAD_X + ROAD_WIDTH, 0),
        (ROAD_X + ROAD_WIDTH, HEIGHT),
        4
    )

    # Center lines
    line_y += enemy_speed

    if line_y >= 40:
        line_y = 0

    for i in range(-1, 20):
        pygame.draw.rect(
            screen,
            WHITE,
            (
                WIDTH // 2 - 5,
                i * 40 + line_y,
                10,
                25
            )
        )

    # Cars
    draw_car(player_x, player_y, RED)
    draw_car(enemy_x, enemy_y, WHITE)

    # Score
    score_surface = font.render(
        f"Score : {score}",
        True,
        WHITE
    )

    screen.blit(score_surface, (10, 10))

    pygame.display.update()

# Game Over
screen.fill((30, 30, 30))

game_over = font.render(
    "GAME OVER",
    True,
    RED
)

final_score = font.render(
    f"Final Score : {score}",
    True,
    WHITE
)

screen.blit(game_over, (150, 300))
screen.blit(final_score, (145, 350))

pygame.display.update()

pygame.time.wait(3000)

pygame.quit()
sys.exit()
