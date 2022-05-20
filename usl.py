#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    s = input('Введите предложение:\n')
    s1 = s.split()
    i = 0
    for i in range(len(s1)):
        for j in range(len(s1)-1):
            if len(s1[j]) < len(s1[j + 1]):
                s1[j], s1[j + 1] = s1[j + 1], s1[j]
    s = ''
    for i in range(0, len(s1)):
        s += s1[i] + ' '
    print(s)
