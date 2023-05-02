import pygame
import numpy as np

# Define the gridworld dimensions and the colors for the cells
GRID_WIDTH = 5
GRID_HEIGHT = 5
CELL_WIDTH = 100
CELL_HEIGHT = 100
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define the special states and their rewards
SPECIAL_STATES = {(0, 1): (10, [4,1]), (0, 3): (5,[2,3])}
ACTIONS = ["up", "down", "left", "right"]
actions = [0,1,2,3]
class Gridworld:
    def __init__(self):
        self.grid = np.zeros((GRID_HEIGHT, GRID_WIDTH))
        self.agent_pos = [0, 0]
        self.screen = pygame.display.set_mode((GRID_WIDTH*CELL_WIDTH, GRID_HEIGHT*CELL_HEIGHT))

    def reset(self):
        self.grid = np.zeros((GRID_HEIGHT, GRID_WIDTH))
        self.agent_pos = [0, 0]

    def step(self, action:str):
        reward = 0        

        if tuple(self.agent_pos) in SPECIAL_STATES:
            reward , self.agent_pos = SPECIAL_STATES[tuple(self.agent_pos)]
            return self.agent_pos, reward
        
        state = self.agent_pos[:]
        # Move the agent according to the action
        if action == "up":
            self.agent_pos[0] = max(self.agent_pos[0] - 1, 0)
        elif action == "down":
            self.agent_pos[0] = min(self.agent_pos[0] + 1, GRID_HEIGHT-1)
        elif action == "left":
            self.agent_pos[1] = max(self.agent_pos[1] - 1, 0)
        elif action == "right":
            self.agent_pos[1] = min(self.agent_pos[1] + 1, GRID_WIDTH-1)


        if state == self.agent_pos:
            reward = -1

        return self.agent_pos, reward
    
    def step_new(self, action:int):

        if tuple(self.agent_pos) in SPECIAL_STATES:
            reward , self.agent_pos = SPECIAL_STATES[tuple(self.agent_pos)]
            return self.agent_pos, reward
        
        if action == 0:  # up
            if self.agent_pos[0] == 0:
                reward = -1
            else:
                self.agent_pos[0] -= 1
                reward = 0
        elif action == 1:  # down
            if self.agent_pos[0] == GRID_HEIGHT - 1:
                reward = -1
            else:
                self.agent_pos[0] += 1
                reward = 0
        elif action == 2:  # left
            if self.agent_pos[1] == 0:
                reward = -1
            else:
                self.agent_pos[1] -= 1
                reward = 0
        elif action == 3:  # right
            if self.agent_pos[1] == GRID_WIDTH - 1:
                reward = -1
            else:
                self.agent_pos[1] += 1
                reward = 0
        

        return self.agent_pos, reward

    def draw(self):
        self.screen.fill(BLACK)

        # Draw the cells of the gridworld
        for i in range(GRID_HEIGHT):
            for j in range(GRID_WIDTH):
                rect = pygame.Rect(j*CELL_WIDTH, i*CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
                if self.grid[i][j] == 1:
                    pygame.draw.rect(self.screen, GREEN, rect)
                elif (i, j) in SPECIAL_STATES:
                    pygame.draw.rect(self.screen, BLUE, rect)
                else:
                    pygame.draw.rect(self.screen, WHITE, rect)
                pygame.draw.rect(self.screen, BLACK, rect, 1)

        # Draw the agent on the gridworld
        agent_rect = pygame.Rect(self.agent_pos[1]*CELL_WIDTH, self.agent_pos[0]*CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT)
        pygame.draw.rect(self.screen, RED, agent_rect)
        pygame.display.update()

    def policy_evaluation(self, gamma, threshold):        
        while True:
            delta = 0
            for i in range(GRID_HEIGHT):
                for j in range(GRID_WIDTH):
                    v = self.grid[i,j] 
                    value = 0
                    for action in ACTIONS:
                        next_state, reward = self.step(action)
                        # print(next_state, reward)
                        value += 0.25 * (reward + gamma*self.grid[next_state[0], next_state[1]])
                    self.grid[i,j] = value
                    delta = max(delta, abs(v - self.grid[i, j]))
            if delta < threshold:
                break

    def close(self):
        pygame.quit()

gridworld = Gridworld()
gamma = 0.9
threshold = 1e-4
# Simulate the gridworld and visualize it
for i in range(50):
    action = np.random.choice(actions)
    print(ACTIONS[action])
    state, reward = gridworld.step(action)
    gridworld.draw()            
    pygame.time.delay(500)

# gridworld.policy_evaluation(gamma, threshold)
print(gridworld.grid)

# gridworld.close()
