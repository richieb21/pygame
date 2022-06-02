import pygame
import os

#defining necessary constants
WIDTH, HEIGHT = 900,500
PATH = "pygame/assets"
BORDER = pygame.Rect(WIDTH/2 - 5,0,10,HEIGHT)

WHITE = (255,255,255)
BLACK = (0,0,0)

SS_WIDTH, SS_HEIGHT = 55,40
VELOCITY = 5
BULLET_VELOCITY = 10

#arrays to store our bullets
yellow_bullets = []
red_bullets = []
MAX_BULLETS = 3

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))


pygame.display.set_caption("First Pygame")


#loading, scaling and rotating image sprites
yellowship_image = pygame.image.load(os.path.join(PATH,'spaceship_yellow.png'))
yellowship = pygame.transform.rotate(pygame.transform.scale(yellowship_image, (SS_WIDTH,SS_HEIGHT)), 90)

redship_image = pygame.image.load(os.path.join(PATH,'spaceship_red.png'))
redship = pygame.transform.rotate(pygame.transform.scale(redship_image, (SS_WIDTH,SS_HEIGHT)), 270)

#updates the screen and fills the background as white
def updateScreen(red, yellow):
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, BORDER)
    screen.blit(yellowship, (yellow.x, yellow.y))
    screen.blit(redship, (red.x, red.y))
    pygame.display.update()

#moves the yellow ship
def yellow_handle_movement(keys_pressed,y): 
    if keys_pressed[pygame.K_a] and (y.x - VELOCITY) > 0: #left key
        y.x -= VELOCITY
    if keys_pressed[pygame.K_d] and (y.x + VELOCITY + y.width) < BORDER.x + 10: #right key
        y.x += VELOCITY
    if keys_pressed[pygame.K_s] and (y.y + VELOCITY + y.height) < HEIGHT - 10: #down key
        y.y += VELOCITY
    if keys_pressed[pygame.K_w] and (y.y - VELOCITY) > 0: #up key
        y.y -= VELOCITY

#moves the red ship
def red_handle_movement(keys_pressed,r):
    if keys_pressed[pygame.K_LEFT] and (r.x - VELOCITY) > BORDER.x + 10: #left key
        r.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and (r.x + VELOCITY + r.width) < WIDTH + 15: #right key
        r.x += VELOCITY
    if keys_pressed[pygame.K_DOWN] and (r.y + VELOCITY + r.height) < HEIGHT - 10: #down key
        r.y += VELOCITY
    if keys_pressed[pygame.K_UP] and (r.y - VELOCITY) > 0: #up key
        r.y -= VELOCITY

#main function
def main():
    
    r = pygame.Rect(700, 300, SS_WIDTH, SS_HEIGHT)
    y = pygame.Rect(100, 300, SS_WIDTH, SS_HEIGHT)


    #creating an object to cap frame rate
    clock = pygame.time.Clock()
    run = True

    #while there isn't any prompt to quit, we continue playing/updating the game
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(y.x + y.width, y.y + y.height/2 - 2, 10, 5)
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(r.x, r.y + r.height/2, 10, 5)
                    red_bullets.append(bullet)
        
        print(red_bullets, yellow_bullets)
        keys_pressed = pygame.key.get_pressed()

        yellow_handle_movement(keys_pressed, y)
        red_handle_movement(keys_pressed, r)

        updateScreen(r, y)

    pygame.quit()

#making sure that we are running from this file
if __name__ == "__main__":
    main()


