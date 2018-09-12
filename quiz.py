# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 14:21:25 2018

@author: maico
"""

import numpy as np

nosymbols=[",",".",";","!","?"]

levels=["facil","médio","difícil"]

white_spaces=["__1__", "__2__", "__3__", "__4__", "__5__","__6__"]

phrases_basics=    ["A César o que é de César, a Deus o que é de Deus.",
                   "Água mole, pedra dura, tanto bate até que fura.",
                   "A pressa é a inimiga da perfeição",
                   "À noite todos os gatos são pardos.",
                   "Antes só do que mal acompanhado.",
                   "As aparências enganam.",
                   "Apressado come cru e quente.",
                   "A voz do povo é a voz de Deus.",
                   "Cada macaco no seu galho.",
                   "Caiu na rede, é peixe",
                   "Casa de ferreiro, espeto de pau.",
                   "Cão que ladra não morde.",
                   "Cavalo dado não se olha os dentes",
                   "De grão em grão, a galinha enche o papo.",
                   "De médico e de louco todo mundo tem um pouco.",
                   "Devagar se vai ao longe.",
                   "Deus ajuda quem cedo madruga.",
                   "Deus escreve certo por linhas tortas.",
                   "Diz-me com quem andas e eu te direi quem és.",
                   "É dando que se recebe.",
                   "Em terra de cego quem tem olho é rei.",
                   "Escreveu, não leu; o pau comeu.",
                   "Filho de peixe, peixinho é.",
                   "Gato escaldado tem medo de água fria.",
                   "Ladrão que rouba ladrão tem cem anos de perdão.",
                   "Mais vale um pássaro na mão do que dois voando.",
                   "Mentira tem perna curta.",
                   "O barato sai caro.",
                   "O hábito faz o monge.",
                   "Onde há fumaça há fogo.",
                   "O seguro morreu de velho.",
                   "Para bom entendedor, meia palavra basta.",
                   "Para baixo todo santo ajuda.",
                   "Pimenta nos olhos dos outros é refresco.",
                   "Por ele eu ponho minha mão no fogo.",
                   "Quando os porcos bailam adivinham chuva.",
                   "Quando um burro fala, o outro abaixa a orelha.",
                   "Quem ama o feio, bonito lhe parece.",
                   "Quem canta seus males espanta.",
                   "Quem casa quer casa.",
                   "Quem com ferro fere, com ferro será ferido.",
                   "Quem mistura-se com porcos, farelo come.",
                   "Quem não tem cão, caça com gato.",
                   "Quem pode, pode; quem não pode, se sacode.",
                   "Quem ri por último ri melhor.",
                   "Quem semeia vento, colhe tempestade.",
                   "Quem tem boca vai à Roma.",
                   "Saco vazio não para em pé.",
                   "Uma andorinha sozinha não faz verão.",
                   "Um dia é da caça, outro do caçador."]

phrases={}
size_phrases=len(phrases_basics)
index_phrases_not_used=list(range(size_phrases))

class Phrase(str):
        
    def __init__(self,name):
        self.name = name
        self.words=[]
        self.size=0
        self.list_of_words()
        self.size_phrase()
        self.list_without_punt()
    
    def list_of_words(self):
        self.words=self.name.lower().split()
        
    def size_phrase(self):
        self.size=len(self.words)
                
    def list_without_punt(self):
                             
        for index in range(self.size):
            word=self.words[index]            
            size_word=len(word)
            position=-1
            while abs(position)<=size_word:            
                last_symbol=word[position]            
                if last_symbol in nosymbols:
                    new_word=word[:position]
                    self.words.pop(index)
                    self.words.insert(index,new_word)                
                position-=1
             
                
class Player(object):
    def __init__(self,name):
        self.name=name

    
class Round(object):
    
    def __init__(self,number,player,level):
        self.number=number
        self.level=level
        self.player=player

        
def add_phrases(list_phrases):
    size_phrases=len(list_phrases)
    for index in range(size_phrases):
        phrases["{0}".format(index)]=Phrase(list_phrases[index])
    return phrases

phrases=add_phrases(phrases_basics)

phrases["22"].words
        
       
    
                            
    
    
    
        
