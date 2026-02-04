
import random
class Camera:
    def __init__(self):
        self.shake = 0
    def trigger(self, amount):
        self.shake = amount
    def offset(self):
        if self.shake > 0:
            self.shake -= 1
            return random.randint(-4,4), random.randint(-4,4)
        return 0,0
