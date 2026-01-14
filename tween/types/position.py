from pygame import Vector2

from src.components.tween.request import TweenRequest
from src.components.tween.types.base_tween import BaseTween


class Position(BaseTween):
    def __init__(
        self,
        parent,
        request: TweenRequest,
    ):
        super().__init__(parent, request)
        self.start = Vector2(request.start)
        self.end = Vector2(request.end)

    def tween_update(self, progress):
        position = self.start + (self.end - self.start) * progress
        self.parent.set_rect(position.x, position.y)

    def tween_reset(self):
        self.parent.set_rect(self.start.x, self.start.y)

    def tween_complete(self):
        self.is_complete = True
        self.parent.set_rect(self.end.x, self.end.y)

    def particle_reset(self, dt, level, player, events):
        pass
