#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите задачу: создайте словарь, где ключами являются числа, а значениями – строки.
# Примените к нему метод items(), c с помощью полученного объекта dict_items создайте
# новый словарь, "обратный" исходному, т. е. ключами являются строки, а значениями –
# числа.

if __name__ == '__main__':
    nomer = {1: 'один', 2: 'два', 3: 'три',4: 'четыре'}

    new_nomer = {}
    for key, value in nomer.items():
        new_nomer[value] = key
    print(new_nomer)