from typing import TypeVar

T = TypeVar('T', bound='WordFrequency')


class WordFrequency:
    def __init__(self, word: str, frequency: int):
        self.word = word
        self.frequency = frequency

    def __eq__(self, other: T) -> bool:
        return other.word == self.word and other.frequency == self.frequency
