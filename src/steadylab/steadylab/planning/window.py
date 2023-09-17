import numpy as np

class Window:
    def __init__(self, size=8) -> None:
        assert 4 < size <= 10
        self.windows = [1/s for s in range(1, size+1)]
        self.weights = [1.0 - 0.1*s for s in range(size)]

