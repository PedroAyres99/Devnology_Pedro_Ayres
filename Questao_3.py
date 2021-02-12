# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 18:21:44 2021

Orientação a objeto
Crie uma classe contendo 3 propriedades com seus respectivos gets e sets e um método que multiplique 
as 3 retornando o produto. Deixe um exemplo de utilização da sua classe no final do código.

@author: Pedro Ayres
"""

class Teste_Q3(object):
    
    def init(self, num_1, num_2, num_3):
        self.num_1 = num_1
        self.num_2 = num_2
        self.num_3 = num_3

    def num_1_Get(self):
        return self.num_1
    
    def num_1_Set(self, num_1):
        self.num_1 = num_1
        
    def num_2_Get(self):
        return self.num_2
    
    def num_2_Set(self, num_2):
        self.num_2 = num_2
        
    def num_3_Get(self):
        return self.num_3
    
    def num_3_Set(self, num_3):
        self.num_3 = num_3
        
    def multiplique(self):
        return self.num_1 * self.num_2 * self.num_3 
    
teste = Teste_Q3()

teste.num_1_Set(3)
teste.num_2_Set(5)
teste.num_3_Set(4)
            
print(teste.multiplique())
            