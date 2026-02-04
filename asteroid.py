
import pygame, random, math
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((50,50),pygame.SRCALPHA)
        pygame.draw.circle(self.image,(120,120,120),(25,25),25)
        self.rect=self.image.get_rect(center=(random.randint(0,900),random.randint(0,600)))
        a=random.uniform(0,360)
        self.vel=pygame.Vector2(math.cos(math.radians(a)),math.sin(math.radians(a)))*2
    def update(self):
        self.rect.center+=self.vel
        self.rect.centerx%=900
        self.rect.centery%=600
