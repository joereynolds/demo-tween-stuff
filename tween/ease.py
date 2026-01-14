import math


# To call it via Tiled. I hate it just as much as you
def proxy(ease_type):
    ease_map = {
        "linear": linear,
        "in_quad": in_quad,
        "out_quad": out_quad,
        "in_out_quad": in_out_quad,
        "in_cubic": in_cubic,
        "out_cubic": out_cubic,
        "in_out_cubic": in_out_cubic,
        "in_quart": in_quart,
        "out_quart": out_quart,
        "in_out_quart": in_out_quart,
        "in_quint": in_quint,
        "out_quint": out_quint,
        "in_out_quint": in_out_quint,
        "in_sine": in_sine,
        "out_sine": out_sine,
        "in_out_sine": in_out_sine,
        "in_expo": in_expo,
        "out_expo": out_expo,
        "in_out_expo": in_out_expo,
        "in_circ": in_circ,
        "out_circ": out_circ,
        "in_out_circ": in_out_circ,
        "in_elastic": in_elastic,
        "out_elastic": out_elastic,
        "in_out_elastic": in_out_elastic,
        "in_back": in_back,
        "out_back": out_back,
        "in_out_back": in_out_back,
        "out_bounce": out_bounce,
    }

    return ease_map[ease_type]


def linear(progress):
    return progress


def in_quad(progress):
    return progress * progress


def out_quad(progress):
    return -1.0 * progress * (progress - 2.0)


def in_out_quad(progress):
    p = progress * 2
    if p < 1:
        return 0.5 * p * p
    p -= 1.0
    return -0.5 * (p * (p - 2.0) - 1.0)


def in_cubic(progress):
    return progress * progress * progress


def out_cubic(progress):
    p = progress - 1.0
    return p * p * p + 1.0


def in_out_cubic(progress):
    p = progress * 2
    if p < 1:
        return 0.5 * p * p * p
    p -= 2
    return 0.5 * (p * p * p + 2.0)


def in_quart(progress):
    return progress * progress * progress * progress


def out_quart(progress):
    p = progress - 1.0
    return -1.0 * (p * p * p * p - 1.0)


def in_out_quart(progress):
    p = progress * 2
    if p < 1:
        return 0.5 * p * p * p * p
    p -= 2
    return -0.5 * (p * p * p * p - 2.0)


def in_quint(progress):
    return progress * progress * progress * progress * progress


def out_quint(progress):
    p = progress - 1.0
    return p * p * p * p * p + 1.0


def in_out_quint(progress):
    p = progress * 2
    if p < 1:
        return 0.5 * p * p * p * p * p
    p -= 2.0
    return 0.5 * (p * p * p * p * p + 2.0)


def in_sine(progress):
    return -1.0 * math.cos(progress * (math.pi / 2.0)) + 1.0


def out_sine(progress):
    return math.sin(progress * (math.pi / 2.0))


def in_out_sine(progress):
    return -0.5 * (math.cos(math.pi * progress) - 1.0)


def in_expo(progress):
    if progress == 0:
        return 0.0
    return pow(2, 10 * (progress - 1.0))


def out_expo(progress):
    if progress == 1.0:
        return 1.0
    return -pow(2, -10 * progress) + 1.0


def in_out_expo(progress):
    if progress == 0:
        return 0.0
    if progress == 1.0:
        return 1.0
    p = progress * 2
    if p < 1:
        return 0.5 * pow(2, 10 * (p - 1.0))
    p -= 1.0
    return 0.5 * (-pow(2, -10 * p) + 2.0)


def in_circ(progress):
    return -1.0 * (math.sqrt(1.0 - progress * progress) - 1.0)


def out_circ(progress):
    p = progress - 1.0
    return math.sqrt(1.0 - p * p)


def in_out_circ(progress):
    p = progress * 2
    if p < 1:
        return -0.5 * (math.sqrt(1.0 - p * p) - 1.0)
    p -= 2.0
    return 0.5 * (math.sqrt(1.0 - p * p) + 1.0)


def in_elastic(progress):
    p = 0.3
    s = p / 4.0
    q = progress
    if q == 1:
        return 1.0
    q -= 1.0
    return -(pow(2, 10 * q) * math.sin((q - s) * (2 * math.pi) / p))


def out_elastic(progress):
    p = 0.3
    s = p / 4.0
    q = progress
    if q == 1:
        return 1.0
    return pow(2, -10 * q) * math.sin((q - s) * (2 * math.pi) / p) + 1.0


def in_out_elastic(progress):
    p = 0.3 * 1.5
    s = p / 4.0
    q = progress * 2
    if q == 2:
        return 1.0
    if q < 1:
        q -= 1.0
        return -0.5 * (pow(2, 10 * q) * math.sin((q - s) * (2.0 * math.pi) / p))
    else:
        q -= 1.0
        return pow(2, -10 * q) * math.sin((q - s) * (2.0 * math.pi) / p) * 0.5 + 1.0


def in_back(progress):
    return progress * progress * ((1.70158 + 1.0) * progress - 1.70158)


def out_back(progress):
    p = progress - 1.0
    return p * p * ((1.70158 + 1) * p + 1.70158) + 1.0


def in_out_back(progress):
    p = progress * 2.0
    s = 1.70158 * 1.525
    if p < 1:
        return 0.5 * (p * p * ((s + 1.0) * p - s))
    p -= 2.0
    return 0.5 * (p * p * ((s + 1.0) * p + s) + 2.0)


def out_bounce(x: float) -> float:
    """
    Implements the easeOutBounce easing function.

    Args:
        x: The input value (typically between 0 and 1).

    Returns:
        The eased output value.
    """
    n1 = 7.5625
    d1 = 2.75

    if x < 1 / d1:
        return n1 * x * x
    elif x < 2 / d1:
        return n1 * (x - 1.5 / d1) * (x - 1.5 / d1) + 0.75
    elif x < 2.5 / d1:
        return n1 * (x - 2.25 / d1) * (x - 2.25 / d1) + 0.9375
    else:
        return n1 * (x - 2.625 / d1) * (x - 2.625 / d1) + 0.984375
