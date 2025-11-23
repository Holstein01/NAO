import os
import sys
import time
import pickle
from itertools import combinations

'''if __name__ == "__main__":
    robotIP = "127.0.0.1"
    port = 37163

if len(sys.argv) <= 1:
    print ("robotIP default: 127.0.0.1")
elif len(sys.argv) <= 2:
    robotIP = sys.argv[1]
else:
    port = int(sys.argv[2])
    robotIP = sys.argv[1]
'''
'''dir = '/home/nao/NAO-main/moves/project_positions'
file_list = []

mandatory = ['16-Sit.py', 'WipeForehead.py', 'Hello.py', '17-SitRelax.py', '11-Stand.py', '15-StandZero.py']

for filename in os.listdir(dir):
    if os.path.isfile(os.path.join(dir, filename)):
        file_list.append(filename)

cond = [[True, True]], 
[]'''

pos = '4-Arms_opening.py'

os.system('python2 moves/project_positions/4-Arms_opening.py 127.0.0.1 37163')
#os.system("python2 moves/project_positions/" + pos + " " + robotIP + " " + str(port))
