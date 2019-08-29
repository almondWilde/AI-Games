#!/usr/bin/env python
# coding: utf-8

# ## Assignment 2, 22-Queen Programming

# Your homework must be implemented in this Notebook file. 
# You can add as many cells as you want. However, you are not allowed to touch the code below the line "=============".
# 

# In[1]:


n = 17


# In[ ]:





# In[2]:


import sys
import numpy as np

# override default recursion limit
sys.setrecursionlimit(1000000000)


class Queens:

    def __init__(self, size):
        self.size = size
        self.columns = [] * self.size
        self.num_of_places = 0
        self.num_of_backtracks = 0
        self.solCount = 0

    def place(self, startRow=0):
        
        # solution when columns == size
        if len(self.columns) == self.size:
            return self.columns

        else:
            for row in range(startRow, self.size):
                if self.isSafe(len(self.columns), row) is True:
                    # place a queen
                    self.columns.append(row)
                    self.num_of_places += 1
                    
                    return self.place()
            else:
                lastRow = self.columns.pop()
                self.num_of_backtracks += 1
                
                return self.place(startRow=lastRow + 1)

    def isSafe(self, col, row):
        
        # check for places of each queen currently on board
        for threatRow in self.columns:
            
            threatCol = self.columns.index(threatRow)
            if row == threatRow or col == self.columns.index(threatRow):
                return False
            elif threatRow + threatCol == row + col or threatRow - threatCol == row - col:
                return False
            
        return True

result = [] * 4
for startRow in range(0,4):
    queens = Queens(n)
    queens.place(startRow)
    cords = [] * n

    for queen in queens.columns:
        cords.append([queens.columns.index(queen), queen])
    
    result.append(cords)
    print cords, '\n'


# In[3]:


def print_result(result):
    for b in result:
        for pair in b:
            sys.stdout.write('(' +  str(pair[0]) + ',' + str(pair[1]) + ') ')
        print '\n'


# In[ ]:





# You can insert as many cells as you want above
# You are not Allowed to modify the code below this line.
# ===============================

# In[ ]:


#you need to implement print_result function to print out the result according to the required format
print_result(result)


# 
# The output format should be as follows. You only need to give 4 solutions in the following format.
# Example Output for 4-queens Problem. Each pair of values represents the position of a queen (row, column)
# (0,1) (1,3) (2,0) (3,2)
# (0,2) (1,0) (2,3) (3,1)
# 
# 
# 
