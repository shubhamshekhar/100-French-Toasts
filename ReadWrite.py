import pandas
import random


class ReadWrite:
    def __init__(self):
        try:
            self.data = pandas.read_csv("data/words_to_learn.csv")
        except FileNotFoundError:
            self.data = pandas.read_csv("data/french_words.csv")
        finally:
            self.to_learn = self.data.to_dict(orient="records")

    def get_random_index(self):
        pass

    def get_random_french_word(self):
        return random.choice(self.to_learn)

    def remove_word_from_dict(self, word):
        self.to_learn.remove(word)
        self.save_unknown_word_to_csv()

    def save_unknown_word_to_csv(self):
        words = pandas.DataFrame(self.to_learn)
        words.to_csv("data/words_to_learn.csv", index=False)


