import unittest
import numpy as np
import pandas as pd
from montecarlo import Die, Game, Analyzer


class MonteCarloTestCase(unittest.TestCase):
    def test_1_die_init(self):
        d = Die(np.array([1, 2, 3, 4, 5, 6]))

        self.assertTrue(isinstance(d, Die))

    def test_2_adj_weights(self):
        d = Die(np.array([1,2,3,4,5,6]))

        d.adj_weights(4, 10)

        self.assertEqual(d._die_df.index[3], 4)
        self.assertEqual(d._die_df.at[d._die_df.index[3], 'Weights'], 10)
        self.assertTrue(type(d._die_df) == pd.DataFrame)

    def test_3_die_roll(self):
        d = Die(np.array([1,2,3,4,5,6]))
        d.adj_weights(4, 10)

        result = d.die_roll(10)

        self.assertTrue(type(result) == list)

    def test_4_show_df(self):
        d = Die(np.array([1, 2, 3, 4, 5, 6]))
        d.adj_weights(4, 10)
        d.die_roll(10)

        df = d.show_df()

        self.assertTrue(type(df) == pd.DataFrame)

    def test_5_game_init(self):
        die1 = Die(np.array([1, 2, 3, 4, 5, 6]))
        die2 = Die(np.array([1, 2, 3, 4, 5, 6]))

        g = Game([die1, die2])

        self.assertTrue(isinstance(g, Game))

    def test_6_play(self):
        d = Die(np.array([1, 2, 3, 4, 5, 6]))
        d.adj_weights(4, 10)
        d.die_roll(10)
        g = Game([d, d, d])

        g = g.play(5)

        self.assertTrue(type(g) == pd.DataFrame)

    def test_7_recent_play(self):
        d = Die(np.array([1, 2, 3, 4, 5, 6]))
        d.adj_weights(4, 10)
        d.die_roll(10)
        g = Game([d, d, d])
        g.play(5)

        wide_df = g.recent_play()
        nar_df = g.recent_play('narrow')

        self.assertTrue(type(wide_df) == pd.DataFrame)
        self.assertTrue(type(nar_df) == pd.DataFrame)

    def test_8_analyzer_init(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die1 = Die(faces)
        die2 = Die(faces)
        g = Game([die1, die2])

        a = Analyzer(g)

        self.assertTrue(isinstance(a, Analyzer))

    def test_9_jackpot(self):
        d = Die(np.array([1, 2, 3, 4, 5, 6]))
        d.adj_weights(4, 10)
        d.die_roll(10)
        g = Game([d, d, d])
        g.play(5)
        g.recent_play()
        a = Analyzer(g)

        jkpot = a.jackpot()

        self.assertTrue(type(jkpot) == int)

    def test_10_face_counts(self):
        d = Die(np.array([1, 2, 3, 4, 5, 6]))
        d.adj_weights(4, 10)
        d.die_roll(10)
        g = Game([d, d, d])
        g.play(5)
        g.recent_play()
        a = Analyzer(g)

        face = a.face_counts()

        self.assertTrue(type(face) == pd.DataFrame)

    def test_11_combo_count(self):
        d = Die(np.array([1, 2, 3, 4, 5, 6]))
        d.adj_weights(4, 10)
        d.die_roll(10)
        g = Game([d, d, d])
        g.play(5)
        g.recent_play()
        a = Analyzer(g)

        combo = a.combo_count()

        self.assertTrue(type(combo) == pd.DataFrame)

    def test_12_perm_count(self):
        d = Die(np.array([1, 2, 3, 4, 5, 6]))
        d.adj_weights(4, 10)
        d.die_roll(10)
        g = Game([d, d, d])
        g.play(5)
        g.recent_play()
        a = Analyzer(g)

        perm = a.perm_count()

        self.assertTrue(type(perm) == pd.DataFrame)

if __name__ == '__main__':
    unittest.main(verbosity=3)
