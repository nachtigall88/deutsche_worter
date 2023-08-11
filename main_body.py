"""модуль для описання головної логіки роботи застосунку"""
import random
from random import randint


class SingleWord:
    def __init__(self, word, translation, article=None):
        self.article = article
        self.word = word
        self.translation = translation

    def __str__(self):
        if self.article:
            return f'{self.article} {self.word} : {self.translation}'
        else:
            return f'{self.word} : {self.translation}'


class WordBase:
    _RANDOM_WORD = None
    my_txt_base = 'word base.txt'

    def __call__(self, data):
        return self.add_word_to_base(data)

    def __init__(self):
        self.make_txt_base()

    def __str__(self):
        return f"{(self._RANDOM_WORD)}"

    def make_txt_base(self):
        if not self.my_txt_base:
            with open(self.my_txt_base, 'w',encoding='UTF-8') as file:
                return

    def get_random_word(self):
        with open(self.my_txt_base, 'r') as file:
            seq = [x for x in file.readlines()]
            res = seq[randint(0, len(seq) - 1)]
            self._RANDOM_WORD = res
        return self._RANDOM_WORD


    def add_word_to_base(self, data:'SingleWord'):
        with open(self.my_txt_base, 'a') as file:
            if not self.check_if_in(data, file):
                file.write(f'{data.article}, {data.word}, {data.translation}\n')


    def check_if_in(self, data, base):
        with open(base, 'r'):
            return any(map(lambda x: data.word in x, base.readlines()))

if __name__ == '__main__':
    wb = WordBase()
    sw = SingleWord('Buch', 'книга', 'das')
    sw1 = SingleWord('Kugel', 'куля', 'das')
    sw2 = SingleWord('Madchen', 'дівча', 'das')
    sw3 = SingleWord('Lehrer', 'книга', 'der')
    sw4 = SingleWord('richtig', 'вірно')
    print(sw)
    wb(sw)
    wb(sw1)
    wb(sw2)
    wb(sw3)
    wb(sw4)
    wb.get_random_word()
    print(wb)
