# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
if __name__ == '__main__':
    word = input('Введите слово: ')
    a = word.find('а')
    o = word.rfind('о')
    if a != -1 and o != -1:
        tmp = list(word)
        tmp[a], tmp[o] = tmp[o], tmp[a]
        word = ''.join(tmp)
        print(word)
    else:
        print('В слове не встречаются буквы а и о', file=sys.stderr)
        exit(1)