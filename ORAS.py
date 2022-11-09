import pygame
import sys
import time

pygame.init()

# screen = pygame.display.set_mode((400, 400))
# pygame.display.set_caption("7/10")
# screen.fill((234, 0, 105))
water = pygame.image.load("images/water.png")
water_rect = water.get_rect()
tile_size = water_rect.width
screen = pygame.display.set_mode((10*tile_size, 10*tile_size))
pygame.display.set_caption("7/10")
screen.fill((234, 0, 105))
screen_rect = screen.get_rect()
# screen.blit(water, (0, 0))
# screen.blit(water, (64, 0))
# screen.blit(water, (128, 0))
rows = screen_rect.height/tile_size
cols = screen_rect.width/tile_size

for x in range(int(rows)):
    for y in range(int(cols)):
        screen.blit(water, (x*water_rect.height, y*water_rect.width))





while True:
   # print("----------check for new events____________")
    recent_events = pygame.event.get()
   # print("----------done checking for events--------")
    for event in recent_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    time.sleep(1)