import os
import sys
import time
from smth import get_positions

positions = get_positions()

edges = []

mandatory = ['16-Sit.py', 'WipeForehead.py', 
'Hello.py', '17-SitRelax.py', 
'11-Stand.py', '15-StandZero.py']

def compatible(pos_1, pos_2):
    if (positions[pos_2][0] and positions[pos_1][1] == False) or (positions[pos_2][0]==False and positions[pos_1][1]):
        return False
    return True

pos_list = [p for p in positions]

n = len(pos_list)

def t_matrix():
    for i in range(n):
        row = []
        for j in range(n):
            if compatible(pos_list[i], pos_list[j]) == False:
                row.append(1000)
            elif pos_list[i] in mandatory and pos_list[j] in mandatory:
                row.append(positions[pos_list[j]][2])
            else:
                row.append(positions[pos_list[j]][2])
        edges.append(row)
    return edges
