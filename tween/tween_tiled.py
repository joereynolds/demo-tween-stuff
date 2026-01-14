from typing import List
import src.components.tween.ease as easee
from src.components.tween.tween import Tween
import src.config.events as e


class TweenTiled:
    """A wrapper so we can use our tween stuff via components"""

    def __init__(
        self,
        parent,
        start: float,
        end: float,
        tween_type: str,
        duration: float = 0.25,
        direction: str = "forward",
        ease: str = "linear",
    ):
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

    def update(self, dt: float, level, player, events: list):
        self.tween.update(dt, level, player, events)
