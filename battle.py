import pygame, pyautogui, time, random

w,h=pyautogui.size()
pygame.init()

background=pygame.transform.scale(pygame.image.load("nightsky.jpg"),(w,h))
ground=pygame.transform.scale(pygame.image.load("stone wallpng"),(w*1.5,h//4))
wizard=pygame.transform.scale(pygame.image.load("wizard.png"),(400,400))



run=True
scrollground=0
screen=pygame.display.set_mode((w,h))

while run:
    screen.blit(ground,(0,h-h//4))
    screen.blit(background,(0,scrollground))
    scrollground-=10
    if scrollground<-h//2:
        scrollground=0
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit()
        if e.type==pygame.KEYDOWN:
            if keys[pygame.K_LEFT]:
                wizard.x-=20
            if keys[pygame.K_RIGHT]:
                wizard.x+=20
        
    pygame.display.update()