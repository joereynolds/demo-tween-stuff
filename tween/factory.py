import sys
from src.components.tween.request import TweenRequest

# These need to be here. They're dynamically loaded in at the bottom, magic...
from src.components.tween.types.alpha import Alpha
from src.components.tween.types.animation_speed import AnimationSpeed
from src.components.tween.types.colour import Colour
from src.components.tween.types.image_rect import ImageRect
from src.components.tween.types.position import Position
from src.components.tween.types.zoom import Zoom
from src.components.tween.types.scale import Scale


def build(tween, parent, tween_args):
    # Builds a tween from kebab-case into TitleCase.
    # For example 'animation-speed' becomes AnimationSpeed
    tween_class = "".join([word.title() for word in tween.split("-")])
    return getattr(sys.modules[__name__], tween_class)(parent, TweenRequest(**tween_args))
