import os, random, copy, sys, time

class Game:
    def_grid = [[0,0,0],[0,0,0],[0,0,0]]

    def __init__(self, grid=def_grid):
        self.grid=copy.deepcopy(grid)
    

    def run(self, grid_size_x, grid_size_y, num_iterations, tune=40):
        self.new_grid(grid_size_x, grid_size_y)
        self.randomize_grid(tune)
        for i in range(0, num_iterations):
            self.display_grid()
            self.scan_grid()
            time.sleep(2)

    def randomize_grid(self, tune=40):
        for i in self.grid:
            for num,j in enumerate(i):
                check_val = random.randint(0,100)
                if(check_val <= tune): 
                    i[num] = 1
                else:
                    i[num] = 0

    def new_grid(self, x, y):
        self.grid = []
        grid_x = [0] * x
        for i in range(0, y):  
            self.grid.append(copy.deepcopy(grid_x))
    
    def display_grid(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in self.grid:
            for j in i:
                sys.stdout.write(' ') if j == 0 else sys.stdout.write('*')
            print("")
    
    def scan_grid(self):
        for num_y,y in enumerate(self.grid):
            for num_x,x in enumerate(y):
                value = self.get_grid_item(num_x, num_y)
                num_live = self.scan_item(num_x,num_y)
                new_val = self.apply_rules(num_live, value)
                self.set_grid_item(num_x, num_y, new_val)
                
    def get_grid_item(self, x, y):
        return self.grid[y][x]

    def set_grid_item(self, x, y, val):
        self.grid[y][x] = val

    def apply_rules(self, num_live, current_val):
        # overpopulation and underpopulation 
        if((num_live > 3 or num_live < 2) and current_val == 1): return 0
        # stasis
        if((num_live == 2 or num_live == 3) and current_val == 1 ): return 1
        # reproduction
        if(num_live == 3 and current_val ==0): return 1
        return current_val

    def scan_item(self, x, y):
        num_live = 0
        check_list = self.new_check_list()
        check_list = self.filter_check_list(check_list, x,y)
        for key in check_list:
            num_live += check_list[key](self, x, y)
        return num_live

    def filter_check_list(self, check_list, x, y):
        max_x = len(self.grid[0]) - 1
        max_y = len(self.grid) - 1
        
        if(x > max_x or y > max_y): raise Exception('Max grid values exceeded!')

        # guards against grid edges
        if(x == 0):
            self.remove_from_list(check_list, 'top_left')
            self.remove_from_list(check_list, 'left')
            self.remove_from_list(check_list, 'bottom_left')
        
        if(y == 0):
            self.remove_from_list(check_list,'top_left')
            self.remove_from_list(check_list,'top')
            self.remove_from_list(check_list,'top_right')

        if(x == max_x):
            self.remove_from_list(check_list,'top_right')
            self.remove_from_list(check_list,'right')
            self.remove_from_list(check_list,'bottom_right')

        if(y == max_y):
            self.remove_from_list(check_list,'bottom_left')
            self.remove_from_list(check_list,'bottom')
            self.remove_from_list(check_list,'bottom_right')

        return check_list

    def remove_from_list(self, check_list, key):
        if(key in check_list): del check_list[key]
        return check_list

    def new_check_list(self):
        return {
            'top' : lambda self, x,y: self.grid[y-1][x],
            'top_right': lambda self, x,y: self.grid[y-1][x+1],
            'right': lambda self, x,y: self.grid[y][x + 1],
            'bottom_right': lambda self,x,y: self.grid[y+1][x+1],
            'bottom' : lambda self,x,y:self.grid[y+1][x],
            'bottom_left': lambda self,x,y: self.grid[y+1][x-1],
            'left': lambda self,x,y: self.grid[y][x - 1],
            'top_left': lambda self,x,y:self.grid[y-1][x-1]
        }

if __name__ == "__main__": 

    game = Game()
    width = int(sys.argv[1])
    height = int(sys.argv[2])
    iterations = int(sys.argv[3])
    if (len(sys.argv)>= 5):
        tune = int(sys.argv[4])
    else:
        tune = 30

    print("Running with width: %i, height: %i, iterations: %i, tune: %i" % (width,height,iterations,tune))
    val = raw_input("Press any key to continue or x to exit: ")
    if(val == "x"): 
        print("exiting")
        quit()
    game.run(width,height,iterations,tune)