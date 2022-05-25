import pygame
import os

WIDTH, HEIGHT = 900,500
PATH = "pygame/assets"
WHITE = (255,255,255)

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))


pygame.display.set_caption("First Pygame")

yellowship = pygame.image.load(os.path.join(PATH,'spaceship_yellow.png'))
redship = pygame.image.load(os.path.join(PATH,'spaceship_red.png'))

#updates the screen and fills the background as white
def updateScreen():
    screen.fill(WHITE)
    screen.blit(yellowship, (0,0))
    pygame.display.update()

#main function
def main():

    #creating an object to cap frame rate
    clock = pygame.time.Clock()
    run = True

    #while there isn't any prompt to quit, we continue playing/updating the game
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        updateScreen()

    pygame.quit()

#making sure that we are running from this file
if __name__ == "__main__":
    main()


