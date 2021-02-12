# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 18:36:10 2021

Lógica de programação
Pensando em todos os números naturais inferiores a 10 que são múltiplos de 3 ou 5, temos 3, 5, 6 e 9.
 Somando esses múltiplos obtemos o valor 23. Utilize um algorítimo para calcular a soma de todos os 
 múltiplos de 3 ou 5 abaixo de 1000

@author: Pedro Ayres
"""
soma=0
    
for i in range(1000):
    if(i%3==0 or i%5==0):
        soma=soma+i

print(soma)        
    
    
