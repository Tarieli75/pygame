import pygame

from controller import Player


pygame.init()

background_image = pygame.image.load('football.png')

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player_1 = Player()

pygame.display.set_caption('user: ')

username = ""

font = pygame.font.SysFont('Arial', 30)

runing = True

while runing:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        if event.type == pygame.KEYDOWN:
            username += event.unicode
    # pygame.draw.rect(screen, BLACK, (player_1.x, player_1.y, player_1.size, player_1.size))
    screen.blit(pygame.transform.scale(background_image, (player_1.size, player_1.size)), (player_1.x, player_1.y))
    keyboard = pygame.key.get_pressed()
    # print(keyboard)
    dx = 0
    dy = 0
    if keyboard[pygame.K_LEFT] :
        dx -= 1
    if keyboard[pygame.K_RIGHT] :
        dx += 1
    if keyboard[pygame.K_UP] :
        dy -= 1
    if keyboard[pygame.K_DOWN] :
        dy += 1

    username_screen = font.render(username, True, RED)
    screen.blit(username_screen, (player_1.x, player_1.y+50))

    player_1.move_player(dx, dy)
    pygame.display.update()
    clock.tick(60)

print(username)

pygame.quit()
# sys.exit()