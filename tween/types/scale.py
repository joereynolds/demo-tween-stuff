import pygame

from src.components.tween.request import TweenRequest
from src.components.tween.types.base_tween import BaseTween


class Scale(BaseTween):
    def __init__(self, parent, request: TweenRequest):
        super().__init__(parent, request)
        self.start = request.start
        self.end = request.end

        self.original_size = self.parent.image.copy()
        self.cache = {}

    def tween_update(self, progress):
        cache = self.cache

        new_scale = self.start + (self.end - self.start) * progress

        # Round it so we have fewer values to cache
        new_scale = round(new_scale, 2)

        if new_scale < 0:
            return

        if new_scale not in cache:
            cache[new_scale] = pygame.transform.scale_by(
                self.original_size,
                new_scale
            )

        self.parent.image = cache[new_scale]

    def tween_reset(self):
        pass

    def tween_complete(self):
        pass

    def particle_reset(self, dt: float, level, player, events: list):
        self.elapsed = 0
        self.is_complete = False
