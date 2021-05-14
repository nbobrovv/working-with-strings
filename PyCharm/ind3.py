#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    a = str(input("Введите фразу: "))
    s = 0
    b = a.split("+")
    b = list(b)
    for i in b:
        g = int(i)
        s += g
    print(s)