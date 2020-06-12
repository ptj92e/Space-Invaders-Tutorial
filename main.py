import pygame
import random
import math

pygame.init()

# Create The Screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("space.jpg")

# Title and Icon
pygame.display.set_caption("Space Invaders Tutorial")

# Player
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0, 735)
enemyY = random.randint(50, 150)
enemyX_change = 3

# Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = "ready"

score = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# Game Loop
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 3
            if event.key == pygame.K_RIGHT:
                playerX_change += 3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":    
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 735:
        playerX = 735

    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX = 0
        enemyX_change = 3
        enemyY += 40
    elif enemyX >= 736:
        enemyX = 736
        enemyX_change = -3
        enemyY += 40

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collision
    collision = is_collision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        enemyX = random.randint(0, 736)
        enemyY = random.randint(50, 150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()