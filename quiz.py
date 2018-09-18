# -*- coding: utf-8 -*-
"""
Quiz 

Baseado em uma lista de frases o jogador tem que acertar os espaços em branco
de uma frase gerada aleatoriamente.
A dificuldade do jogo consiste no número de espaçoes em branco e na 
possibilidade de errar ou não uma palavra.
De acordo com o nível de dificuldade e a frase gerada aleatoriamente o programa
define o número de substituições e as posições das substituições na frase.
Se o jogador acerta a frase ele tem uma pontuação de acordo com a escolha
 da dificuldade. Em cada rodada ele é questionado qual o nível quer jogar.
O jogo pode ser finalizado pelo jogador por um comando de teclado ou
quando erra uma palavra e esgota o número de tentativas.

Based on a list of phrases the player has hit the blanks of a randomly generated phrase.
The difficulty of the game consists of the number of blank spaces and the
number of chances to hit a word.
According to the level and the phrase randomly generated the program
calculates the number of substitutions and the positions of substitutions in the sentence.
If the player hits the whole sentence he has a score according to the choice
of difficulty.
In each round he is asked which level he wants to play.
The game can be finished by the player by a keyboard command or 
when the player misses a word and exhausts the number of attempts.



"""

#imports necessary packges
import numpy as np

#variables of the game
nosymbols=[",",".",";","!","?"]
levels=["fácil","médio","difícil"]
chances_by_level=[3,2,1]
number_spaces=[2,3,4,5,6]
size_of_phrase=[3,4,5,6,7]
levels_score=[1,3,5]
white_spaces=["__1__", "__2__", "__3__", "__4__", "__5__","__6__"]


#file that store the phrases of the game
file = open("phrases.txt","r") 
phrases_basics = []
for line in file:
    phrase=line[:-2]
    phrases_basics.append(phrase)
file.close()
phrases={}
size_phrases=len(phrases_basics)
index_phrases_not_used=list(range(size_phrases))


class Phrase(str):
    
    """Constructed as string subclass. This class store the phrases of the game.
    And makes all necessary adjusts. """    
    
    def __init__(self,name):
        
        """ When some instance of the class is created 
        automatically store the words without ponctuation 
        in list and the sizes of the phrase."""
        
        self.name = name
        self.words=[]
        self.size=0
        self.list_of_words()
        self.size_phrase()
        self.list_without_punt()
    
    def list_of_words(self):
        
        """Store the words in phrase in list."""
        
        self.words=self.name.lower().split()        
              
    def list_without_punt(self):
        
        """Turns all words in phrase without pontuaction"""
                             
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
    
    def size_phrase(self):
        
        """Store the size of the phrase"""
        
        self.size=len(self.words)
             
                
class Player(object):
    
    """Store the players of the game"""
    
    def __init__(self):
        
        """When some player is created automatically call an input asking it's name"""
        
        self.name=""
        self.name=input(" Por favor, digite o seu nome:")
        self.score=0
        
    def print_score_middle(self):
        
        """Prints the name of the player and the score inside the game"""
        
        print("Você marcou {} pontos até o momento {} !"\
              .format(self.score,self.name))
        
    def print_final_score(self):
        
        """Prints the name of the player and the score after the game finished"""
        
        print("Parabéns {}! Sua pontuação final foi {}.".\
              format(self.name,self.score))
        
class Game(object):
    
    """Class that store games"""
    
    def __init__(self):
        self.new_round=True
        self.round=1
        
        
    def initial_instructions(self):
        
        """Prints the initial instructions of the game. Including score by levels"""
        
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
        
        
    def final_instructions(self):
        
        """Prints a message to end the game"""
        
        print("")
        print("Fim de jogo.")
        
    def play_again(self):
        
        """Actualize the variable new_round acording user's response"""
        
        self.new_round=not(bool(input("Digite enter para jogar novamente ou outra coisa para sair.")))
                
    
    def play_game(self):
        
        """Develops all the game"""
        
                
        player={}
        rounds={}        
        number=str(self.round)
        self.initial_instructions()
        player["{0}".format(number)]=Player()     
        
        while self.new_round:
            
            number_r=number+str(self.round)
            rounds["{0}".format(number_r)]=Round(number_r,player[number])
            rounds[number_r].play_round()            
            self.round+=1
            
            if not rounds[number_r].match:
                self.new_round=False
            if rounds[number_r].match:
                player[number].print_score_middle()
                self.play_again()
        
        self.final_instructions()        
        player[number].print_final_score()                 
            
          
class Round(object):
    
    """The most important class on the game. Develops the round of the game
and makes all necessary calculations to play a round """
    
    def __init__(self,number,player,level=""):
        self.number=number
        self.level=level
        self.player=player
        self.phrase=""
        self.index_phrase=0
        self.spaces=0
        self.list_substitution=[]
        self.list_space=[]
        self.select_index_phrase()
        self.score=0
        self.max_choices=0
        self.word=""
        self.match=False
        
    def verify_match(self):
        
        """Verifies if the list_space is the same that word's phrase list.
        If they are then actualizes the variable "match" to true"""
        
        if self.phrase.words==self.list_space:
            self.match=True
        
        
    def select_level(self):
        
        """According user's response select the level.
        The response should start with the initial letter of the level."""
        
        print("")
        self.level=input("Escolha um nível: {}, {}, {}: "\
                .format(levels[0],levels[1],levels[2])).lower()
        
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
        
    def select_index_phrase(self):
        
        """Selects an random index not used. This index will select the phrase of the round."""
        
        index_round=np.random.randint(size_phrases)    
        while index_round not in index_phrases_not_used:
            index_round=np.random.randint(size_phrases)          
        index_phrases_not_used.remove(index_round)             
        self.index_phrase=index_round
        self.phrase=phrases[str(index_round)]            
    
    def amount_of_spaces(self):
        
        """According the level and the size of the phrase, sets the amount of spaces of the round"""
        
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
        
        """According the amount of spaces of the round, create a list of
        random positions that will be replaced by white spaces."""
        
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
        
        """Replaced the words in phrase of the round by white spaces in
        "list_substitution" and store in list spaces"""
        
        count=0
        for i in range(self.phrase.size):
            if i in self.list_substitution:
                self.list_space.append(white_spaces[count])
                count+=1
            else:
                self.list_space.append(self.phrase.words[i])              
    
    def verify_word(self,word,position):
        
        """Verifies if some word is in the position required of the phrase"""
        
        if self.phrase.words[position]==str(word).lower():
            return True
        return False
    
    
    def change_list_space(self,word,position):
        
        """Verifies if the word is correct and replaces the word in list_space"""
        
        if self.verify_word(word,position):
            self.list_space[position]=str(word).lower()
    
    def print_phrase_spaces(self):
        
        """Prints the phrase with spaces"""
        
        print(" ".join(self.list_space)) 
        
    def enter_word(self,word_space):
        
        """Asks the user to enter the word required and stores in word of the round"""
        
        self.word=str(input("Por favor, entre com a palavra {}: "\
                        .format(word_space))).lower()    
      
    
    
    def play_round(self):
        
        """Develops all necessary in a round of the game"""
        
        max_attempt=False 
        self.select_level()
        self.max_choices=chances_by_level[levels.index(self.level)]        
        self.amount_of_spaces()        
        self.substitution_list()        
        self.space_list()          
        
        for i in (self.list_substitution):  
            if not max_attempt:
                for j in range(self.max_choices):
                    if self.list_space[i]!=self.phrase.words[i]:
                        print("")
                        print("Sua frase é: ")
                        self.print_phrase_spaces()
                        self.enter_word(self.list_space[i])                         
                        self.change_list_space(self.word,i)    
                        if (j==self.max_choices-1) and (self.word!=self.phrase.words[i]):
                            max_attempt = True
                            
        self.add_score()
        self.verify_match()
        self.show_phrase_round()       
    
        
    def add_score(self):
        
        """Actualizes the score of the game"""
        
        if self.list_space==self.phrase.words:
            if self.level== levels[0]:
                self.score+=levels_score[0]
            if self.level== levels[1]:
                self.score+=levels_score[1]
            if self.level== levels[2]:
                self.score+=levels_score[2]
                
        self.player.score+=self.score
        
    def show_phrase_round(self):
        
        """Prints the phrase in the end of the round"""
        
        print("")
        if self.match:            
            print("Parabéns, você acertou. A frase era:")
            print(self.phrase)
            print("")
        else:
            print("Que pena, você errou. A frase era:")
            print(self.phrase)
            print("")   
 
        
def add_phrases(list_phrases):
    
    """Creates the phrases of the game"""
    
    size_phrases=len(list_phrases)
    for index in range(size_phrases):
        phrases["{0}".format(index)]=Phrase(list_phrases[index])
    return phrases

phrases=add_phrases(phrases_basics)

game1=Game()
game1.play_game()






        

