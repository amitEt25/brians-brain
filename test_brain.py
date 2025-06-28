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
        self.sim.grid[1][1] = ON
        self.sim.grid[1][3] = ON
        next_state = self.sim.get_next_state(1, 2)
        self.assertEqual(next_state, ON)
        
        next_state = self.sim.get_next_state(1, 1)
        self.assertEqual(next_state, DYING)
        
        self.sim.grid[2][2] = DYING
        next_state = self.sim.get_next_state(2, 2)
        self.assertEqual(next_state, OFF)
    
    def test_step_generation(self):
        """Test that step() increments generation counter"""
        initial_gen = self.sim.generation
        self.sim.step()
        self.assertEqual(self.sim.generation, initial_gen + 1)


if __name__ == '__main__':
    unittest.main() 