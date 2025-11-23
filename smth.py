import os
import sys
import time
import pickle

pkl_file = 'positions2.pkl'

def positions():

    standing = {'11-Stand.py': [True, True], 
    '4-Arms_opening.py': [None, None],
    '13-Rotation_foot_LLeg.py': [True, True], 
    '8-Move_backward.py': [True, True], 
    '6-Crouch.py': [True, False],
    'BirthdayDance.py': [True, True], 
    '9-Diagonal_left.py': [True, True], 
    '2-Right_arm.py': [None, None],
    '16-Sit.py': [True,False], 
    'ArmDanceSX.py': [True, True], 
    '7-Move_forward.py': [True, True],
    'Sprinkler1.py': [True, True], 
    '5-Union_arms.py': [None, None], 
    'WipeForehead.py': [None, True],
    '10-Diagonal_right.py': [True, True], 
    '3-Double_movement.py': [None, None], 
    '12-Rotation_foot_RLeg.py': [True, True],
    '15-StandZero.py': [True, True], 
    'Hello.py': [None, True], 
    '14-StandInit.py': [True, True],
    '17-SitRelax.py': [False, None], 
    '1-Rotation_handgun_object.py': [None, None]}

    robotIP = '127.0.0.1'
    port = 37163

    for pos in standing:
        if standing[pos][0] == True:
            os.system("python2 moves/project_positions/11-Stand.py " + robotIP + " " + str(port))   
        elif standing[pos][0] == False:
            os.system("python2 moves/project_positions/16-Sit.py " + robotIP + " " + str(port))
        start = time.time()
        os.system("python2 moves/project_positions/" + pos + " " + robotIP + " " + str(port))
        end = time.time()
        standing[pos].append(end-start)

    return standing

def get_positions():
    if os.path.exists(pkl_file):
        with open(pkl_file, "rb") as f:
            return pickle.load(f)

    poses = positions()

    with open(pkl_file, "wb") as f:
        pickle.dump(poses, f)

    return poses
