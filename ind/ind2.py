#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    w = str(input('Введите слово: '))
    tmp = list(w)

    s = tmp[2]
    tmp[2] = tmp[-1]
    tmp[-1] = s

    w = ''.join(tmp)
    print(w)
