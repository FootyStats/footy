import numpy as np
import unittest

from parameterized import parameterized

from footy import Footy


class TestFootyClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Setup the class for testing.

        This sets the data as it was with one game to go at the end of the
        English Premier League in May 2009.

        References
        ----------
        Spiegelhalter, D. (2009). The professor’s Premiership probabilities.
        [online] BBC News. Available
        at: http://news.bbc.co.uk/1/hi/programmes/more_or_less/8062277.stm
        [Accessed 29 Aug. 2020].
        """
        footy = Footy()
        footy.add_team('Arsenal', 64, 36, 18, 19, 69)
        footy.add_team('Aston Villa', 53, 48, 18, 19, 59)
        footy.add_team('Blackburn', 40, 60, 18, 19, 40)
        footy.add_team('Bolton', 41, 52, 19, 18, 41)
        footy.add_team('Chelsea', 65, 22, 19, 18, 80)
        footy.add_team('Everton', 53, 37, 19, 18, 60)
        footy.add_team('Fulham', 39, 32, 18, 19, 53)
        footy.add_team('Hull', 39, 63, 18, 19, 35)
        footy.add_team('Liverpool', 74, 26, 18, 19, 83)
        footy.add_team('Man City', 57, 50, 18, 19, 47)
        footy.add_team('Man United', 67, 24, 19, 18, 87)
        footy.add_team('Middlesbrough', 27, 55, 19, 18, 32)
        footy.add_team('Newcastle', 40, 58, 19, 18, 34)
        footy.add_team('Portsmouth', 38, 56, 19, 18, 41)
        footy.add_team('Stoke', 37, 51, 19, 18, 45)
        footy.add_team('Sunderland', 32, 51, 18, 19, 36)
        footy.add_team('Tottenham', 44, 42, 19, 18, 51)
        footy.add_team('West Brom', 36, 67, 19, 18, 31)
        footy.add_team('West Ham', 40, 44, 18, 19, 48)
        footy.add_team('Wigan', 33, 45, 18, 19, 42)
        footy.average_goals_scored_by_a_home_team(1.36)
        footy.average_goals_scored_by_an_away_team(1.06)
        cls.footy = footy

    @parameterized.expand([
        ([1, 0, 0], [100.0, 0.0, 0.0], 0.0),
        ([0, 1, 0], [100.0, 0.0, 0.0], 2.0),
        ([0, 0, 1], [100.0, 0.0, 0.0], 2.0),
        ([1, 0, 0], [70.02, 18.43, 9.56], 0.13),
        ([0, 1, 0], [70.02, 18.43, 9.56], 1.16),
        ([0, 0, 1], [70.02, 18.43, 9.56], 1.34)
    ])
    def test_brier_score(self, y_true, y_prob, expected_answer):
        footy = self.footy
        y_true = np.array(y_true) / 100.0
        y_prob = np.array(y_prob) / 100.0
        bs = footy.brier_score(y_true, y_prob)
        self.assertEqual(bs, expected_answer)

    @parameterized.expand([
        ('Arsenal', 'Stoke', [72.0, 19.0, 10.0]),
        ('Aston Villa', 'Newcastle', [62.0, 21.0, 17.0]),
        ('Blackburn', 'West Brom', [54.0, 23.0, 23.0]),
        ('Fulham', 'Everton', [35.0, 35.0, 30.0]),
        ('Hull', 'Man United', [9.0, 19.0, 72.0]),
        ('Liverpool', 'Tottenham', [72.0, 20.0, 9.0]),
        ('Man City', 'Bolton', [59, 22, 19]),
        ('Sunderland', 'Chelsea', [10, 25, 65]),
        ('West Ham', 'Middlesbrough', [57, 28, 15]),
        ('Wigan', 'Portsmouth', [44, 32, 25])
    ])
    def test_outcome(self, home_team, away_team, expected_probabilities):
        """
        Test that the probabilities are calculated correctly and compare
        against values calculated by Prof Spiegelhalter.

        Parameters
        ----------
        home_team : str
            The name of the home team.
        away_team : str
            The name of the away team.
        expected_probabilities : List of int
            The first element is the probability of the home team winning.
            The second element is the probability of a score draw.
            The third element is the probability of the away team winning.
        """
        footy = self.footy
        probabilities = footy.outcome_probability(home_team, away_team, False)
        (home_team_win_probability, score_draw_probability,
         away_team_win_probability) = probabilities

        # We allow some wriggle room for the values calculated.  This is
        # because the maximum number of goals we test up to is six.  However,
        # the sum of all the probabilities for the Arsenal v Stoke games
        # is actually 98.01 (not a perfect 100.0).  Therefore we subtract the
        # sum from 100.0 and use the result as a variance to compare against.
        probabilities_sum = home_team_win_probability
        probabilities_sum += score_draw_probability
        probabilities_sum += away_team_win_probability
        variance = abs(100.0 - probabilities_sum)

        for expected_probability in expected_probabilities:
            min_val = expected_probability - variance
            max_val = expected_probability + variance
            msg = f'The expected probability ({expected_probability}) '
            msg += f'must be between {min_val} and {max_val}.'
            self.assertGreaterEqual(expected_probability, min_val, msg)
            self.assertLessEqual(expected_probability, max_val, msg)


if __name__ == '__main__':
    unittest.main()
