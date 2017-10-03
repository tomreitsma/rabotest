import unittest

from word_frequency import WordFrequency
from word_frequency_analyzer import WordFrequencyAnalyzer


class TestWordFrequencyAnalyzer(unittest.TestCase):
    TEXT = '- A favorite copy set by writing teachers for their pupils is the following, ' \
           'because it contains every letter of the alphabet: "A quick brown fox jumps over the lazy dog"'

    def test_calculate_highest_frequency(self):
        wfa = WordFrequencyAnalyzer()

        self.assertEqual(wfa.calculate_highest_frequency(self.TEXT), 3)

    def test_calculate_frequency_for_word(self):
        wfa = WordFrequencyAnalyzer()
        word = "The"

        self.assertEqual(wfa.calculate_frequency_for_word(self.TEXT, word), 3)

    def test_calculate_most_frequent_n_words(self):
        wfa = WordFrequencyAnalyzer()
        number = 3

        self.assertEqual(
            wfa.calculate_most_frequent_n_words(self.TEXT, number),
            [
                WordFrequency('the', 3),
                WordFrequency('a', 2),
                WordFrequency('favorite', 1)
            ]
        )

if __name__ == '__main__':
    unittest.main()
