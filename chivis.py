import os
import random
import pygame
import pygame, sys
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Should you do it or not?')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60

# first_event = True

WHAT_DOING = pygame.image.load(os.path.join('Assets', '900_what_doing.png'))
WHAT_DOING3 = pygame.image.load(os.path.join('Assets', '900_what_doing_3.png'))
WHAT_DOING2 = pygame.image.load(os.path.join('Assets', '900_what_doing_2.png'))
WHAT_DOING1 = pygame.image.load(os.path.join('Assets', '900_what_doing_1.png'))
TRUE_PIC = pygame.image.load(os.path.join('Assets', 'true_pic.png'))
FALSE_PIC = pygame.image.load(os.path.join('Assets', 'false_pic.png'))
INGUSH_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'ingush.mp3'))
TRUE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'TRUE.mp3'))
FALSE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'FALSE.mp3'))


def draw_window_w():
    WIN.blit(WHAT_DOING, (0, 0))
    pygame.display.update()


def draw_window_w3():
    WIN.blit(WHAT_DOING3, (0, 0))
    pygame.display.update()
    pygame.time.delay(1000)


def draw_window_w2():
    WIN.blit(WHAT_DOING2, (0, 0))
    pygame.display.update()
    pygame.time.delay(1000)


def draw_window_w1():
    WIN.blit(WHAT_DOING1, (0, 0))
    pygame.display.update()
    pygame.time.delay(1000)


def draw_window_t():
    WIN.blit(TRUE_PIC, (0, 0))
    pygame.display.update()
    pygame.time.delay(7000)


def draw_window_f():
    WIN.blit(FALSE_PIC, (0, 0))
    pygame.display.update()
    pygame.time.delay(7000)


def main():
    pygame.key.stop_text_input()
    clock =pygame.time.Clock()
    run = True
    first_event = True
    count_down3 = True
    count_down2 = True
    count_down1 = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if first_event:
                INGUSH_SOUND.set_volume(0.045)
                INGUSH_SOUND.play()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and first_event:
                    chivis_yes = bool(random.getrandbits(1))
                    first_event = False
                    pygame.mixer.fadeout(3000)

                if not first_event:
                    draw_window_w3()
                    count_down3 = False
                    
                    

                if not first_event and not count_down3:
                    draw_window_w2()
                    count_down2 = False
                    
                    

                if not first_event and not count_down2:
                    draw_window_w1()
                    count_down1 = False
                    

                if chivis_yes and not first_event and not count_down1:
                    print('change to true pic')
                    TRUE_SOUND.play()
                    draw_window_t()
                    pygame.display.update()
                    pygame.quit()
                    sys.exit()
                    

                if not chivis_yes and not first_event and not count_down1:
                    print('change to false pic')
                    FALSE_SOUND.play()
                    draw_window_f()
                    pygame.display.update()
                    pygame.quit()
                    sys.exit()

                    
                    


        if first_event:
            draw_window_w()


if __name__ == '__main__':
    main()
