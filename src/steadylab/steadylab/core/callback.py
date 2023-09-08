import sys
from typing import Any

sys.path.append("src/steadylab/steadylab")

from core.processor import *


class CallBack:
    def __init__(self, name) -> None:
        self.name = name

    def __call__(self, msg) -> Any:
        pass


class ImageCallBack(CallBack):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.processor = ImageProcessor(name)

    def __call__(self, msg) -> Any:
        return self.processor(msg) 


class DepthCallBack(CallBack):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.processor = DepthProcessor(name)

    def __call__(self, msg) -> Any:
        return self.processor(msg)


class PoseCallBack(CallBack):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.processor = PoseProcessor(name)

    def __call__(self, msg) -> Any:
        return self.processor(msg)


class PathMapCallBack(CallBack):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.processor = PathMapProcessor(name)

    def __call__(self, msg) -> Any:
        return self.processor(msg)


class PointCloudCallBack(CallBack):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.processor = PointCloudProcessor(name)

    def __call__(self, msg) -> Any:
        return self.processor(msg)


class IMUCallBack(CallBack):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.processor = IMUProcessor(name)

    def __call__(self, msg) -> Any:
        return self.processor(msg)


class TFCallBack(CallBack):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.processor = TFProcessor(name)

    def __call__(self, msg) -> Any:
        return self.processor(msg)
