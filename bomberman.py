from person import Person
from bomb import Bomb
from termcolor import colored

class Bomberman(Person):
    def __init__(self,arr):
        self.m=4
        self.n=2
        Person.__init__(self,arr,self.m,self.n)

    def place(self,arr,m,n):
        arr[n][m]=colored('[','yellow')
        arr[n][m+1]=colored('^','yellow')
        arr[n][m+2]=colored('^','yellow')
        arr[n][m+3]=colored(']','yellow')
        arr[n+1][m]=' '
        arr[n+1][m+1]=colored(']','yellow')
        arr[n+1][m+2]=colored('[','yellow')
        arr[n+1][m+3]=' '
        return arr

    def enemy_present(self,arr,char):
        if(char=='a'):
            dm=-4
            dn=0
        elif(char=='d'):
            dm=4
            dn=0
        elif(char=='s'):
            dm=0
            dn=2
        elif(char=='w'):
            dm=0
            dn=-2
        else:
            dm=0
            dn=0
        if(arr[self.n+dn][self.m+dm]==colored('E','red')):
            return True
        else:
            return False

    def move(self,arr,char):
        if(char=='a'):
            dm=-4
            dn=0
        elif(char=='d'):
            dm=4
            dn=0
        elif(char=='s'):
            dm=0
            dn=2
        elif(char=='w'):
            dm=0
            dn=-2
        else:
            dm=0
            dn=0
        if(self.is_not_obstacle(arr,dm,dn)):
            for i in range(0,2):
                for j in range(0,4):
                    arr[self.n+i][self.m+j]=' '
            self.setN(self.n+dn)
            self.setM(self.m+dm)
            arr=self.place(arr,self.m,self.n)
        return arr
