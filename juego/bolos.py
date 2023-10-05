from dataclasses import dataclass, field
from abc import ABC, abstractmethod


@dataclass
class Roll:
    pins: int


@dataclass
class Frame(ABC):
    rolls: list[Roll] = field(default_factory=list)

    def is_strike(self) -> bool:
        return self.rolls[0].pins == 10

    def is_spare(self) -> bool:
        return self.rolls[0].pins + self.rolls[1].pins == 10

    @abstractmethod
    def add_roll(self, pins: int):
        raise NotImplementedError

    @abstractmethod
    def score(self) -> int:
        raise NotImplementedError


class NormalFrame(Frame):
    def __init__(self):
        super().__init__()


class TenthFrame(Frame):
    pass


class Game:
    FRAMES_TOTALES = 10
