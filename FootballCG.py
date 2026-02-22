
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Penalty Shoot Game")

WHITE = (255,255,255)
GREEN = (30,160,60)
BLACK = (0,0,0)
RED = (220,50,50)
BLUE = (50,80,220)
YELLOW = (255,220,0)
SKIN = (255,220,180)

clock = pygame.time.Clock()

def draw_bresenham(x1,y1,x2,y2,color):
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    sx = 1 if x1<x2 else -1
    sy = 1 if y1<y2 else -1
    err = dx-dy

    while True:
        if 0 <= x1 < WIDTH and 0 <= y1 < HEIGHT:
            screen.set_at((x1,y1), color)
        if x1==x2 and y1==y2:
            break
        e2 = 2*err
        if e2>-dy:
            err-=dy
            x1+=sx
        if e2<dx:
            err+=dx
            y1+=sy

def draw_circle(cx,cy,r,color):
    x=0
    y=r
    p=1-r

    def plot(x,y):
        pts=[
            (cx+x,cy+y),(cx-x,cy+y),
            (cx+x,cy-y),(cx-x,cy-y),
            (cx+y,cy+x),(cx-y,cy+x),
            (cx+y,cy-x),(cx-y,cy-x)
        ]
        for pt in pts:
            if 0<=pt[0]<WIDTH and 0<=pt[1]<HEIGHT:
                screen.set_at(pt,color)

    while x<=y:
        plot(x,y)
        x+=1
        if p<0:
            p+=2*x+1
        else:
            y-=1
            p+=2*(x-y)+1

ball_x = WIDTH//2
ball_y = 450
start_x = WIDTH//2
start_y = 450

target_x = ball_x
moving = False

keeper_x = WIDTH//2
keeper_dir = 3

score = 0
font = pygame.font.SysFont(None,36)

running=True
while running:
    screen.fill(GREEN)

    draw_bresenham(0,500,WIDTH,500,WHITE)

    draw_bresenham(250,200,650,200,WHITE)
    draw_bresenham(250,200,250,350,WHITE)
    draw_bresenham(650,200,650,350,WHITE)

    draw_circle(WIDTH//2,480,12,BLUE)

    keeper_x += keeper_dir
    if keeper_x <= 280 or keeper_x >= 620:
        keeper_dir *= -1

    pygame.draw.rect(screen, BLUE, (keeper_x-15, 240, 30, 50))
    draw_circle(int(keeper_x), 220, 12, SKIN)
    pygame.draw.rect(screen, SKIN, (keeper_x-35, 245, 20, 8))
    pygame.draw.rect(screen, SKIN, (keeper_x+15, 245, 20, 8))

    if moving:
        ball_y -= 8
        ball_x += (target_x-ball_x)*0.1

        if ball_y < 240:
            moving=False

            if abs(ball_x - keeper_x) > 35:
                score += 1

            ball_x = start_x
            ball_y = start_y

    draw_circle(int(ball_x),int(ball_y),8,YELLOW)

    txt = font.render(f"Score: {score}",True,WHITE)
    screen.blit(txt,(20,20))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.MOUSEBUTTONDOWN and not moving:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if 250 < mouse_x < 650 and 200 < mouse_y < 350:
                target_x = mouse_x
                moving = True

    pygame.display.flip()
    clock.tick(60)

pygame.quit()