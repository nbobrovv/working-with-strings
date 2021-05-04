#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    a = str(input("Введите фразу: "))
    s = 0
    b = a.split("+")
    for i in range(len(b)):
        g = int(b[i])
        s += g
    print(s)