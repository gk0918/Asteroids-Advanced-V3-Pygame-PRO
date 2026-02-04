
import pygame, sys
from settings import Settings
from entities.ship import Ship
from entities.asteroid import Asteroid
from utils.camera import Camera
from utils.particles import Particle
from utils.time import Time
from utils.audio import Audio

pygame.init()
pygame.mixer.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0) if pygame.joystick.get_count() else None
if joystick: joystick.init()

screen=pygame.display.set_mode((Settings.WIDTH,Settings.HEIGHT))
clock=pygame.time.Clock()

ship=Ship()
bullets=pygame.sprite.Group()
asteroids=pygame.sprite.Group(Asteroid(),Asteroid(),Asteroid())
particles=pygame.sprite.Group()
camera=Camera()

Audio.load()

flash=0

while True:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit(); sys.exit()

    Time.update()

    ship.handle_input(bullets, joystick)
    ship.update()
    bullets.update()
    asteroids.update()
    particles.update()

    hits=pygame.sprite.groupcollide(bullets,asteroids,True,True)
    for a in hits.values():
        for ast in a:
            for _ in range(20):
                particles.add(Particle(ast.rect.center))
            camera.trigger(10)
            Time.slowmo(0.4,30)
            flash=6

    screen.fill((255,255,255) if flash>0 else Settings.BG)
    if flash>0: flash-=1

    ox,oy=camera.offset()
    for g in (asteroids,bullets,particles):
        for s in g:
            screen.blit(s.image,s.rect.move(ox,oy))
    ship.draw(screen,(ox,oy))

    pygame.display.flip()
    clock.tick(Settings.FPS*Time.scale)
