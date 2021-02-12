# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 16:19:03 2021

@author: Pedro Ayres

Arrays
Tendo os arrays ['ES', 'MG', 'RJ', 'SP', 'MT'] e ['Mato Grosso', 'São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Espírito Santo'],
percorra os vetores dados e crie um outro com a seguinte estrutura:
['MT' => ''Mato Grosso'', 'ES'=>'Espírito Santo', 'MG'=>'Minas Gerais', 'RJ'=>'Rio de Janeiro', 'SP'=>'São Paulo'].
Depois de criado terceiro vetor, leia-o e imprima em cada linha a chave de cada posição e seu respectivo valor
separados por "-".
"""

import itertools

L_1 = ['ES', 'MG', 'RJ', 'SP', 'MT'] 
L_2 = ['Mato Grosso', 'São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Espírito Santo']

count = (len(L_2) - 1)

dic = {}
for j in range(len(L_2)):
    dic[L_1[count]] = L_2[j]
    count -= 1

# Reordenando a Lista:
dic.pop("MT")
dic[L_1[4]] = L_2[0]

# Gera a lista com os índices:
indices = list(dic.keys())

# Ordena a lista de índices em ordem reversa:
indices = reversed(indices)

# Percorre a lista de índices, acessando a respectiva posição:
for indice in indices:
    print(indice, '-' ,dic[indice])

