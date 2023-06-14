#Test Stretch Legs
print("Hello World")

#Import the Package initialize
import pygame
import time
import random

#Initialize Game
pygame.init()

#Define Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#Setup the Display
dis_width = 800
dis_height = 600

#Start Display
dis = pygame.display.set_mode((dis_width, dis_height))  #Start Display
pygame.display.set_caption("J's Snake ;)")  #Output welcome message

#Initialize stuff
snake_block = 10
snake_speed = 30
clock = pygame.time.Clock()

#Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

#score
def your_score(score):
    value = score_font.render("Pitiful Score: " + str(score), True, yellow)
    dis.blit(value, [0,0])

#Make Snek
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

#Function Display Message to Player
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])

#Meat and Potatos
def gameloop():
    game_over = False   #Dead bool
    game_close = False  #Close bool
    
    x1 = dis_width/2
    y1 = dis_height/2
    
    x1_delta = 0
    y1_delta = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

    while not game_over:    #Keeps the game from closing instantly

        while game_close == True:
            dis.fill(blue)
            message("Get Rekt Loser Press Q-Quit or C-Play Again", red)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True    #Sets the game over to true on X click
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_delta = -snake_block
                    y1_delta = 0
                elif event.key == pygame.K_RIGHT:
                    x1_delta = snake_block
                    y1_delta = 0
                elif event.key == pygame.K_UP:
                    x1_delta = 0
                    y1_delta = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_delta = 0
                    y1_delta = snake_block

        #Out of Bounds Dead
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True       
        
        #Move Snake
        x1 += x1_delta
        y1 += y1_delta
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block]) #Draw Food
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)

        pygame.display.update()

        #Got Food?
        if x1 == foodx and y1 == foody:
            print("Yummy!!")
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            length_of_snake += 1
        
        clock.tick(snake_speed) #Increment the clock, Control movement speed

    #End of program when game_over goes True
    pygame.quit()
    quit()

#Run the game
gameloop()