import re
from collections import Counter

from word_frequency import WordFrequency


class WordFrequencyAnalyzer:
    def _normalize(self, text: str) -> str:
        """
        Normalize the word for processing. In this case only making everything lowercase is sufficient.
        :param text:
        :return:
        """

        return text.lower()

    def _normalize_many(self, text: list) -> tuple:
        """
        Takes a list of strings and returns them normalized in a tuple
        :param text:
        :return tuple:
        """
        return tuple([
            word.lower() for word in text
        ])

    def _get_words_from_string(self, text: str) -> list:
        """
        Extracts individual words from a string and returns them in a list
        :param text:
        :return str:
        """
        words = re.findall(r'\w+', self._normalize(text))
        return words

    def calculate_highest_frequency(self, text: str) -> int:
        """
        Calculates the most common word and returns the number that's most common
        :param text:
        :return:
        """
        word_counter = Counter(self._get_words_from_string(text))

        try:
            most_common = word_counter.most_common(1)[0][1]
        except IndexError:
            return 0

        return most_common

    def calculate_frequency_for_word(self, text: str, word: str) -> tuple:
        """
        Calculates the amount of times a word occurs in a given text
        :param text:
        :param word:
        :return:
        """
        text, word = self._normalize_many([text, word])
        word_counter = Counter(self._get_words_from_string(text))

        return word_counter[word]

    def calculate_most_frequent_n_words(self, text: str, n: int) -> list:
        """
        Calculates the top <n> most frequent words in <text>
        :param text:
        :param n:
        :return:
        """
        word_counter = Counter(self._get_words_from_string(text))
        return [
            WordFrequency(word, frequency) for word, frequency in word_counter.most_common(n)
        ]
