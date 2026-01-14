import src.components.tween.ease as ease


class TweenRequest:
    # TODO - direction should be enum
    # Direction can be (forward, backward)
    def __init__(
        self, start, end, duration, direction: str = "forward", ease=ease.in_out_elastic
    ):
        self.start = start
        self.end = end
        self.duration = duration
        self.direction = direction
        self.ease = ease

        # For pingpong stuff
        self.reverse_direction = False
        self.emit_event_on_ping_pong_complete = False
