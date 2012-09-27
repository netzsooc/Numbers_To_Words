#!/usr/bin/python
#-*- coding: utf-8 -*-

'''This program transforms integers to words in Spanish'''

ONES = {0: '', 1: 'UN ', 2: 'DOS ', 3: 'TRES ', 4: 'CUATRO ', 5: 'CINCO ',
        6: 'SEIS ', 7: 'SIETE ', 8: 'OCHO ', 9: 'NUEVE ', 10: 'DIEZ ',
        11: 'ONCE ', 12: 'DOCE ', 13: 'TRECE ', 14: 'CATORCE ', 15: 'QUINCE ',
        16: 'DIECISEIS ', 17: 'DIECISIETE ', 18: 'DIECIOCHO ',
        19: 'DIECINUEVE ', 20: 'VEINTE '}

TENS = {0: '', 2: 'VEINTI', 3: 'TREINTA ', 4: 'CUARENTA ', 5: 'CINCUENTA ',
        6: 'SESENTA ', 7: 'SETENTA ', 8: 'OCHENTA ', 9: 'NOVENTA '}

HUNDREDS = {1: 'CIENTO ', 2: 'DOSCIENTOS ', 3: 'TRESCIENTOS ',
            4: 'CUATROCIENTOS ', 5: 'QUINIENTOS ', 6: 'SEISCIENTOS ',
            7: 'SETECIENTOS ', 8: 'OCHOCIENTOS ', 9: 'NOVECIENTOS ', 0: ''}


def num_to_let(number):
    '''Function that transforms numbers up to (10 ** 12) - 1 or 999999999999'''
    n0 = number / 10 ** 6
    n1 = number % 10 ** 6
    ht0 = n0 / 1000
    h0 = n0 % 1000
    ht1 = n1 / 1000
    h1 = n1 % 1000
    out = ''

    if n0:
        if ht0:
            if ht0 == 1:
                out += 'MIL ' + first_pass(h0)
            else:
                out += first_pass(ht0) + 'MIL ' + first_pass(h0)
        out += first_pass(h0)
        if out != 'UN ':
            out += 'MILLONES '
        else:
            out += 'MILLÓN '

    if ht1:
        if ht1 == 1:
            out += 'MIL ' + first_pass(h1)
            return out
        out += first_pass(ht1) + 'MIL '
    out += first_pass(h1)
    return out


def first_pass(number):
    '''function that transforms numbers from 1-999 to words in Spanish'''
    if number == 100:
        return 'CIEN '
    if number <= 20:
        return ONES[number]
    h = number / 100
    t = (number % 100) / 10
    o = (number % 10)
    if t < 2 or (t == 2 and o == 0):
        return HUNDREDS[h] + ONES[number % 100]
    if o and t > 2:
        return HUNDREDS[h] + TENS[t] + 'Y ' + ONES[o]
    return HUNDREDS[h] + TENS[t] + ONES[o]
