import random
from person import Person
from board import Board
from termcolor import colored

class Enemy(Person):
    def __init__(self,arr):
        self.n=random.randrange(6,35,2)
        self.m=random.randrange(12,69,4)
        self.flag=True
        while(1):
            if(arr[self.n][self.m]!=' '):
                self.n=random.randrange(6,35,2)
                self.m=random.randrange(12,69,4)
            else:
                break
        for i in range(0,2):
            for j in range(0,4):
                arr[self.n+i][self.m+j]=colored('E','red')
        Person.__init__(self,arr,self.m,self.n)

    def place(self,arr):
        for i in range(0,2):
            for j in range(0,4):
                arr[self.n+i][self.m+j]=colored('E','red')
        return arr

    def clear_enemy(self,arr):
        for i in range(0,2):
            for j in range(0,4):
                arr[self.n+i][self.m+j]=colored('^','magenta')
        return arr

    def setFlag(self,val):
        self.flag=val

    def getFlag(self):
        return self.flag

    def move(self,arr):
        l=random.randrange(-4,5,2)
        if(l==4 or l==-4):
            dm=l
            dn=0
        elif(l==0):
            dm=0
            dn=0
        else:
            dn=l
            dm=0

        if(self.is_not_obstacle(arr,dm,dn) and self.flag):
            for i in range(0,2):
                for j in range(0,4):
                    arr[self.n+i][self.m+j]=' '
            self.setN(self.n+dn)
            self.setM(self.m+dm)
            arr=self.place(arr)
        return arr
