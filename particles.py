
import pygame, random, math
class Particle(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((3,3))
        self.image.fill((255,200,50))
        self.rect = self.image.get_rect(center=pos)
        a=random.uniform(0,360)
        self.vel=pygame.Vector2(math.cos(math.radians(a)),math.sin(math.radians(a)))*random.uniform(1,4)
        self.life=30
    def update(self):
        self.rect.center+=self.vel
        self.life-=1
        if self.life<=0: self.kill()
