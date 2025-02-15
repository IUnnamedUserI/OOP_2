#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать электронный словарь, который хранит карточки с иностранными
словами и их переводами, ограничивает их количество (size), поддерживает
добавление, удаление, поиск переводов, операции объединения, пересечения
и разности словарей, а также исключает дубли.
"""


class WordCard:
    def __init__(self, foreign_word, translation):
        """
        Конструктор карточки иностранного слова.
        """
        self.foreign_word = foreign_word
        self.translation = translation

    def __eq__(self, other):
        """
        Проверяет равенство двух карточек по иностранному слову.
        """
        if isinstance(other, WordCard):
            return self.foreign_word == other.foreign_word
        return False

    def __hash__(self):
        """
        Хеш-функция для поддержки операций с множествами.
        """
        return hash(self.foreign_word)


class Dictionary:
    MAX_SIZE = 100

    def __init__(self, name, size=MAX_SIZE):
        """
        Конструктор класса Dictionary.
        """
        self.name = name
        self.size = min(size, self.MAX_SIZE)
        self.cards = []
        self.count = 0

    def size(self):
        """
        Возвращает установленную длину словаря.
        """
        return self.size

    def add_card(self, foreign_word, translation):
        """
        Добавляет карточку в словарь.
        """
        if self.count >= self.size:
            raise ValueError("Словарь переполнен")

        new_card = WordCard(foreign_word, translation)

        # Проверка на наличие дублей
        if new_card in self.cards:
            print(f"Слово '{foreign_word}' уже есть в словаре")
            return

        self.cards.append(new_card)
        self.count += 1

    def remove_card(self, foreign_word):
        """
        Удаляет карточку из словаря.
        """
        self.cards = [
            card for card in self.cards if card.foreign_word != foreign_word
        ]
        self.count = len(self.cards)

    def find_translation(self, foreign_word):
        """
        Ищет перевод для иностранного слова.
        """
        for card in self.cards:
            if card.foreign_word == foreign_word:
                return card.translation
        return None

    def __getitem__(self, foreign_word):
        """
        Перегрузка операции индексирования для поиска перевода.
        """
        return self.find_translation(foreign_word)

    def __setitem__(self, foreign_word, translation):
        """
        Перегрузка индексирования для добавления или обновления карточки.
        """
        for card in self.cards:
            if card.foreign_word == foreign_word:
                card.translation = translation
                return
        self.add_card(foreign_word, translation)

    def __add__(self, other):
        """
        Операция объединения словарей.
        """
        if not isinstance(other, Dictionary):
            return NotImplemented
        new_dict = Dictionary(
            f"{self.name} + {other.name}", size=self.MAX_SIZE
        )
        new_dict.cards = list(set(self.cards + other.cards))
        new_dict.count = len(new_dict.cards)
        return new_dict

    def __and__(self, other):
        """
        Операция пересечения словарей.
        """
        if not isinstance(other, Dictionary):
            return NotImplemented
        new_dict = Dictionary(
            f"{self.name} & {other.name}", size=self.MAX_SIZE
        )
        new_dict.cards = list(set(self.cards) & set(other.cards))
        new_dict.count = len(new_dict.cards)
        return new_dict

    def __sub__(self, other):
        """
        Операция вычитания словарей.
        """
        if not isinstance(other, Dictionary):
            return NotImplemented
        new_dict = Dictionary(
            f"{self.name} - {other.name}", size=self.MAX_SIZE
        )
        new_dict.cards = [
            card for card in self.cards if card not in other.cards
        ]
        new_dict.count = len(new_dict.cards)
        return new_dict

    def __str__(self):
        """
        Строковое представление словаря.
        """
        cards_str = "\n".join(
            f"{card.foreign_word}: {card.translation}" for card in self.cards
        )
        return f"'{self.name}' ({self.count}/{self.size}):\n{cards_str}"


# Пример использования:
if __name__ == "__main__":
    dict1 = Dictionary("Еда")
    dict1.add_card("Apple", "Яблоко")
    dict1.add_card("Bread", "Хлеб")
    dict1.add_card("Milk", "Молоко")

    dict2 = Dictionary("Природа")
    dict2.add_card("Apple", "Яблоко")
    dict2.add_card("Tree", "Дерево")
    dict2.add_card("River", "Река")

    print(f"{dict1}\n")  # Вывод словаря 1
    print(f"{dict2}\n")  # Вывод словаря 2

    print("\nОбъединение словарей:")
    print(dict1.__add__(dict2))

    print("\nПересечение словарей:")
    print(dict1.__and__(dict2))

    print("\nРазность словарей:")
    print(dict1.__sub__(dict2))

    dict1.name = "Продовольствие"  # Изменение названия словаря
    print(f"\n{dict1}")
