# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 14:21:25 2018

@author: maico
"""

import numpy as np

nosymbols=[",",".",";","!","?"]
levels=["fácil","médio","difícil"]
chances_by_level=[3,2,1]
number_spaces=[2,3,4,5,6]
size_of_phrase=[3,4,5,6,7]
levels_score=[1,3,5]
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
    
    def __init__(self):
        self.name=""
        self.name=input(" Por favor, digite o seu nome:")
        self.score=0
        
    def print_score_middle(self):
        print("Você marcou {} pontos até o momento {} !"\
              .format(self.score,self.name))
        
    def print_final_score(self):
        print("Parabéns {}! Sua pontuação final foi {}.".\
              format(self.name,self.score))
        
class Game(object):
    
    def __init__(self):
        self.new_round=True
        self.round=1
        
        
    def initial_istructions(self):
        
        print("")
        print("O objetivo do jogo é completar as palavras de uma frase...")
        print("Não se esqueça dos acentos!")
        print("Se você escolher difícil você só terá uma chance por palavra,")
        print("médio duas chances e fácil três chances.")   
        print("A escolha dos níveis também pode deixar mais espaços em branco!")
        print("Fácil são dois, médio é de dois a três e difícil é de três à seis espaços!")
        print("")
        print("Cada frase acertada no nível {} acumula {} pontos!"\
          .format(levels[2],levels_score[2]))
        print("Cada frase acertada no nível {} acumula {} pontos!"\
          .format(levels[1],levels_score[1]))
        print("Cada frase acertada no nível {} acumula {} ponto!"\
          .format(levels[0],levels_score[0]))
        print("Pense nas suas escolhas e boa sorte!!")
        print("")
        
       
    
    def begin_game(self):
        self.initial_istructions()
        player1= Player()
        
        
    def final_instructions(self):
        print("")
        print("Fim de jogo.")
        
    
class Round(object):
    
    def __init__(self,number,player,level=""):
        self.number=number
        self.level=level
        self.player=player
        self.phrase=""
        self.list_index=[]
        self.index_phrase=0
        self.spaces=0
        self.list_substitution=[]
        self.list_space=[]
        self.select_index_phrase()
        self.score=0
        self.choices=0
        self.max_choices=0
        self.match=False
        
    def verify_match(self):
        if self.phrase.words==self.list_space:
            self.match=True
        
        
    def select_level(self):
        
        print("")
        self.level=input("Escolha um nível: {}, {}, {}: "\
                .format(levels[0],levels[1],levels[2]).lower()).lower()
        
        if self.level.startswith(levels[0][0]):
            self.level=levels[0]
        
        if self.level.startswith(levels[1][0]):
            self.level=levels[1]
            
        if self.level.startswith(levels[2][0]):
            self.level=levels[2]
        
        while self.level not in levels :
            print("Digite um nível válido...")
            self.level=input("Escolha um nível: {}, {}, {}: ".\
                    format(levels[0],levels[1],levels[2])).lower()
            
        self.max_choices=chances_by_level[levels.index(self.level)]
        
        self.amount_of_spaces()
        
        self.substitution_list()
        
        self.space_list()
        
        
        

        
    def select_index_phrase(self):
        
        index_round=np.random.randint(size_phrases)    
        while index_round not in index_phrases_not_used:
            index_round=np.random.randint(size_phrases)          
        index_phrases_not_used.remove(index_round)             
        self.index_phrase=index_round
        self.phrase=phrases[str(index_round)]            
    
    def amount_of_spaces(self):
        
        if self.level==levels[0]:
            self.spaces=number_spaces[0]
        if self.level==levels[1]:
            if self.phrase.size>=size_of_phrase[1]:
                self.spaces=number_spaces[1]
            else:
                self.spaces=number_spaces[0]      
        if self.level == levels[2]:            
            if self.phrase.size<=size_of_phrase[2]:
                self.spaces= number_spaces[1]                
            if self.phrase.size >size_of_phrase[2]:
                self.spaces=number_spaces[2]                
            if self.phrase.size>size_of_phrase[3]:
                self.spaces= number_spaces[3]           
            if self.phrase.size> size_of_phrase[4]:
                self.spaces=number_spaces[4] 
    

    def substitution_list(self):
        
 
        self.list_substitution.append(np.random.randint(self.phrase.size))       
        count = 1
        position=np.random.randint(self.phrase.size)
        while count < self.spaces:
            while position in self.list_substitution:
                position=np.random.randint(self.phrase.size)
            self.list_substitution.append(position)
            count+=1
        self.list_substitution.sort()
  
        
    def space_list(self):       
        
        count=0
        for i in range(self.phrase.size):
            if i in self.list_substitution:
                self.list_space.append(white_spaces[count])
                count+=1
            else:
                self.list_space.append(self.phrase.words[i])              
    
    def verify_word(self,word,position):
        self.choices+=1
        if self.phrase.words[position]==word.lower():
            return True
        return False
    
    
    def change_list_space(self,word,position):
        if self.verify_word(word,position):
            self.list_space[position]=word.lower()
    
    def print_phrase_spaces(self):
        print(" ".join(self.list_space)) 
    
        
    def add_score(self):
        
        if self.list_space==self.phrase.words:
            if self.level== levels[0]:
                self.score+=levels_score[0]
            if self.level== levels[1]:
                self.score+=levels_score[1]
            if self.level== levels[2]:
                self.score+=levels_score[2]
                
        self.player.score+=self.score
        
    
   
        
def add_phrases(list_phrases):
    size_phrases=len(list_phrases)
    for index in range(size_phrases):
        phrases["{0}".format(index)]=Phrase(list_phrases[index])
    return phrases



phrases=add_phrases(phrases_basics)

phrases["22"].words
        
x=Player()

x.print_final_score()

D=Round(1,x)
                
D.select_level()    
    
D.max_choices

D.phrase
D.spaces
D.list_substitution
D.list_space
D.print_phrase_spaces()

D.change_list_space("mão",5)

D.change_list_space("que",7)

D.verify_match()

D.match

D.list_space

D.add_score()

x.score

D.score
        

