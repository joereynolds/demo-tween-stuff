from pygame import Vector2

from src.components.tween.request import TweenRequest
from src.components.tween.types.base_tween import BaseTween


class AnimationSpeed(BaseTween):
    def __init__(
        self,
        parent,
        request: TweenRequest,
    ):
        super().__init__(parent, request)
        self.animates = None

    def tween_update(self, progress):
        if not self.animates:
            self.animates = self.parent.get_component("animates")

            self.start = self.animates.speed
            self.end = self.animates.speed * 4

        position = self.start + (self.end - self.start) * progress

        self.animates.set_speed(position)

    def tween_reset(self):
        self.animates.set_speed(self.start)

    def tween_complete(self):
        self.is_complete = True
        self.animates.play = False

    def particle_reset(self, dt, level, player, events):
        pass
