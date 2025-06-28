import os
import random
import json


OFF = 0
ON = 1
DYING = 2

SYMBOLS = {
    OFF: ' ',
    ON: '█', 
    DYING: '░'
}


class BriansBrain:
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [[OFF for _ in range(width)] for _ in range(height)]
        self.next_grid = [[OFF for _ in range(width)] for _ in range(height)]
        self.generation = 0
    
    def load_seed_from_file(self, filepath: str) -> None:
        try:
            with open(filepath, 'r') as f:
                lines = f.readlines()
            
            self.grid = [[OFF for _ in range(self.width)] for _ in range(self.height)]
            
            pattern_height = len(lines)
            pattern_width = max(len(line.strip()) for line in lines)
            
            start_y = (self.height - pattern_height) // 2
            start_x = (self.width - pattern_width) // 2
            
            for y, line in enumerate(lines):
                line = line.strip()
                for x, char in enumerate(line):
                    if char in ['1', '2']:
                        state = int(char)
                        grid_y = start_y + y
                        grid_x = start_x + x
                        if 0 <= grid_y < self.height and 0 <= grid_x < self.width:
                            self.grid[grid_y][grid_x] = state
                            
        except FileNotFoundError:
            raise FileNotFoundError(f"Seed file '{filepath}' not found")
        except Exception as e:
            raise Exception(f"Error loading seed file: {e}")
    
    def generate_random_seed(self, seed_value: int) -> None:
        random.seed(seed_value)
        
        for _ in range(self.width * self.height // 10):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            self.grid[y][x] = ON
    
    def count_neighbors(self, x: int, y: int) -> int:
        count = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if self.grid[ny][nx] == ON:
                        count += 1
        return count
    
    def get_next_state(self, x: int, y: int) -> int:
        current_state = self.grid[y][x]
        
        if current_state == OFF:
            if self.count_neighbors(x, y) == 2:
                return ON
            return OFF
        elif current_state == ON:
            return DYING
        else:
            return OFF
    
    def step(self) -> None:
        for y in range(self.height):
            for x in range(self.width):
                self.next_grid[y][x] = self.get_next_state(x, y)
        
        self.grid, self.next_grid = self.next_grid, self.grid
        self.generation += 1
    
    def display(self) -> None:
        print('\033[H\033[J', end='')
        
        print(f"Brian's Brain - Generation {self.generation}")
        print("=" * (self.width + 2))
        
        for row in self.grid:
            print('|', end='')
            for cell in row:
                print(SYMBOLS[cell], end='')
            print('|')
        
        print("=" * (self.width + 2))
    
    def save_generation(self, output_dir: str) -> None:
        os.makedirs(output_dir, exist_ok=True)
        filename = os.path.join(output_dir, f"generation_{self.generation:04d}.json")
        
        with open(filename, 'w') as f:
            json.dump({
                'generation': self.generation,
                'width': self.width,
                'height': self.height,
                'grid': self.grid
            }, f, indent=2) 