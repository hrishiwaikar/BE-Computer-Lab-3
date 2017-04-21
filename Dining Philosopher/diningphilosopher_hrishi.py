'''
Multithreaded Dining Philosopher
Dining Philosopher by Hrishikesh Waikar - Multithreading :
Each philosopher is an independent thread that infinitely:
1. thinks               state : thinking
2. seeks left fork      state : hungry  { atomic action but waits if fork unavailable
3. seeks right fork     state : hungry  { -||-
4. eats                 state : eating
5. releases left fork   state : thinking  - atomic action
6. releases left fork   state : thinking  - atomic action

the forks are commonly shared and are to be provided as a shared memory resource

'''

import time
import threading
import random

fork=[1,1,1,1,1]

class Philosopher(threading.Thread):

    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id = id
        self.state = None

    def run(self):
        self.philosopher_lifecycle_better()

    def minmax(self,no1,no2):
        if no1>no2:
            min = no2
            max=no1
        else:
            min = no1
            max = no2
        return min,max

    def think(self):
        self.state = 'Thinking'
        thinktime=random.randint(1,10)/float(10)
        time.sleep(thinktime)

    def getForks(self,minid,maxid):
        while True:
            if fork[minid]==0 or fork[maxid]==0:
                self.state = 'Hungry and waiting for forks '+str(minid)+' and '+str(maxid)

            elif fork[minid]==1 and fork[maxid]==1:
                fork[minid]=0
                fork[maxid]=0
                self.state ='Got forks '+str(minid)+' and '+str(maxid)
                break

    def eat(self):
        self.state = 'Eating'
        eattime = random.randint(1,20)/float(10)
        #print eattime
        time.sleep(eattime)

    def releaseFork(self,forkid):
        fork[forkid]=1
        self.state='Thinking but releasing fork '+str(forkid)

    def philosopher_lifecycle_better(self):

        while True:
            self.think()
            min = self.id
            max= (self.id+1)%5
            min,max = self.minmax(min,max)
            self.getForks(min,max)

            self.eat()
            self.releaseFork(min)
            self.releaseFork(max)

    def philosopher_lifecycle_worse(self):

        while True:
            self.think()
            self.getFork(self.id)
            self.getFork((self.id+1)%5)
            self.eat()
            self.releaseFork(self.id)
            self.releaseFork((self.id+1)%5)


if __name__ == '__main__':
    philosophers=[]
    for i in range(5):
        p=Philosopher(i)
        philosophers.append(p)
        p.start()

    time.sleep(1.33)
    while True:
        print '\nStatus:'
        time.sleep(1)
        for i in range(5):
            print 'Philosopher '+str(i)+' : '+ str(philosophers[i].state)