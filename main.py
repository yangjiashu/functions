import numpy as np
import Airline
import Q_lam

if __name__ == '__main__':
    # block-1 initial
    capacity = 10
    times = np.array([5, 4, 3, 2, 1])
    states = []
    for c in range(capacity):
        for t in times:
            states.append(tuple([c,t]))

    
    RL = Q_lamine()
    iter_times = 1000

    # block-2 iteration
    for _ in range(iter_times + 1):
        s = env.reset()
        a = np.random.choice()
    
