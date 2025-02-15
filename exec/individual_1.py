#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Поле first — целое положительное число, часы; поле second — целое
положительное число, минуты. Реализовать метод
minutes() — приведение времени в минуты.

Выполнил студент группы ИВТ-б-о-22-1 Иващенко О.А.
'''


class Time:
    def __init__(self, hours=0, minutes=0):
        """
        Метод инициализации значений.
        """
        if not self.is_valid(hours) or not self.is_valid(minutes):
            raise ValueError(
                "Часы и минуты должны быть неотрицательными целыми числами"
            )
        self.hours = hours
        self.minutes = minutes

    @staticmethod
    def is_valid(value):
        """
        Проверяет аргумент на правильность введённых данных.
        """
        return isinstance(value, int) and value >= 0

    def total_minutes(self):
        """
        Метод приведения времени в минуты.
        """
        return self.hours * 60 + self.minutes

    def __add__(self, other):
        """
        Перегрузка оператора сложения.
        """
        if isinstance(other, Time):
            total_minutes = self.total_minutes() + other.total_minutes()
        elif isinstance(other, int):
            total_minutes = self.total_minutes() + other
        else:
            return NotImplemented
        return Time(total_minutes // 60, total_minutes % 60)

    def __sub__(self, other):
        """
        Перегрузка оператора вычитания.
        """
        if isinstance(other, Time):
            total_minutes = self.total_minutes() - other.total_minutes()
        elif isinstance(other, int):
            total_minutes = self.total_minutes() - other
        else:
            return NotImplemented
        return Time(total_minutes // 60, total_minutes % 60)

    def __int__(self):
        """
        Приведение объекта к целому числу (общее количество минут).
        """
        return self.total_minutes()

    def __str__(self):
        """
        Строковое представление объекта.
        """
        return f"{self.hours} ч. {self.minutes} мин."

    def __eq__(self, other):
        """
        Перегрузка оператора равенства.
        """
        if isinstance(other, Time):
            return self.total_minutes() == other.total_minutes()
        return False

    def __lt__(self, other):
        """
        Перегрузка оператора меньше.
        """
        if isinstance(other, Time):
            return self.total_minutes() < other.total_minutes()
        return NotImplemented

    def __le__(self, other):
        """
        Перегрузка оператора меньше или равно.
        """
        return self == other or self < other


if __name__ == "__main__":
    try:
        hours = int(input("[1] Введите количество часов: "))
        minutes = int(input("[1] Введите количество минут: "))
        time1 = Time(hours, minutes)

        hours = int(input("[2] Введите количество часов: "))
        minutes = int(input("[2] Введите количество минут: "))
        time2 = Time(hours, minutes)

        print(f"\nВремя 1: {time1.__str__()}, всего минут: {int(time1)}")
        print(f"Время 2: {time2.__str__()}, всего минут: {int(time2)}\n")

        print(f"[=] Эквивалентно ли время: {time1.__eq__(time2)}")
        print(f"[+] Сумма времён: {time1.__add__(time2).__str__()}")
        if time1.total_minutes() > time2.total_minutes():
            print(f"[-] Разность времён: {time1.__sub__(time2).__str__()}")
        else:
            print(f"[-] Разность времён: {time2.__sub__(time1).__str__()}")
        print(f"[<] Время 1 < Время 2: {time1.__lt__(time2).__str__()}")
        print(f"[<=] Время 1 <= Время 2: {time1.__le__(time2).__str__()}")

    except ValueError as e:
        print(f"Ошибка: {e}")
