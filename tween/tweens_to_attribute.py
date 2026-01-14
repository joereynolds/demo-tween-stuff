from src.components.tween.tween import Tween
from pygame.math import Vector2
from src.attributes import Attribute
import src.components.tween.ease as ease_type
import src.graphics as g


class TweensToAttribute:
    """
    Tweens the position of an entity up to (but not including)
    the position of the tile that has `attribute`.

    The direction of where it searches for the tile
    is determined by the velocity component
    """

    def __init__(
        self,
        parent,
        duration: float = 5,
        direction: str = "forward",
        ease: str = "linear",
        attribute: str = Attribute.SOLID
    ):
        self.parent = parent

        self.duration = duration
        self.direction = direction
        self.ease = ease
        self.attribute = attribute

        self.loaded = False

    def preload(self):

        start = Vector2(
            self.parent.physics_rect.x,
            self.parent.physics_rect.y
        )

        end = self.get_end_position()

        self.tween = Tween(
            self.parent,
            [
                {
                    "type": "position",
                    "tween_args": {
                        "start": start,
                        "end": end,
                        "duration": self.duration,
                        "ease": ease_type.proxy(self.ease),
                        "direction": self.direction,
                    },
                }
            ],
        )

    def get_end_position(self) -> Vector2:
        velocity = self.parent.get_component('velocity').velocity
        tile_range = 12

        for i in range(tile_range):
            _x = self.parent.physics_rect.x + (velocity.x * i * g.tile_width)
            _y = self.parent.physics_rect.y + (velocity.y * i * g.tile_height)

            tiles = self.parent.level.get_occupying_tiles(_x, _y)

            for tile in tiles:
                if tile.has_attribute(self.attribute):
                    final_x = _x - (velocity.x * g.tile_width)
                    final_y = _y - (velocity.y * g.tile_height)

                    return Vector2(final_x, final_y)

        return Vector2(
            self.parent.physics_rect.x + (velocity.x * g.tile_width),
            self.parent.physics_rect.y + (velocity.y * g.tile_height)
        )

    def update(self, dt: float, level, player, events: list):
        if not self.loaded:
            self.preload()
            self.loaded = True

        self.tween.update(dt, level, player, events)
