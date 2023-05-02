import numpy as np

# initialize gridworld
nrow, ncol = 5, 5
grid = np.zeros((nrow, ncol))

# initialize state-value function
V = {}
for i in range(1, nrow+1):
    for j in range(1, ncol+1):
        V[(i,j)] = 0

# set up policy
policy = np.ones((nrow, ncol, 4)) / 4  # equally likely to choose any action

# set up discount factor
gamma = 0.9

# set up tolerance level
theta = 1e-5

def step(action, i, j):
    if a == 0:  # up
        i_new, j_new = max(i-1, 1), j
    elif a == 1:  # down
        i_new, j_new = min(i+1, nrow), j
    elif a == 2:  # left
        i_new, j_new = i, max(j-1, 1)
    elif a == 3:  # right
        i_new, j_new = i, min(j+1, ncol)
    r = -1 if i == i_new and j == j_new else 0  # penalty for moving off grid
    if (i,j) == (1,2):
        r, i_new, j_new = 10, 5, 1
    elif (i,j) == (1,4):
        r, i_new, j_new = 5, 3, 4
    return i_new, j_new, r

# policy evaluation loop
delta = theta + 1
while delta > theta:
    delta = 0
    for i in range(1, nrow+1):
        for j in range(1, ncol+1):
            v = V[(i,j)]
            v_new = 0
            for a in range(4):
                i_new, j_new, r = step(a, i, j)
                v_new += policy[i-1,j-1,a] * (r + gamma * V[(i_new,j_new)])
            V[(i,j)] = v_new
            delta = max(delta, abs(v - V[(i,j)]))

# print state-value function
for i in range(1,6):
    for j in range(1,6):
        print("{:.2f}".format(V[(i,j)]), end="\t")
    print()
