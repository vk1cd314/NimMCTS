from gamestate import GameState
from minimax import MinimaxAgent
from alphabetaprune import AlphaBetaPruningAgent
from gen import generate_random_piles
import random
import math
import time

EPS = 50
dataset = []
for i in range(EPS):
    sz = random.randint(1, 4)
    mx_sz = 3
    lst = generate_random_piles(sz, mx_sz)
    dataset.append(lst)

start_time = time.time()
states_visited = 0
for i in range(EPS):
    initial_state = GameState(dataset[i])
    agent = MinimaxAgent()
    result = agent.minimax(initial_state, True)
    assert result == initial_state.get_real_answer()
    states_visited += agent.get_states_visited()
end_time = time.time()
print(f'Minimax took on average {(end_time - start_time) / EPS}s')
print(f'Average Number of States Visited {states_visited / EPS}')

start_time = time.time()
states_visited = 0
for i in range(EPS):
    initial_state = GameState(dataset[i])
    agent = AlphaBetaPruningAgent()
    result = agent.alphabetapruning(initial_state, -math.inf, math.inf, True)
    assert result == initial_state.get_real_answer()
    states_visited += agent.get_states_visited()
end_time = time.time()
print(f'AlphaBeta Pruning took on average {(end_time - start_time) / EPS}s')
print(f'Average Number of States Visited {states_visited / EPS}')
