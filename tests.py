import unittest
from unittest.mock import patch
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
    
    '''Move Distance'''
    def test_move_distance_forward(self):
        length = Robot()
        self.assertEqual(length.forward(1), 2, 'The returned position is wrong')

    def test_move_distance_backward(self):
        length = Robot()
        self.assertEqual(length.backward(1), 0, 'The returned position is wrong')

    '''Move Direction'''
    def setUp(self):
        self.robot = Robot()
        self.robot.is_placed = True

    @patch.object(Robot, 'backward')
    @patch.object(Robot, 'forward')
    def test_move_direction(self, mock_forward, mock_backward):
        self.robot.face = "North"
        initial_pos = self.robot.posY
        self.robot.move()
        mock_forward.assert_called_once_with(initial_pos)
        mock_backward.assert_not_called()
        mock_forward.reset_mock()
        mock_backward.reset_mock()
 
        self.robot.face = "South"
        initial_pos = self.robot.posY
        self.robot.move()
        mock_backward.assert_called_once_with(initial_pos)
        mock_forward.assert_not_called()
        mock_forward.reset_mock()
        mock_backward.reset_mock()
 
        self.robot.face = "East"
        initial_pos = self.robot.posX
        self.robot.move()
        mock_forward.assert_called_once_with(initial_pos)
        mock_backward.assert_not_called()
        mock_forward.reset_mock()
        mock_backward.reset_mock()
 
        self.robot.face = "West"
        initial_pos = self.robot.posX
        self.robot.move()
        mock_backward.assert_called_once_with(initial_pos)
        mock_forward.assert_not_called()
        mock_forward.reset_mock()
        mock_backward.reset_mock()
 
if __name__ == '__main__':
    unittest.main()