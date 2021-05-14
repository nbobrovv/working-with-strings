#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = str.strip(input('Введите предложение: '))
    n = (s.split(' '))
    print(n[-2:])