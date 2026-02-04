
class Time:
    scale = 1.0
    timer = 0

    @classmethod
    def slowmo(cls, scale, frames):
        cls.scale = scale
        cls.timer = frames

    @classmethod
    def update(cls):
        if cls.timer > 0:
            cls.timer -= 1
            if cls.timer == 0:
                cls.scale = 1.0
