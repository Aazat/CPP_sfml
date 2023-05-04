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
SPECIAL_STATES = {(0, 1): (10, (4,1)), (0, 3): (5, (2,3))}
ACTIONS = ["up", "down", "left", "right"]
actions = [0,1,2,3]
class Gridworld:
    def __init__(self):
        self.grid = np.zeros((GRID_HEIGHT, GRID_WIDTH))
        self.agent_pos = [0, 0]
        # self.screen = pygame.display.set_mode((GRID_WIDTH*CELL_WIDTH, GRID_HEIGHT*CELL_HEIGHT))

    def reset(self):
        self.grid = np.zeros((GRID_HEIGHT, GRID_WIDTH))
        self.agent_pos = [0, 0]

    def step(self, action:str, i:int, j:int):
        reward = 0        

        if (i,j) in SPECIAL_STATES:
            reward , (i,j) = SPECIAL_STATES[(i,j)]
            return i,j, reward
        
        state = (i,j)
        # Move the agent according to the action
        if action == "up":
            i = max(i - 1, 0)
        elif action == "down":
            i = min(i + 1, GRID_HEIGHT-1)
        elif action == "left":
            j = max(j - 1, 0)
        elif action == "right":
            j = min(j + 1, GRID_WIDTH-1)


        if state == (i,j):
            reward = -1

        return i,j, reward
        

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
                        next_state_x, next_state_y, reward = self.step(action,i,j)
                        
                        value += 0.25 * (reward + gamma*self.grid[next_state_x, next_state_y])
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
# for i in range(50):
#     action = np.random.choice(ACTIONS)
#     print(action)
#     state, reward = gridworld.step(action)
#     print(state, reward)
#     gridworld.draw()            
#     pygame.time.delay(500)

gridworld.policy_evaluation(gamma, threshold)
print(np.round(gridworld.grid,2))

# gridworld.close()
