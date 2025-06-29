import unittest
from brain import BriansBrain, OFF, ON, DYING


class TestBriansBrain(unittest.TestCase):
    
    def setUp(self):
        self.sim = BriansBrain(5, 5)
    
    def test_initial_state(self):
        for y in range(self.sim.height):
            for x in range(self.sim.width):
                self.assertEqual(self.sim.grid[y][x], OFF)
    
    def test_count_neighbors(self):
        self.sim.grid[1][1] = ON
        self.sim.grid[1][2] = ON
        self.sim.grid[2][1] = DYING
        
        count = self.sim.count_neighbors(1, 1)
        self.assertEqual(count, 1)
    
    def test_basic_rules(self):
        self.sim.grid[2][1] = ON
        self.sim.grid[2][3] = ON
        
        neighbor_count = self.sim.count_neighbors(2, 2)
        print(f"Cell (2,2) has {neighbor_count} ON neighbors")
        next_state = self.sim.get_next_state(2, 2)
        self.assertEqual(next_state, ON)
        
        self.sim.step()
        self.assertEqual(self.sim.grid[2][1], DYING)
        self.assertEqual(self.sim.grid[2][2], ON)
        self.assertEqual(self.sim.grid[2][3], DYING)
        
        self.sim.step()
        self.assertEqual(self.sim.grid[2][1], OFF)
        self.assertEqual(self.sim.grid[2][2], DYING)
        self.assertEqual(self.sim.grid[2][3], OFF)
    
    def test_step_generation(self):
        initial_gen = self.sim.generation
        self.sim.step()
        self.assertEqual(self.sim.generation, initial_gen + 1)


if __name__ == '__main__':
    unittest.main() 