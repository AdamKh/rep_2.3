#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    w = str(input('Введите слово: '))
    k = int(input('Введите k: '))
    tmp = list(w)

    s = tmp[-1]
    for i in range(len(w) - 1, k - 1, -1):
        tmp[i] = tmp[i - 1]
    tmp[k - 1] = s

    w = ''.join(tmp)
    print(w)
