import os
from termcolor import colored

class Board:
    def __init__(self,arr,lives,score):
        os.system('clear')
        self.__arr=arr
        self.__lives=lives
        self.__score=score

    def print_board(self):
        for i in range(0,38):
            for j in range(0,76):
                print(self.__arr[i][j],end="")
            print()
        if(self.__lives>0):
            print(colored('Lives left = %d'%(self.__lives),'red',attrs=['bold']))
        print(colored('Score = %d'%(self.__score),'red',attrs=['bold']))
