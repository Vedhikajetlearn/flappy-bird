import pygame, pyautogui, time, random

w,h=pyautogui.size()
pygame.init()

background=pygame.transform.scale(pygame.image.load("bg.png"),(w,h))
ground=pygame.transform.scale(pygame.image.load("ground.png"),(w*1.5,h//4))

run=True
scrollground=0
screen=pygame.display.set_mode((w,h))

class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.index=0
        self.counter=0
        for i in range(3):
            img=pygame.image.load(f"bird{i+1}.png")
            self.images.append(img)

        self.image=self.images[0]
        self.rect=self.image.get_rect()
        self.rect.center=x,y
        self.velocity=0
        
    def update(self):
        self.velocity+=1
        if self.velocity>8:
            self.velocity=8
        if pygame.mouse.get_pressed()[0]:
            self.velocity=-10
        self.rect.y+=self.velocity            
        self.counter+=1
        if self.counter==10:
            
            self.index+=1
            if self.index>2:
                self.index=0
            self.image=self.images[self.index]
            self.counter=0
        
birdgroup=pygame.sprite.Group()
flappy=Bird(100,h/2)
birdgroup.add(flappy)
        
while run:
    screen.blit(background,(0,0))
    screen.blit(ground,(scrollground,h-h//4))
    birdgroup.draw(screen)
    birdgroup.update()
    scrollground-=10
    if scrollground<-w//2:
        scrollground=0
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit()
        
    pygame.display.update()