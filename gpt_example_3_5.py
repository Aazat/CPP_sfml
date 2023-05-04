import pygame
import numpy as np

class Gridworld:
    def __init__(self, GRID_HEIGHT=5, GRID_WIDTH= 5 ):
        self.GRID_WIDTH = GRID_WIDTH
        self.GRID_HEIGHT = GRID_HEIGHT
        
        
        self.grid = np.zeros((self.GRID_HEIGHT, self.GRID_WIDTH))
        self.ACTIONS = ["up", "down", "left", "right"]
        self.actions = [0,1,2,3]
        self.SPECIAL_STATES = {(0, 1): (10, (4,1)), (0, 3): (5, (2,3))}
        self.agent_pos = [0, 0]
        # self.screen = pygame.display.set_mode((self.GRID_WIDTH*self.CELL_WIDTH, self.GRID_HEIGHT*self.CELL_HEIGHT))

        self.CELL_WIDTH = 100
        self.CELL_HEIGHT = 100
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)

    def reset(self):
        self.grid = np.zeros((self.GRID_HEIGHT, self.GRID_WIDTH))
        self.agent_pos = [0, 0]

    def step(self, action:str, i:int, j:int):
        reward = 0        

        if (i,j) in self.SPECIAL_STATES:
            reward , (i,j) = self.SPECIAL_STATES[(i,j)]
            return i,j, reward
        
        state = (i,j)
        # Move the agent according to the action
        if action == "up":
            i = max(i - 1, 0)
        elif action == "down":
            i = min(i + 1, self.GRID_HEIGHT-1)
        elif action == "left":
            j = max(j - 1, 0)
        elif action == "right":
            j = min(j + 1, self.GRID_WIDTH-1)


        if state == (i,j):
            reward = -1

        return i,j, reward
        

    def draw(self):
        self.screen.fill(self.BLACK)

        # Draw the cells of the gridworld
        for i in range(self.GRID_HEIGHT):
            for j in range(self.GRID_WIDTH):
                rect = pygame.Rect(j*self.CELL_WIDTH, i*self.CELL_HEIGHT, self.CELL_WIDTH, self.CELL_HEIGHT)
                if self.grid[i][j] == 1:
                    pygame.draw.rect(self.screen, self.GREEN, rect)
                elif (i, j) in self.SPECIAL_STATES:
                    pygame.draw.rect(self.screen, self.BLUE, rect)
                else:
                    pygame.draw.rect(self.screen, self.WHITE, rect)
                pygame.draw.rect(self.screen, self.BLACK, rect, 1)

        # Draw the agent on the gridworld
        agent_rect = pygame.Rect(self.agent_pos[1]*self.CELL_WIDTH, self.agent_pos[0]*self.CELL_HEIGHT, self.CELL_WIDTH, self.CELL_HEIGHT)
        pygame.draw.rect(self.screen, self.RED, agent_rect)
        pygame.display.update()

    def policy_evaluation(self, gamma, threshold):        
        while True:
            delta = 0
            for i in range(self.GRID_HEIGHT):
                for j in range(self.GRID_WIDTH):
                    v = self.grid[i,j] 
                    value = 0
                    for action in self.ACTIONS:
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
#     action = np.random.choice(self.ACTIONS)
#     print(action)
#     state, reward = gridworld.step(action)
#     print(state, reward)
#     gridworld.draw()            
#     pygame.time.delay(500)

gridworld.policy_evaluation(gamma, threshold)
print(np.round(gridworld.grid,2))

# gridworld.close()
