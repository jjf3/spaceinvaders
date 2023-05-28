#created by jjf3

import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Space Invaders")

# Set up the background
background_image = pygame.image.load("background_image.jpg")
background_image = pygame.transform.scale(background_image, (window_width, window_height))

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up the player
player_width = 50
player_height = 50
player_x = window_width // 2 - player_width // 2
player_y = window_height - player_height - 10
player_speed = 5

# Set up the enemy
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, window_width - enemy_width)
enemy_y = random.randint(50, 200)
enemy_speed = 2

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < window_width - player_width:
        player_x += player_speed

    # Move the enemy
    enemy_x += enemy_speed
    if enemy_x < 0 or enemy_x > window_width - enemy_width:
        enemy_speed *= -1
        enemy_y += enemy_height

    # Collision detection
    if player_x < enemy_x + enemy_width and player_x + player_width > enemy_x and \
            player_y < enemy_y + enemy_height and player_y + player_height > enemy_y:
        running = False

    # Draw the background
    window.blit(background_image, (0, 0))

    # Draw the player and enemy
    pygame.draw.rect(window, white, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(window, white, (enemy_x, enemy_y, enemy_width, enemy_height))

    pygame.display.update()
    clock.tick(60)

# Quit the game
pygame.quit()
