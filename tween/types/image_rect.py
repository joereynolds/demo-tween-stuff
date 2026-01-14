from pygame import Vector2

from src.components.tween.request import TweenRequest
from src.components.tween.types.base_tween import BaseTween


class ImageRect(BaseTween):
    """
    Tweens the image rect offset from the physics rect.
    This allows the visual image to move independently from the physics position

    The start and end vectors represent offsets (x, y) from the physics_rect.
    For example, Vector2(0, -5) would offset the image 5 pixels up from the physics position.
    """

    def __init__(
        self,
        parent,
        request: TweenRequest,
    ):
        start_as_list = list(map(int, request.start.strip().split(',')))
        end_as_list = list(map(int, request.end.strip().split(',')))

        request.start = Vector2(*start_as_list)
        request.end = Vector2(*end_as_list)
        request.emit_event_on_ping_pong_complete = True

        super().__init__(parent, request)
        self.start = request.start
        self.end = request.end

    def tween_update(self, progress):
        offset = self.start + (self.end - self.start) * progress

        self.parent.rect.x = self.parent.physics_rect.x + offset.x
        self.parent.rect.y = self.parent.physics_rect.y + offset.y

    def tween_reset(self):
        self.parent.rect.x = self.parent.physics_rect.x + self.start.x
        self.parent.rect.y = self.parent.physics_rect.y + self.start.y

    def tween_complete(self):
        self.is_complete = True
        self.parent.rect.x = self.parent.physics_rect.x + self.end.x
        self.parent.rect.y = self.parent.physics_rect.y + self.end.y

    def particle_reset(self, dt, level, player, events):
        pass
