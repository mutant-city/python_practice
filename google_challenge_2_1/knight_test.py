import unittest
import knight

class KnightTestCase(unittest.TestCase):

    def setUp(self):
        self.game = knight.KnightMoves()

    def test_filter_bounds(self):
        result = self.game.calc_single_move((4,4))
        result = self.game.filter_bounds(result,(4,4))
        self.assertIn((2,3), result)
        self.assertIn((3,2), result)
        self.assertNotIn((6,3), result)
        self.assertNotIn((5,6), result)

    def test_calc_single_move(self):
        result = self.game.calc_single_move((4,4))
        self.assertIn((2,3), result)
        self.assertIn((2,5), result)
        self.assertIn((6,3), result)
        self.assertIn((6,5), result)
        self.assertIn((3,2), result)
        self.assertIn((5,2), result)
        self.assertIn((3,6), result)
        self.assertIn((5,6), result)

    def test_calc_all_next_moves(self):
        x_y_set = {(10,10)}
        result = self.game.calc_all_next_moves(x_y_set)
        print len(result)
        self.assertTrue(len(result) == 8)
        result = self.game.calc_all_next_moves(result)
        print len(result)
        result = self.game.calc_all_next_moves(result)
        print len(result)
        result = self.game.calc_all_next_moves(result)
        print len(result)
        result = self.game.calc_all_next_moves(result)
        print len(result)
        result = self.game.calc_all_next_moves(result)
        print len(result)
        result = self.game.calc_all_next_moves(result)
        print len(result)
        result = self.game.calc_all_next_moves(result)
        print len(result)
        result = self.game.calc_all_next_moves(result)
        print len(result)
        result = self.game.calc_all_next_moves(result)
        print len(result)
        # self.assertTrue(len(result) == (8^8))

if __name__ == '__main__':
    unittest.main()