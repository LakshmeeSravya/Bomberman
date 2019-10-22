from board import Board
from time import sleep
from threading import Timer
from termcolor import colored

class Bomb():
    def __init__(self,m,n):
        self.__m=m
        self.__n=n

    def place(self,arr,cnt):
        if(arr[self.__n][self.__m]!=colored('[','yellow')):
            for i in range(0,2):
                arr[self.__n+i][self.__m]=colored('[','green')
                arr[self.__n+i][self.__m+1]=colored(cnt,'green')
                arr[self.__n+i][self.__m+2]=colored(cnt,'green')
                arr[self.__n+i][self.__m+3]=colored(']','green')
        return arr

    def explode(self,arr):
        if(arr[self.__n][self.__m-4]!=colored('#','blue')):
            for i in range(0,2):
                for j in range(0,4):
                    arr[self.__n+i][self.__m+j-4]=colored('^','magenta')
        if(arr[self.__n][self.__m+4]!=colored('#','blue')):
            for i in range(0,2):
                for j in range(0,4):
                    arr[self.__n+i][self.__m+j+4]=colored('^','magenta')
        if(arr[self.__n+2][self.__m]!=colored('#','blue')):
            for i in range(0,2):
                for j in range(0,4):
                    arr[self.__n+i+2][self.__m+j]=colored('^','magenta')
        if(arr[self.__n-2][self.__m]!=colored('#','blue')):
            for i in range(0,2):
                for j in range(0,4):
                    arr[self.__n+i-2][self.__m+j]=colored('^','magenta')
        for i in range(0,2):
            for j in range(0,4):
                arr[self.__n+i][self.__m+j]=colored('^','magenta')
        return arr

    def post_explode(self,arr):
        if(arr[self.__n][self.__m-4]==colored('^','magenta')):
            for i in range(0,2):
                for j in range(0,4):
                    arr[self.__n+i][self.__m+j-4]=' '
        if(arr[self.__n][self.__m+4]==colored('^','magenta')):
            for i in range(0,2):
                for j in range(0,4):
                    arr[self.__n+i][self.__m+j+4]=' '
        if(arr[self.__n+2][self.__m]==colored('^','magenta')):
            for i in range(0,2):
                for j in range(0,4):
                    arr[self.__n+i+2][self.__m+j]=' '
        if(arr[self.__n-2][self.__m]==colored('^','magenta')):
            for i in range(0,2):
                for j in range(0,4):
                    arr[self.__n+i-2][self.__m+j]=' '
        for i in range(0,2):
            for j in range(0,4):
                arr[self.__n+i][self.__m+j]=' '
        return arr
