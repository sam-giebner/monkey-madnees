from curses import KEY_LEFT, KEY_RIGHT
import pygame
import sys
import random

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000

MONKEY_SPEED = 5

GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption('Monkey-Madness')

clock = pygame.time.Clock()

gravity = 2

score = 0

background = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
background.fill('Blue')

font = pygame.font.Font('fonts/Tribeca.ttf',30)

ground = pygame.Surface((SCREEN_WIDTH,50))
ground.fill('Green')
ground_rect = ground.get_rect(midbottom = (SCREEN_WIDTH/2,SCREEN_HEIGHT))

monkey = pygame.image.load('images/monkey.png').convert_alpha()
monkey = pygame.transform.scale(monkey,(50,50))
monkey_x, monkey_y = [SCREEN_WIDTH/2,SCREEN_HEIGHT-50]
monkey_rect = monkey.get_rect(midbottom = (monkey_x, monkey_y))

momentum = 0

banana = pygame.image.load('images/banana.png').convert_alpha()
banana = pygame.transform.scale(banana,(50,50))
banana_x, banana_y = [random.randint(10,SCREEN_WIDTH-10),-10]
banana_rect = banana.get_rect(midtop = (banana_x,banana_y))

    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                
                momentum -= MONKEY_SPEED
                
            if event.key == pygame.K_RIGHT:
                
                momentum += MONKEY_SPEED
                
    score_text = font.render(f'POINTS: {score}',True,RED,BLUE)
    score_rect = score_text.get_rect()
    score_rect.topleft = (20,10)
            
    screen.blit(background,(0,0))
    screen.blit(ground,ground_rect)
    screen.blit(score_text,score_rect)
    screen.blit(monkey,monkey_rect)
    screen.blit(banana,banana_rect)
    
    monkey_rect.x +=  momentum
    
    if momentum != 0:
        momentum = momentum * 0.75
    
    if banana_rect.colliderect(ground_rect) > 0:
    
        print('Game over')
    
    if banana_rect.colliderect(monkey_rect) > 0:
        print('Win!')
        
        score += 10

        gravity +=0.5
        
        banana_rect.y = -10
        banana_rect.x = random.randint(10,SCREEN_WIDTH-10)
        
    banana_rect.y += gravity
        
    pygame.display.update()
    
    clock.tick(60)