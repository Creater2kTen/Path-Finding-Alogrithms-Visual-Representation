from constants import width, height, square_size, blue2, rows, cols, grid_height, grid_width, custom_color_1, WHITE, RED, rrt_x, rrt_y, rrt_border, BLACK
from node import Node
import pygame
import time


class Window:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Pathfinding Visualizer ")
        gameIcon = pygame.image.load('./icon/icon.png')
        pygame.display.set_icon(gameIcon)
        self.font = pygame.font.SysFont("Arial", 15)
        self.win = pygame.display.set_mode((grid_width, grid_height))
        self.selected_algorithm = None
        self.speed = "Fast"
        self.paused = False
        self.previous_results = []
        self.is_print = None
        

    def make_grid(self):
        # Make an N by N grid with each index implemented as a node
        grid = []
        for i in range(rows):
            grid.append([])
            for j in range(cols):
                grid[i].append(Node(i, j))
        
        return grid

    def draw_grid_rrt(self):
        pygame.draw.rect(screen,BLACK,(rrt_x,rrt_y,574,470),GAME_border)


    def draw_grid(self):
        for i in range(rows + 1):
            pygame.draw.line(self.win, (0, 0, 0), (i * square_size, 1), (i * square_size, width), 2)
            pygame.draw.line(self.win, (0, 0, 0), (1, i * square_size), (width, i * square_size), 2)
    
    def draw_buttons(self):
        
        pygame.draw.rect(self.win, (0, 0, 0), (square_size * 41 + 5, square_size - 10 , square_size * 9 + 5, square_size * 27 + 2), border_radius=10)
        pygame.draw.rect(self.win, WHITE, (square_size * 41 + 7, square_size - 10 + 2 , square_size * 9 + 1, square_size * 27 - 2 ), border_radius=10)
        file=["a_star_m", "a_star_e", "dijkstras", "depth_first_search", "breadth_first_search", "greedy_best_first_search", "rrt"] #, "d_star_lite"]
        algo=["A* Search Manh.", "A* Search Eucli.", "Dijkstra's", "Depth First", "Breadth First", "Greedy Best First", "RRT"] #, " D* Search", ]
        gap = 0
        for i in range(7):
            pygame.draw.rect(self.win, (0, 0, 0), (square_size * 41 + 15 , square_size + gap, square_size * 8 , square_size * 2))
            if self.selected_algorithm == file[i]:
                pygame.draw.rect(self.win, blue2, (square_size * 41 + 16 , square_size + 1 + gap, square_size * 8 - 2, square_size * 2 - 2))
            else:
                pygame.draw.rect(self.win, custom_color_1, (square_size * 41 + 16 , square_size + 1 + gap, square_size * 8 - 2, square_size * 2 - 2))
            text = self.font.render(algo[i], True, WHITE)
            self.win.blit(text, (square_size * 42 + 5, square_size + 10 + gap ))
            gap+=50
        
        # print(square_size + gap, square_size + gap + square_size * 2)

        pygame.draw.rect(self.win, (0, 0, 0), (square_size * 41 + 15 , square_size + gap, square_size * 8 , square_size * 2))
        if self.is_print == "Print":
            pygame.draw.rect(self.win, blue2, (square_size * 41 + 16 , square_size + 1 + gap, square_size * 8 - 2, square_size * 2 - 2))
            time.sleep(1)
            self.is_print = "None"
        else:
            pygame.draw.rect(self.win, custom_color_1, (square_size * 41 + 16 , square_size + 1 + gap, square_size * 8 - 2, square_size * 2 - 2))
        text = self.font.render("Print", True, WHITE)
        self.win.blit(text, (square_size * 42 + 5, square_size + 10 + gap ))

        # Draw image
        gap+=50
        picture = pygame.image.load('./icon/icon.png')
        picture = pygame.transform.scale(picture, (100,100))
        pygame.draw.rect(self.win, WHITE, (square_size * 41 + 16 , square_size + 1 + gap, 200, 300))
        self.win.blit(picture, (square_size * 42 , square_size + 10 + gap ))

    
    def draw_results(self):
        pygame.draw.rect(self.win, (0, 0, 0), (square_size - 5 , square_size * 41 + 10 ,square_size * 50 -5  , square_size * 7 - 10 ))
        if self.previous_results:
            text = pygame.font.SysFont("Arial", 20).render(self.previous_results[0]+" :", True, WHITE)
            self.win.blit(text, (square_size + 10 , square_size * 41 + 17))
            for i in range(0,len(self.previous_results)-1):
                text = pygame.font.SysFont("Arial", 18).render(self.previous_results[i+1], True, WHITE)
                self.win.blit(text, (square_size * 27 + 10 , square_size * (41+(2*i)) + 17))

    def draw_solution(self, start, end, path, draw):
        # Total cost (sum of the weights of all nodes from start to end) of path found
        cost = 0
        end.place_end()

        # Backtrack from end node to start node and draw the path found
        current = end
        while current in path:
            if current not in (start, end):
                cost += current.weight
            current = path[current]
            current.draw_path()
            draw()

        start.place_start()
        print(cost)
        return cost
        
    def draw(self, grid=None):
        # self.win.fill((255, 255, 255))
        # if self.selected_algorithm == "rrt":
        #     self.draw_grid_rrt()
        if self.selected_algorithm and self.selected_algorithm!="rrt":
            if grid :
                for row in grid:
                    for node in row:
                        node.draw(self.win)
                        if node.weight != 1:
                            text = self.font.render("..", True, (0, 0, 0))
                            self.win.blit(text, (node.row * square_size + 4, node.col * square_size))
            self.draw_grid()
        
        pygame.draw.rect(self.win,BLACK,(1,1,613,613),3)
        self.draw_buttons()
        self.draw_results()

        pygame.display.update()

    def get_mouse_position(self, pos):
        row = pos[0] // square_size
        col = pos[1] // square_size
        return row, col


