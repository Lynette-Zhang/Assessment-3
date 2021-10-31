import pygame, random
from pygame.locals import *


def print_text(src, font, x, y, text, color=(250,25,200)):
    imgText = font.render(text, True, color)
    src.blit(imgText, (x, y))

def game(screen, lives, score):
    rect_x, rect_y, rect_w, rect_h = 300, 460, 120, 40
    ball1_x, ball1_y = random.randint(30, 470), -50
    ball2_x, ball2_y = random.randint(30, 470), -50
    ball3_x, ball3_y = random.randint(30, 470), -50
    vel1_y = 2
    vel2_y = 2
    vel3_y = 3
    white = 255, 255, 255
    font = pygame.font.Font(None, 24)
    while lives:
        for event in pygame.event.get():
            if event.type == QUIT:
               pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    rect_x -= 50
                if event.key == K_RIGHT:
                    rect_x += 50
        screen.fill(white)

        if rect_x < 0:
            rect_x = 0
        elif rect_x > 600 - rect_w:
            rect_x = 600 - rect_w
        pygame.draw.rect(screen, (30, 0, 0), (rect_x, rect_y, rect_w, rect_h), 0)

        if ball1_y > 500:
            lives -= 1
            ball1_x, ball1_y = random.randint(30, 470), -50
        elif (rect_y - ball1_y) < 30 and ball1_x > rect_x and ball1_x < (rect_x + rect_w):
            score += 1
            vel1_y += score//5
            ball1_x, ball1_y = random.randint(30, 470), -50
        else:
            ball1_y += vel1_y
        pygame.draw.circle(screen, (120, 120, 150), (ball1_x, ball1_y), 30, 0)

        if ball2_y > 500:
            lives += 0
            ball2_x, ball2_y = random.randint(30, 470), -50
        elif (rect_y - ball2_y) < 30 and ball2_x > rect_x and ball2_x < (rect_x + rect_w):
            score -= 1
            vel2_y += score//5
            ball2_x, ball2_y = random.randint(30, 470), -50
        else:
            ball2_y += vel2_y
        pygame.draw.circle(screen, (255, 120, 120), (ball2_x, ball2_y), 30, 0)

        if ball3_y > 500:
            lives += 0
            ball3_x, ball3_y = random.randint(30, 470), -50
        elif (rect_y - ball3_y) < 30 and ball3_x > rect_x and ball3_x < (rect_x + rect_w):
            score += 3
            vel3_y += score//5
            ball3_x, ball3_y = random.randint(30, 470), -50
        else:
            ball3_y += vel3_y
        pygame.draw.circle(screen, (100, 255, 200), (ball3_x, ball3_y), 30, 0)

        print_text(screen, font, 20, 0, "lives:" + str(lives))
        print_text(screen, font, 500, 0, "score:" + str(score))
        pygame.display.update()
        pygame.time.delay(10)

    return lives, score

def main():
    pygame.init()
    pygame.display.set_caption("Watch your Catch")
    screen = pygame.display.set_mode((600, 500))
    lives = 5
    score = 0
    font2 = pygame.font.Font(None, 24)
    while True:
        lives, score = game(screen, lives, score)
        for event in pygame.event.get():
            if event.type == QUIT:
               pygame.quit()
            if event.type == MOUSEBUTTONUP:
                lives = 5
                score = 0
        screen.fill((255, 255, 255))
        print_text(screen, font2, 200, 200, "score:"+str(score)+"...GAME OVER!...")
        pygame.display.update()
main()