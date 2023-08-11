"""модуль для описання головної логіки роботи застосунку"""


class WordBase:
    _RANDOM_WORD = list()
    my_txt_base = 'word base.txt'

    def __init__(self):
        self.make_txt_base()

    def __str__(self):
        return f"{(self._RANDOM_WORD)}"

    def make_txt_base(self):
        with open(self.my_txt_base, encoding='UTF-8') as file:
            pass

    def get_random_word(self):
        pass

    def add_word_to_base(self, data):
        with open(self.my_txt_base, 'a') as file:
            file.write(data)



if __name__ == '__main__':
    w = WordBase()
