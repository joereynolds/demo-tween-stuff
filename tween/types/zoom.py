from src.components.tween.request import TweenRequest
from src.components.tween.types.base_tween import BaseTween


class Zoom(BaseTween):
    def __init__(
        self,
        parent,
        request: TweenRequest,
    ):
        super().__init__(parent, request)
        self.start = request.start
        self.end = request.end

    def tween_update(self, progress):
        position = self.start + (self.end - self.start) * progress
        self.parent.level.layer.zoom = position

    def tween_reset(self):
        self.parent.level.layer.zoom = self.start

    def tween_complete(self):
        self.is_complete = True
        self.parent.level.layer.zoom = self.end

    def particle_reset(self, dt, level, player, events):
        pass
