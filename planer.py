import os
import sys
import time
import random
from smth import get_positions
from edges import t_matrix, mandatory, pos_list

def planer(alpha, beta, rho, Q, n_ants, n_iterations, mand_weight, penalty_mndt, penalty_end):

    time_matrix = t_matrix()
    positions = get_positions()

    start = '14-StandInit.py'
    finish = '6-Crouch.py'

    # constants
    n = len(time_matrix) # number of possible positions
    L_target = 120 - positions[start][2] - positions[finish][2]
    eps = 1 # delta in path duration
    span_time = positions['17-SitRelax.py'][2]

    #index of positions
    def pos_idx(pos):
        idx = None
        for i, p in enumerate(pos_list):
            if p == pos:
                idx = i
        return idx

    # normalization of values in a list
    def list_norm(lst):
        s = 0
        for item in lst:
            s += item
        for i, item in enumerate(lst):
            lst[i] = item/s
        return lst

    # pheromones evaporation
    def tau_ev(tau, rho):
        for i in range(n):
            for j in range(n):
                tau[i][j] *= (1-rho)
        return tau 

    # number of missed mandatory states
    def missed_mndt(path):
        s = 0
        for m in mandatory:
            if m not in path:
                s += 1
        return s


    #sets of similar positions
    st_pos = ['11-Stand.py', '15-StandZero.py', '14-StandInit.py']

    # initial weights
    tau = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(1)
        tau.append(row)

    best_path = None
    best_score = -1

    for _ in range(n_iterations):
        all_paths = []
        for _ in range(n_ants):
            path = [start]
            duration = 0
            while True:
                if (positions[path[-1]][1] and duration - L_target > eps) or (positions[path[-1]][1] == False and duration - L_target - span_time > eps):
                    break
                probs = []
                i = pos_idx(path[-1])
                for pos in pos_list:
                    j = pos_idx(pos)
                    if pos in mandatory and pos not in path:
                        w = mand_weight
                    else:
                        w = 1
                    if (path[-1] in st_pos and pos in st_pos) or path[-1] == pos:
                        probs.append(0)
                    else:
                        probs.append((tau[i][j]**alpha)*((1/time_matrix[i][j])**beta)*w)
                probs = list_norm(probs)
                next = random.choices(pos_list, weights=probs)[0]
                j = pos_idx(next)
                path.append(next)
                duration += time_matrix[i][j]*1.2
            all_paths.append((path,duration))
        
        tau = tau_ev(tau, rho)
        for path, duration in all_paths:
            if missed_mndt(path) == 0:
                penalty_mndt = 0
            penalty_mndt = missed_mndt(path)
            if path[-1] == finish:
                penalty_end = 0
            score = Q/(abs(duration-L_target)+1+penalty_end+penalty_mndt) 
            for a in range(len(path)-1):
                i = pos_idx(path[a])
                j = pos_idx(path[a+1])
                tau[i][j] += score
            if score > best_score:
                best_score = score
                best_path = path
                final_dur = duration
    if positions[path[-1]][1] == False:
        best_path.append('17-SitRelax.py')
        final_dur += span_time

    best_path.append(finish)
    final_dur += positions[finish][2]

                
    return best_path, final_dur, missed_mndt(best_path)

