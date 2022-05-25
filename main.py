import pygame
import os

#defining necessary constants
WIDTH, HEIGHT = 900,500
PATH = "pygame/assets"
WHITE = (255,255,255)
SS_WIDTH, SS_HEIGHT = 55,40

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
    screen.blit(yellowship, (yellow.x, yellow.y))
    screen.blit(redship, (red.x, red.y))
    pygame.display.update()

#main function
def main():
    
    r = pygame.Rect(100, 300, SS_WIDTH, SS_HEIGHT)
    y = pygame.Rect(700, 300, SS_WIDTH, SS_HEIGHT)


    #creating an object to cap frame rate
    clock = pygame.time.Clock()
    run = True

    #while there isn't any prompt to quit, we continue playing/updating the game
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        updateScreen(r, y)

    pygame.quit()

#making sure that we are running from this file
if __name__ == "__main__":
    main()


