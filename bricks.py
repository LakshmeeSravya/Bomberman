import random
from termcolor import colored

class Bricks():
    def __init__(self,arr):
        self.__arr=arr

    def place_brick(self):
        n=random.randrange(4,35,2)
        m=random.randrange(8,69,4)
        while(1):
            if(self.__arr[n][m]!=' '):
                n=random.randrange(4,35,2)
                m=random.randrange(8,69,4)
            else:
                break
        for i in range(0,2):
            for j in range(0,4):
                self.__arr[n+i][m+j]=colored('%','cyan')
        return self.__arr

    def bricks_in_explosion(self,arr,n,m):
        if(arr[n+2][m]==colored('%','cyan') or arr[n-2][m]==colored('%','cyan') or arr[n][m+4]==colored('%','cyan') or arr[n][m-4]==colored('%','cyan')):
            return True
        else:
            return False

    def num_of_bricks(self,arr,n,m):
        no=0
        if(arr[n+2][m]==colored('%','cyan')):
            no=no+1
        if(arr[n-2][m]==colored('%','cyan')):
            no=no+1
        if(arr[n][m+4]==colored('%','cyan')):
            no=no+1
        if(arr[n][m-4]==colored('%','cyan')):
            no=no+1
        return no
