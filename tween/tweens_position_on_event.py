from src.components.tween.tween import Tween
from pygame.math import Vector2
from src.attributes import Attribute
import src.config.events as e
import src.components.tween.ease as ease_type
import src.graphics as g
from src.components.tween.request import TweenRequest


class TweensPositionOnEvent:
    """
    Tweens the position of an entity upon receiving event
    """

    def __init__(
        self,
        parent,
        request: TweenRequest,
        event: str
    ):
        self.parent = parent
        self.should_tween = False
        self.event = e.events[event]

        self.tween = Tween(
            self.parent,
            [
                {
                    "type": "position",
                    "tween_args": {
                        "start": request.start,
                        "end": request.end,
                        "duration": request.duration,
                        "ease": request.ease,
                        "direction": request.direction,
                    },
                }
            ],
        )

        self.parent.level.event_handler.register(self, self.event)

    def update(self, dt: float, level, player, events: list) -> None:
        if self.should_tween:
            self.tween.update(dt, level, player, events)

    def on_event(self, dt: float, level, player, event):
        if event.type == self.event:
            self.should_tween = True
