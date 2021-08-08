try:
    import pygame
    from os import path
    import time
except:
    from Install_requirements import *
    import pygame
    from os import path 
    import time



from window import Window
from algorithms import a_star_m,a_star_e, dijkstras, depth_first_search, breadth_first_search, greedy_best_first_search, prims
import rrt




def start_visualizer():
    win = Window()
    win.win.fill((255, 255, 255))
    grid = win.make_grid()
    carImg = pygame.image.load('./icon/icon.png')
    win.win.blit(carImg, (651 ,460))
    start = None
    end = None
    win.draw(grid)

    running = True
    while running:
        if win.selected_algorithm=="rrt":
            win.draw()
        else:
            win.draw(grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Left click will place nodes
            if pygame.mouse.get_pressed(3)[0]:
                pos = pygame.mouse.get_pos()
                row, col = win.get_mouse_position(pos)
                # print('obsticle')

                # Clicking within the grid
                if 0 <= row <= 40 and 0 <= col <= 40:
                    node = grid[row][col]

                    # If there is no start node and you are not clicking on end node
                    if not start and node != end:
                        start = node
                        start.place_start()
                    
                    # If there is no end node and you are not clicking on start node
                    elif not end and node != start:
                        end = node
                        end.place_end()

                    # If start and end nodes are defined and you are not clicking on them
                    elif node != start and node != end:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_w] and not node.is_wall():
                            node.reset_color()
                            node.place_weight()
                        else:
                            if node.weight == 1:
                                node.place_wall()
                
                # Selecting Algorithms / Heuristic
                
                elif 15 <= pos[1] <= 45:
                    win.selected_algorithm = "a_star_m"

                elif 65 <= pos[1] <= 95:
                    win.selected_algorithm = "a_star_e"

                elif 115 <= pos[1] <= 145:
                    win.selected_algorithm = "dijkstras"

                elif 165 <= pos[1] <= 195:
                    win.selected_algorithm = "depth_first_search"
                    
                elif 215 <= pos[1] <= 245:
                    win.selected_algorithm = "breadth_first_search"

                elif 265 <= pos[1] <= 295:
                    win.selected_algorithm = "greedy_best_first_search"

                elif 315 <= pos[1] <= 345:
                    win.selected_algorithm = "rrt"
                    rrt.run(win,lambda: win.draw())
                    start = None
                    end = None
                    for row in grid:
                        for node in row:
                            node.reset_color()
                            node.reset_weight()
                
                    
                
                # elif 365 <= pos[1] <= 395:
                #     # win.selected_algorithm = "d_star_lite"
                #     pygame.quit()
                #     from d_star import main
                #     print("D* Lite")
                # elif 415 <= pos[1] <= 445:
                
                elif 365 <= pos[1] <= 395:
                    if win.selected_algorithm:
                        win.is_print = "Print"
                        if win.selected_algorithm == "a_star_m":
                            loc="./Screenshoots/" + win.selected_algorithm + "/image.jpeg"
                            c=-1
                            while path.exists(loc):
                                c+=1
                                loc="./Screenshoots/" + win.selected_algorithm + "/image"+str(c)+".jpeg"
                            pygame.image.save_extended(win.win, loc)
                        
                        elif win.selected_algorithm == "greedy_best_first_search":
                            loc="./Screenshoots/" + win.selected_algorithm + "/image.jpeg"
                            c=-1
                            while path.exists(loc):
                                c+=1
                                loc="./Screenshoots/" + win.selected_algorithm + "/image"+str(c)+".jpeg"
                            pygame.image.save_extended(win.win, loc)
                        
                        elif win.selected_algorithm == "dijkstras":
                            loc="./Screenshoots/" + win.selected_algorithm + "/image.jpeg"
                            c=-1
                            while path.exists(loc):
                                c+=1
                                loc="./Screenshoots/" + win.selected_algorithm + "/image"+str(c)+".jpeg"
                            pygame.image.save_extended(win.win, loc)

                        elif win.selected_algorithm == "depth_first_search":
                            loc="./Screenshoots/" + win.selected_algorithm + "/image.jpeg"
                            c=-1
                            while path.exists(loc):
                                c+=1
                                loc="./Screenshoots/" + win.selected_algorithm + "/image"+str(c)+".jpeg"
                            pygame.image.save_extended(win.win, loc)
                        
                        elif win.selected_algorithm == "breadth_first_search":
                            loc="./Screenshoots/" + win.selected_algorithm + "/image.jpeg"
                            c=-1
                            while path.exists(loc):
                                c+=1
                                loc="./Screenshoots/" + win.selected_algorithm + "/image"+str(c)+".jpeg"
                            pygame.image.save_extended(win.win, loc)
                            
                        elif win.selected_algorithm == "a_star_e":
                            loc="./Screenshoots/" + win.selected_algorithm + "/image.jpeg"
                            c=-1
                            while path.exists(loc):
                                c+=1
                                loc="./Screenshoots/" + win.selected_algorithm + "/image"+str(c)+".jpeg"
                            pygame.image.save_extended(win.win, loc)
                        elif win.selected_algorithm == "rrt":
                            loc="./Screenshoots/" + win.selected_algorithm + "/image.jpeg"
                            c=-1
                            while path.exists(loc):
                                c+=1
                                loc="./Screenshoots/" + win.selected_algorithm + "/image"+str(c)+".jpeg"
                            pygame.image.save_extended(win.win, loc)                        
                       

                
                        
            # Right click will remove (reset) nodes
            elif pygame.mouse.get_pressed(3)[2]:
                row, col = win.get_mouse_position(pygame.mouse.get_pos())
                if 0 <= row <= 40 and 0 <= col <= 40:
                    node = grid[row][col]
                    if node == start:
                        start = None
                    elif node == end:
                        end = None
                    node.reset_color()
                    node.reset_weight()
            
            if event.type == pygame.KEYDOWN:

                # If start and end are defined and an algorithm is selected, run the algorithm
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            if node != start and node != end and not node.is_wall():
                                node.reset_color()

                            node.add_neighbours(grid)
                    
                    if win.selected_algorithm:
                        if win.selected_algorithm == "a_star_m":
                            a_star_m.algorithm(start, end, grid, lambda: win.draw(grid), win)
                             
                        elif win.selected_algorithm == "greedy_best_first_search":
                            greedy_best_first_search.algorithm(start, end, grid, lambda: win.draw(grid), win)
                             
                        elif win.selected_algorithm == "dijkstras":
                            dijkstras.algorithm(start, end, grid, lambda: win.draw(grid), win)
                            

                        elif win.selected_algorithm == "depth_first_search":
                            depth_first_search.algorithm(start, end, lambda: win.draw(grid), win)
                             
                        elif win.selected_algorithm == "breadth_first_search":
                            breadth_first_search.algorithm(start, end, grid, lambda: win.draw(grid), win)
                             
                        elif win.selected_algorithm == "a_star_e":
                            a_star_e.algorithm(start, end, grid, lambda: win.draw(grid), win)

                        elif win.selected_algorithm == "rrt":
                            print("rrt")
                            # import main
                            # main.run(win,lambda: win.draw())
                            # grid=[]



                
                # Clear the board
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    for row in grid:
                        for node in row:
                            node.reset_color()
                            node.reset_weight()
                
                # Generate a maze
                if event.key == pygame.K_g:
                    start, end, grid = prims.algorithm(grid, lambda: win.draw(grid), win)
                
    
    
    pygame.quit()


if __name__ == "__main__":
    start_visualizer()
