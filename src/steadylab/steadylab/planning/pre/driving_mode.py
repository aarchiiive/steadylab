from enum import Enum, auto


class DrivingMode(Enum):
    CRUISING = auto()
    RIGHT_TURN = auto()
    COMPLEX_AREA = auto()
    UTURN = auto()
    TOLLGATE = auto()
    TUNNEL = auto()
    STATIC_OBSTACLE = auto()
    DYNAMIC_OBSTACLE = auto()