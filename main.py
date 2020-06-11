import pygame

pygame.init()
# Create The Screen
screen = pygame.display.set_mode((800, 600))
# Title and Icon
pygame.display.set_caption("Space Invaders Tutorial")
# Player
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg, (playerX, playerY))

# Game Loop
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    player()
    
    pygame.display.update()