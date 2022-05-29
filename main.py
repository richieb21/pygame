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
    if keys_pressed[pygame.K_a]: #left key
        y.x -= VELOCITY
    if keys_pressed[pygame.K_d]: #right key
        y.x += VELOCITY
    if keys_pressed[pygame.K_s]: #down key
        y.y += VELOCITY
    if keys_pressed[pygame.K_w]: #up key
        y.y -= VELOCITY

#moves the red ship
def red_handle_movement(keys_pressed,r):
    if keys_pressed[pygame.K_LEFT]: #left key
        r.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT]: #right key
        r.x += VELOCITY
    if keys_pressed[pygame.K_DOWN]: #down key
        r.y += VELOCITY
    if keys_pressed[pygame.K_UP]: #up key
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

        keys_pressed = pygame.key.get_pressed()

        yellow_handle_movement(keys_pressed, y)
        red_handle_movement(keys_pressed, r)

        updateScreen(r, y)

    pygame.quit()

#making sure that we are running from this file
if __name__ == "__main__":
    main()


