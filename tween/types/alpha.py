from src.components.tween.request import TweenRequest
from src.components.tween.types.base_tween import BaseTween


class Alpha(BaseTween):
    def __init__(self, parent, request: TweenRequest):
        super().__init__(parent, request)

        self.start = int(request.start)
        self.end = int(request.end)

    def tween_update(self, progress):
        alpha = self.start + (self.end - self.start) * progress
        self.parent.image.set_alpha(alpha)

    def tween_reset(self):
        self.parent.image.set_alpha(self.start)

    def tween_complete(self):
        self.parent.image.set_alpha(self.end)

    def particle_reset(self, dt: float, level, player, events: list):
        self.elapsed = 0
        self.is_complete = False
        self.tween_reset()
