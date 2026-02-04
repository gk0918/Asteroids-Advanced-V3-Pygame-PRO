
import pygame
class Audio:
    shoot = None
    explode = None

    @staticmethod
    def load():
        Audio.shoot = pygame.mixer.Sound("sounds/shoot.wav")
        Audio.explode = pygame.mixer.Sound("sounds/explode.wav")

    @staticmethod
    def play(sound, x):
        pan = max(-1,min(1,(x-450)/450))
        left = 1-pan if pan<0 else 1
        right = 1+pan if pan>0 else 1
        sound.set_volume(left*0.5,right*0.5)
        sound.play()
