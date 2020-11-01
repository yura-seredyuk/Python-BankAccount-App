"""Написати клас "Банківський рахунок" (Account), який містить:

Номер рахунку
Розмір коштів на рахунку
Назва валюти рахунку (рублі, гривні, евро тощо), для позначення якої можна скористатись одним символом: R, G, E, $ тощо
Забезпечити можливість:

Відкривати рахунок та первинно вносити гроші на рахунок
Знімати гроші з рахунку
Докладати гроші на рахунок
ПРИМІТКА! На 12 балів реалізувати також можливість здійснювати переказ грошей з одного рахунку на другий."""


if __name__ == "__main__":
    Account

import random


class Account:

    def __init__(self, sum: int, currency: str):
        self.__number = random.randint(10000000, 99999999)
        self.__sum = sum
        self.__currency = currency

    def take_money(self, take):
        if take <= 0:
            print("Uncorrect sum!")
        elif take < self.__sum:
            self.__sum -= take
            print("Operation is correct!")
        else:
            print("You do not have enough money!")
        return self.__sum

    def put_money(self, put):
        if put <= 0:
            print("Uncorrect sum!")
        else:
            self.__sum += put
            print("Operation is correct!")
        return self.__sum

    @property
    def number(self):
        return self.__number

    @property
    def sum(self):
        return self.__sum

    @property
    def currency(self):
        return self.__currency
