class WordFrequency:
    def __init__(self, word: str, frequency: int):
        self.word = word
        self.frequency = frequency

    def __eq__(self, other):
        return other.word == self.word and other.frequency == self.frequency
