
import pygame, math, random
from entities.bullet import Bullet
from settings import Settings

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40,30), pygame.SRCALPHA)
        pygame.draw.polygon(self.image,(200,200,255),[(0,30),(20,0),(40,30)])
        self.rect = self.image.get_rect(center=(450,300))
        self.pos = pygame.Vector2(self.rect.center)
        self.vel = pygame.Vector2()
        self.angle = 0
        self.lives = 3
        self.score = 0

    def handle_input(self, bullets, joystick):
        keys = pygame.key.get_pressed()

        if joystick:
            x = joystick.get_axis(0)
            y = joystick.get_axis(1)
            if abs(x) > Settings.DEADZONE:
                self.angle -= x*4
            if abs(y) > Settings.DEADZONE:
                rad=math.radians(self.angle)
                self.vel += pygame.Vector2(math.cos(rad),-math.sin(rad))*(-y*0.3)
            if joystick.get_button(0):
                bullets.add(Bullet(self))
        else:
            if keys[pygame.K_LEFT]: self.angle+=4
            if keys[pygame.K_RIGHT]: self.angle-=4
            if keys[pygame.K_UP]:
                rad=math.radians(self.angle)
                self.vel+=pygame.Vector2(math.cos(rad),-math.sin(rad))*0.3
            if keys[pygame.K_SPACE]:
                bullets.add(Bullet(self))

    def update(self):
        self.vel*=0.98
        self.pos+=self.vel
        self.rect.center=self.pos

    def draw(self, screen, offset):
        r=pygame.transform.rotate(self.image,self.angle)
        rect=r.get_rect(center=self.rect.center)
        rect.x+=offset[0]; rect.y+=offset[1]
        screen.blit(r,rect)
