#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = str(input('Введите предложение:\n'))
    am_words = 0
    for i in range(0, len(s)):
        if s[i] == ' ':
            am_words += 1
    if s[-1] != ' ':
        am_words += 1
    print(am_words)
