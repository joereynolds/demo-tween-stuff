import pygame
import src.config.events as e
import src.components.tween.factory as tween_factory


from typing import List


class Tween:
    def __init__(self, parent, tweens: list[dict] = [], play_type: str = "sequential"):
        self.parent = parent
        self.tweens = [
            tween_factory.build(tween["type"], parent, tween["tween_args"])
            for tween in tweens
        ]

        for tween in self.tweens:
            if tween.request.direction == "backward":
                tween.start, tween.end = tween.end, tween.start

        # Keep this to maintain what's complete so we don't
        # process extra stuff and spam the event queue
        self.completed_tweens = set()

    def update(self, dt: float, level, player, events: list):
        for tween in self.tweens:
            if tween in self.completed_tweens:
                continue

            if tween.is_complete:
                self.completed_tweens.add(tween)
                pygame.event.post(
                    pygame.event.Event(
                        e.events[tween.event], {"entity_id": self.parent.id}
                    )
                )

            tween.update(dt, level, player, events)

    def particle_reset(self, dt: float, level, player, events: list) -> None:
        for tween in self.tweens:
            tween.particle_reset(dt, level, player, events)
