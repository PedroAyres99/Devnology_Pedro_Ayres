# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 17:37:22 2021

Função recursiva
Crie uma função recursiva para descobrir o menor número inteiro divisível por 2, 3 e 10 ao mesmo tempo. 
Quando encontrá-lo, imprima-o na tela.

@author: Pedro Ayres
"""

def divisor(number):
    if(number%2==0 and number%3==0 and number%10==0):
        return number
    valor = divisor(number+1)
    return valor


a = divisor(1)
print(a)
