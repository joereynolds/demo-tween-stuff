from src.components.tween.tween import Tween
import src.config.events as e
import src.components.tween.ease as easee
import src.graphics as g
from src.components.tween.request import TweenRequest


class TweensOnEvent:
    """
    Tweens an entity upon receiving an event
    """

    def __init__(
        self,
        parent,
        event: str,
        start: float,
        end: float,
        tween_type: str,
        duration: float = 0.25,
        direction: str = "forward",
        ease: str = "linear",
    ):
        self.parent = parent
        self.should_tween = False
        self.event = e.events[event]

        self.tween = Tween(
            parent,
            [
                {
                    "type": tween_type,
                    "tween_args": {
                        "start": start,
                        "end": end,
                        "duration": duration,
                        "ease": easee.proxy(ease),
                        "direction": direction,
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
