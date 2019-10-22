from termcolor import colored
import random

class Person:
    def __init__(self,arr,m,n):
        self.m=m
        self.n=n

    #overrinding
    def place(self,arr):
        raise NotImplementedError
        return arr

    def is_not_obstacle(self,arr,dm,dn):
        flag=True
        if(arr[self.n+dn][self.m+dm]==colored('#','blue') or
        arr[self.n+dn][self.m+dm]==colored('%','cyan') or
        arr[self.n+dn][self.m+dm]==colored('[','green')):
            flag=False
        return flag

    def getN(self):
        return self.n

    def getM(self):
        return self.m

    def setN(self,n):
        self.n=n

    def setM(self,m):
        self.m=m

    def in_explosion(self,arr):
        if(arr[self.n][self.m]==colored('^','magenta')):
            return True
        else:
            return False
