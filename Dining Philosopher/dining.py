'''
Dining Philosopher by Hrishikesh Waikar:
Each phiolosopher is an independent process that infinitely:
1. thinks               state : thinking
2. seeks left fork      state : hungry  { atomic action but wait is there of fork unavailable
3. seeks right fork     state : hungry  { -||-
4. eats                 state : eating
5. releases left fork   state : thinking  - atomic action
6. releases left fork   state : thinking  - atomic action

the forks are commonly shared and are to be provided as a shared memory resource

'''

import time

fork=[1,1,1,1,1]

class Philosopher():

    def __init__(self,id):
        self.id = id
        self.state = None

    def minmax(no1,no2):
        if no1>no2:
            min = no2
            max=no1
        else:
            min = no1
            max = no2
        return min,max

    def think(self):
        self.state = 'Thinking'
        time.sleep(1)

    def getFork(self,forkid):
        while fork[forkid]==0:
            self.state = 'Hungry and waiting for fork '+str(forkid)

        if fork[forkid]==1:
            fork[forkid]=0
            self.state ='Hungry but got fork '+str(forkid)

    def eat(self):
        state = 'Eating'
        self.delay(1)

    def releaseFork(self,forkid):
        fork[forkid]=1
        state='Thinking but releasing fork '+str(forkid)

    def philosopher_lifecycle(self):

        while True:
            self.think()
            min,max = self.minmax(id, (id + 1) % 5)
            self.getFork(min)
            self.getFork(max)
            self.eat()
            self.releaseFork(min)
            self.releaseFork(max)

