import pygame
import os
pygame.font.init()
pygame.mixer.init()

# defining necessary constants
WIDTH, HEIGHT = 900, 500
PATH = "pygame/assets"
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

SS_WIDTH, SS_HEIGHT = 55, 40
VELOCITY = 8
BULLET_VELOCITY = 12

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join(PATH, 'Hit.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join(PATH, 'Shoot.mp3'))

#arrays to store our bullets

yellow_bullets = []
red_bullets = []
MAX_BULLETS = 3

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.display.set_caption("First Pygame")


# loading, scaling and rotating image sprites
yellowship_image = pygame.image.load(
    os.path.join(PATH, 'spaceship_yellow.png'))
yellowship = pygame.transform.rotate(pygame.transform.scale(
    yellowship_image, (SS_WIDTH, SS_HEIGHT)), 90)

redship_image = pygame.image.load(os.path.join(PATH, 'spaceship_red.png'))
redship = pygame.transform.rotate(pygame.transform.scale(
    redship_image, (SS_WIDTH, SS_HEIGHT)), 270)

SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join(PATH, 'space.png')), (WIDTH, HEIGHT))

# displays the winner


def draw_winner(text):
    printed_text = WINNER_FONT.render(text, 1, WHITE)
    screen.blit(printed_text, (WIDTH/2 - printed_text.get_width() /
                2, HEIGHT/2 - printed_text.get_height()/2))

    pygame.display.update()
    pygame.time.delay(5000)

# updates the screen and fills the background as white


def updateScreen(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    screen.blit(SPACE, (0, 0))
    pygame.draw.rect(screen, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render(
        "Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(yellow_health), 1, WHITE)

    screen.blit(red_health_text,
                (WIDTH - red_health_text.get_width() - 10, 10))
    screen.blit(yellow_health_text, (10, 10))

    screen.blit(yellowship, (yellow.x, yellow.y))
    screen.blit(redship, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(screen, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(screen, YELLOW, bullet)

    pygame.display.update()

# moves the yellow ship


def yellow_handle_movement(keys_pressed, y):
    if keys_pressed[pygame.K_a] and (y.x - VELOCITY) > 0:  # left key
        y.x -= VELOCITY
    # right key
    if keys_pressed[pygame.K_d] and (y.x + VELOCITY + y.width) < BORDER.x + 10:
        y.x += VELOCITY
    # down key
    if keys_pressed[pygame.K_s] and (y.y + VELOCITY + y.height) < HEIGHT - 10:
        y.y += VELOCITY
    if keys_pressed[pygame.K_w] and (y.y - VELOCITY) > 0:  # up key
        y.y -= VELOCITY

# moves the red ship


def red_handle_movement(keys_pressed, r):
    # left key
    if keys_pressed[pygame.K_LEFT] and (r.x - VELOCITY) > BORDER.x + 10:
        r.x -= VELOCITY
    # right key
    if keys_pressed[pygame.K_RIGHT] and (r.x + VELOCITY + r.width) < WIDTH + 15:
        r.x += VELOCITY
    # down key
    if keys_pressed[pygame.K_DOWN] and (r.y + VELOCITY + r.height) < HEIGHT - 10:
        r.y += VELOCITY
    if keys_pressed[pygame.K_UP] and (r.y - VELOCITY) > 0:  # up key
        r.y -= VELOCITY

# moving and colliding bullets


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VELOCITY
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VELOCITY
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

# main function


def main():
    
    for bullet in red_bullets:
        red_bullets.remove(bullet)
    
    for bullet in yellow_bullets:
        yellow_bullets.remove(bullet)


    for x in red_bullets:
        red_bullets.remove(x)
    for x in yellow_bullets:
        yellow_bullets.remove(x)

    pygame.display.update()


    r = pygame.Rect(700, 300, SS_WIDTH, SS_HEIGHT)
    y = pygame.Rect(100, 300, SS_WIDTH, SS_HEIGHT)

    red_health = 10
    yellow_health = 10

    # creating an object to cap frame rate
    clock = pygame.time.Clock()
    run = True

    # while there isn't any prompt to quit, we continue playing/updating the game
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            # deals with firing bullets
            if event.type == pygame.KEYDOWN:

                # creates bullets from corresponding positions of the spaceship
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        y.x + y.width, y.y + y.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(r.x, r.y + r.height//2, 10, 5)
                    red_bullets.append(bullet)

                    BULLET_FIRE_SOUND.play()
            
            #subtracting health points if any spaceship is hit


            # subtracting health points if any spaceship is hit

            if event.type == RED_HIT:
                BULLET_HIT_SOUND.play()
                red_health -= 1

            if event.type == YELLOW_HIT:
                BULLET_HIT_SOUND.play()
                yellow_health -= 1

        winner_text = ""

        keys_pressed = pygame.key.get_pressed()

        # functions to handle movement
        yellow_handle_movement(keys_pressed, y)
        red_handle_movement(keys_pressed, r)

        # functions to handle bullet fire and collision
        handle_bullets(yellow_bullets, red_bullets, y, r)

        # updates the screen with new positions of the spaceships and bullets
        updateScreen(r, y, red_bullets, yellow_bullets,
                     red_health, yellow_health)

        # conditions to check for winners
        if red_health <= 0:
            winner_text = "Yellow Wins"
        if yellow_health <= 0:
            winner_text = "Red Wins"


        keys_pressed = pygame.key.get_pressed()

        #functions to handle movement
        yellow_handle_movement(keys_pressed, y)
        red_handle_movement(keys_pressed, r)

        #functions to handle bullet fire and collision
        handle_bullets(yellow_bullets, red_bullets, y, r)

        #updates the screen with new positions of the spaceships and bullets
        updateScreen(r, y, red_bullets, yellow_bullets, red_health, yellow_health)

        if winner_text != "":
            draw_winner(winner_text)
            break


        if winner_text != "":
            draw_winner(winner_text)
            break

    main()


# making sure that we are running from this file
if __name__ == "__main__":
    main()
