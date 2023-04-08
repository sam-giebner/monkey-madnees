
import pygame
import sys
import random

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000

MONKEY_SPEED = 10

GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,0,0)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption('Monkey-Madness')

clock = pygame.time.Clock()

gravity = 2

score = 0

happy_sound = pygame.mixer.Sound("audio/happy-monkey.wav")
sad_sound = pygame.mixer.Sound("audio/sad-monkey.wav")

background = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
background.fill('Blue')

font = pygame.font.Font('fonts/Tribeca.ttf',30)

ground = pygame.Surface((SCREEN_WIDTH,50))
ground.fill('Green')
ground_rect = ground.get_rect(midbottom = (SCREEN_WIDTH/2,SCREEN_HEIGHT))

monkey = pygame.transform.scale_by(pygame.image.load('images/monkey.png').convert_alpha(),0.1)
monkey_x, monkey_y = [SCREEN_WIDTH/2,SCREEN_HEIGHT-50]
monkey_rect = monkey.get_rect(midbottom = (monkey_x, monkey_y))

momentum = 0

banana = pygame.transform.scale_by(pygame.image.load('images/banana.png').convert_alpha(),0.06)
banana_x, banana_y = [random.randint(10,SCREEN_WIDTH-10),-10]
banana_rect = banana.get_rect(midtop = (banana_x,banana_y))

play = True

while play:
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
        momentum = momentum * 0.9

    if monkey_rect.x <= 0:
        momentum = 0
        monkey_rect.x = 5

    if monkey_rect.x >= SCREEN_WIDTH - 20:
        momentum = 0
        monkey_rect.x = SCREEN_WIDTH - 50
    
    if banana_rect.colliderect(ground_rect) > 0:

        pygame.mixer.Sound.play(sad_sound)
        
        banana_rect.y = -10
        banana_rect.x = random.randint(10,SCREEN_WIDTH-10)
    
    if banana_rect.colliderect(monkey_rect) > 0:
        print('Win!')
        pygame.mixer.Sound.play(happy_sound)
        
        score += 10

        gravity += 0.4
        
        banana_rect.y = -10
        banana_rect.x = random.randint(10,SCREEN_WIDTH-10)
        
    banana_rect.y += gravity
        
    pygame.display.update()
    
    clock.tick(60)