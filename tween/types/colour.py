import pygame

from src.components.tween.request import TweenRequest
from src.components.tween.types.base_tween import BaseTween


class Colour(BaseTween):
    def __init__(self, parent, request: TweenRequest):
        super().__init__(parent, request)
        self.start = pygame.Color(request.start)
        self.end = pygame.Color(request.end)

    def tween_update(self, progress):
        lerped_colour = self.start.lerp(self.end, progress)
        self.parent.image.fill(lerped_colour)

    def tween_reset(self):
        self.parent.image.fill(self.start)

    def tween_complete(self):
        self.parent.image.fill(self.end)

    def particle_reset(self, dt, level, player, events):
        self.elapsed = 0
        self.is_complete = False
        self.parent.image.fill(self.start)
