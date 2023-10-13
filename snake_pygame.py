import pygame
import time
import random

pygame.init()

# Dimensions
width, height = 600, 400

# Colors
black = (0, 0, 0)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game by ChatGPT')

game_over = False

x1 = width/2
y1 = height/2
 
snake_block=20
 
x1_change = 0     
y1_change = 0
 
clock = pygame.time.Clock()
snake_speed=7
 
font_style = pygame.font.SysFont(None, 50)
 
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [width/6, height/3])
    
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, blue, [x[0], x[1], snake_block, snake_block])

def has_eaten(snake, food, threshold):
    sx, sy = snake[0] + snake_block//2, snake[1] + snake_block//2
    fx, fy = food[0] + snake_block//2, food[1] + snake_block//2
    return ((sx - fx)**2 + (sy - fy)**2)**0.5 < threshold

def gameLoop():
    game_over = False
    game_close = False
    
    x1 = width / 2
    y1 = height / 2
    
    x1_change = 0
    y1_change = 0
    
    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
    
    while not game_over:
        
        while game_close == True:
            dis.fill(black)
            message("Game over - press C to restart", red)
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        
        our_snake(snake_block, snake_List)
        
        pygame.display.update()
        
        if has_eaten((x1, y1), (foodx, foody), snake_block):
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        
        clock.tick(snake_speed)
        
    pygame.quit()
    quit()

gameLoop()
