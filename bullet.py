
import pygame, math
class Bullet(pygame.sprite.Sprite):
    def __init__(self, ship):
        super().__init__()
        self.image = pygame.Surface((4,4))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center=ship.rect.center)
        rad=math.radians(ship.angle)
        self.vel=pygame.Vector2(math.cos(rad),-math.sin(rad))*8
    def update(self):
        self.rect.center+=self.vel
        if not pygame.display.get_surface().get_rect().collidepoint(self.rect.center):
            self.kill()
