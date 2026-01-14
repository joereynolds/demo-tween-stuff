import pygame
import src.config.events as e

from abc import ABC, abstractmethod
from typing import List

from src.components.tween.request import TweenRequest


class BaseTween(ABC):
    def __init__(
        self,
        parent,
        request: TweenRequest,
    ):
        self.parent = parent
        self.request = request
        self.elapsed = 0
        self.is_complete = False

        # tween-position-complete event, tween-colour-complete-event etc...
        self.event = "tween-" + type(self).__name__.lower() + "-complete-event"

    def update(self, dt: float, level, player, events: list) -> None:
        self.elapsed += dt
        progress = min(self.elapsed / self.request.duration, 1)

        eased_progress = self.request.ease(progress)

        if progress >= 1:
            if self.request.direction == "pingpong":
                self.elapsed = 0
                self.request.reverse_direction = not self.request.reverse_direction

                if self.request.reverse_direction:
                    temp = self.start
                    self.start = self.end
                    self.end = temp
                else:
                    temp = self.start
                    self.start = self.end
                    self.end = temp

                    # By default don't emit events on pingpong complete,
                    # it's noisy. Allow each tween to set it if necessary
                    if self.request.emit_event_on_ping_pong_complete:
                        pygame.event.post(
                            pygame.event.Event(
                                e.events[self.event], {"entity_id": self.parent.id}
                            )
                        )

                self.tween_reset()
                return
            else:
                self.is_complete = True
                self.tween_complete()
                return

        self.tween_update(eased_progress)

    @abstractmethod
    def tween_reset(self):
        pass

    @abstractmethod
    def tween_complete(self):
        pass

    @abstractmethod
    def tween_update(self, progress):
        pass
