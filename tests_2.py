from mcts_node import NimPiles
from mcts import MCTS
from gen import generate_random_piles
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def get_real_answer(heaps):
    xr = 0
    for x in heaps:
        xr ^= x
    if xr == 0:
        return 0 
    return 1 

dataset = []
RUN = 50
for i in range(RUN):
    sz = random.randint(1, 5)
    mx_sz = 10
    lst = generate_random_piles(sz, mx_sz)
    dataset.append(lst)

episode_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000]
correctness_percentages = []
for EPS in episode_list:
    correct = 0
    nodes_visited = 0
    for i in range(RUN):
        tree = MCTS()
        piles = NimPiles(dataset[i])

        for j in range(EPS):
            tree.do_rollout(piles)

        cnt = 0
        while not piles.is_terminal():
            piles = tree.choose(piles)
            cnt += 1
        
        if cnt % 2 == get_real_answer(lst):
            correct += 1
        
        nodes_visited += tree.get_nodes_visited()

    correctness_percentage = correct / RUN * 100
    
    correctness_percentages.append(correctness_percentage)

    print(f'Percentage Correctness at {EPS} rollouts is {correctness_percentage}%')
    print(f'Average Number of Nodes visted is {nodes_visited / RUN}')

plt.plot(episode_list, correctness_percentages, marker='o')
plt.xlabel('Number of Rollouts (EPS)')
plt.ylabel('Percentage Correctness')
plt.title('Percentage Correctness vs Number of Rollouts')
plt.grid(True)
plt.show()
