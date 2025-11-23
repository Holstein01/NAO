import os
import sys
import time
import subprocess
from planer import planer

time.sleep(20)

alpha = 3
beta = 0
rho = 0.2
Q = 10
n_ants = 50
n_iterations = 100
mand_weight = 50 #additional weight of mandatory positions
penalty_mndt = 1000
penalty_end = 0


path, duration, missed_mndt = planer(alpha, beta, rho, Q, n_ants, n_iterations, mand_weight, penalty_mndt, penalty_end)

if __name__ == "__main__":

    robotIP = "127.0.0.1"
    port = 9559
    if len(sys.argv) > 2:
        port = int(sys.argv[2])
        robotIP = sys.argv[1]
    elif len(sys.argv) == 2:
        robotIP = sys.argv[1]

subprocess.Popen(['aplay', 'music.wav'])

for pos in path:
    os.system("python2 moves/project_positions/" + pos + " " + robotIP + " " + str(port))
print(missed_mndt)




















