from walls import Walls
from bomberman import Bomberman
from board import Board
from bomb import Bomb
from enemy import Enemy
from bricks import Bricks
from termcolor import colored
from time import sleep
import random
import click
import sys

global arr,e1,e2,e3,e4,bm,f1,f2,score,brick
score=0
lives=3

def new():
    global arr,e1,e2,e3,e4,bm,f1,f2,brick
    #create walls
    w=Walls()
    arr=w.structure()
    #flags use for bomb
    f1=False
    f2=False
    #random number of bricks
    num=random.randint(15,25)
    for i in range(0,num):
        brick=Bricks(arr)
        arr=brick.place_brick()
    #four enemies
    e1=Enemy(arr)
    e2=Enemy(arr)
    e3=Enemy(arr)
    e4=Enemy(arr)
    #create bomberman instance
    bm=Bomberman(arr)
    arr=bm.place(arr,4,2)
    #create board instance
    b=Board(arr,lives,score)
    b.print_board()
#start the game
new()

while(1):
    char=click.getchar()
    if(e1.getFlag()):
        arr=e1.move(arr)
    if(e2.getFlag()):
        arr=e2.move(arr)
    if(e3.getFlag()):
        arr=e3.move(arr)
    if(e4.getFlag()):
        arr=e4.move(arr)
    a=bm.enemy_present(arr,char)
    #check if enemy and bomberman meet

    if(char=='b' and not f2 and not f1):
        n=bm.getN()
        m=bm.getM()
        bb=Bomb(m,n)
        f1=True
        cnt=3
    elif(char=='q'):
        print(colored('YOU HAVE QUIT THE GAME',color='red',attrs=['bold']))
        sys.exit(0)
    else:
        arr=bm.move(arr,char)
        a=bm.enemy_present(arr,char)
        if((e1.getN()==bm.getN() and e1.getM()==bm.getM() and e1.getFlag()) or
        (e2.getN()==bm.getN() and e2.getM()==bm.getM() and e2.getFlag()) or
        (e3.getN()==bm.getN() and e3.getM()==bm.getM() and e3.getFlag()) or
        (e4.getN()==bm.getN() and e4.getM()==bm.getM() and e4.getFlag()) or a):
            for i in range (0,2):
                for j in range(0,4):
                    arr[bm.getN()+i][bm.getM()+j]=colored('E','red')
            b=Board(arr,lives,score)
            b.print_board()
            sleep(0.2)
            lives=lives-1
            if(lives==0):
                b=Board(arr,lives,score)
                b.print_board()
                print(colored('GAME OVER',color='red',attrs=['bold']))
                sys.exit(0)
            else:
                new()
        b=Board(arr,lives,score)
        b.print_board()

    if(f1):
        arr=bb.place(arr,cnt-1)
        if(cnt==0):
            if(brick.bricks_in_explosion(arr,n,m)):
                no=brick.num_of_bricks(arr,n,m)
                score=score+(no*20)

            arr=bb.explode(arr)
            f1=False
            f2=True

            if(e1.in_explosion(arr) and e1.getFlag()):
                arr=e1.clear_enemy(arr)
                e1.setFlag(False)
                score=score+100
            if(e2.in_explosion(arr) and e2.getFlag()):
                arr=e2.clear_enemy(arr)
                e2.setFlag(False)
                score=score+100
            if(e3.in_explosion(arr) and e3.getFlag()):
                arr=e3.clear_enemy(arr)
                e3.setFlag(False)
                score=score+100
            if(e4.in_explosion(arr) and e4.getFlag()):
                arr=e4.clear_enemy(arr)
                e4.setFlag(False)
                score=score+100
            b=Board(arr,lives,score)
            b.print_board()
            sleep(0.2)

            if(bm.in_explosion(arr)):
                b=Board(arr,lives,score)
                b.print_board()
                sleep(0.2)
                lives=lives-1
                if(lives==0):
                    b=Board(arr,lives,score)
                    b.print_board()
                    print(colored('GAME OVER',color='red',attrs=['bold']))
                    sys.exit(0)
                else:
                    new()

            if(not e1.getFlag() and not e2.getFlag() and not e3.getFlag()
            and not e4.getFlag()):
                b=Board(arr,lives,score)
                b.print_board()
                print(colored('YOU WON','red',attrs=['bold']))
                sys.exit(0)
        b=Board(arr,lives,score)
        b.print_board()
        cnt=cnt-1

    if(f2):
        arr=bb.post_explode(arr)
        f2=False
