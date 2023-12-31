"""модуль для описання головної логіки роботи застосунку"""
import random
from random import randint
# from frontend_body import *

class SingleWord:
    """
    клас для опису блока даних для запису в базу даних
    """

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
    """
    клас для опису логіки створення текстового документу (бази даних),
    отримання рандомного слова із словника, додавання даних до бази даних
    """
    _RANDOM_WORD = None
    my_txt_base = 'word base.txt'

    def __call__(self, data):
        """
        дозволяє викликати екземпляр класу як функцію з аргументом-екземпляром класу SingleWord
        :param data: SingleWord instance
        :return: WordBase.add_word_to_base(data)
        """
        self.add_word_to_base(data)

    def __init__(self):
        """
        створює базу даних під час створення екземляра класу
        """
        self.make_txt_base()

    def __str__(self):
        return f"{(self._RANDOM_WORD)}"

    def make_txt_base(self):
        """
        створює файл-базу даних для зберігання і використання даних
        :return:
        """
        try:
            with open(self.my_txt_base, 'x', encoding='UTF-8') as file:
                return
        except FileExistsError:
            pass

    def get_random_word(self):
        """
        функція для отримання рандомної інформації з бази даних
        :return:
        """
        with open(self.my_txt_base, 'r') as file:
            seq = [x for x in file.readlines()]
            res = seq[randint(0, len(seq) - 1)]
            self._RANDOM_WORD = res
        return self._RANDOM_WORD

    def add_word_to_base(self, data: SingleWord):
        """
        функція для додавання інформації у базу даних
        :param data: SingleWord instance
        :return:
        """
        with open(self.my_txt_base, 'a') as file:
            res = f'{data.article}, {data.word}, {data.translation}\n'
            file.writelines(res)



# if __name__ == '__main__':
#     rule_entries()

