import unittest
from toy_robot import Robot

class TestCommands(unittest.TestCase):

    '''Validate Position'''
    def test_valid_position(self):
        position = Robot()
        self.assertTrue(position.valid_pos(3), 'Not a valid position on table')

    def test_invalid_position(self):
        position = Robot()
        self.assertFalse(position.valid_pos(3.4), 'Not a valid position on table')

    '''Validate Direction'''
    def test_valid_direction(self):
        direction = Robot()
        self.assertTrue(direction.valid_direction('south'), 'Not a valid direction')

    def test_invalid_direction(self):
        direction = Robot()
        self.assertFalse(direction.valid_direction('library'), 'Not a valid direction')


if __name__ == '__main__':
    unittest.main()