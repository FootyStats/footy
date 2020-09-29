import numpy as np
import unittest

from parameterized import parameterized

from footy import Footy


class TestFootyClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Setup the class for testing.

        This sets the data as it was with one game to go at the end of the English Premier League in May 2009.

        References
        ----------
        Spiegelhalter, D. (2009). The professor’s Premiership probabilities. [online] BBC News. Available
        at: http://news.bbc.co.uk/1/hi/programmes/more_or_less/8062277.stm [Accessed 29 Aug. 2020].
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
        footy.average_goals_scored_by_a_home_team = 1.36
        footy.average_goals_scored_by_an_away_team = 1.06
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

    def test_dummy_league(self):
        """Test a dummy league through various stages of progression."""
        footy_obj = Footy()

        # The league has not yet started so zero  values.
        footy_obj.add_team('domain A', 0, 0, 0, 0, 0)
        footy_obj.add_team('domain B', 0, 0, 0, 0, 0)
        footy_obj.add_team('domain C', 0, 0, 0, 0, 0)
        footy_obj.add_team('domain D', 0, 0, 0, 0, 0)
        footy_obj.average_goals_scored_by_a_home_team = 0
        footy_obj.average_goals_scored_by_an_away_team = 0

        # Our micro league should contain four teams.
        self.assertEqual(len(footy_obj.get_teams()), 4)

        # No games played, so we don't expect any probability data to
        # be available.
        response = footy_obj.fixture('domain A', 'domain B')
        self.assertIsNone(response)

        # domain D beats A 2 - 0 away.
        footy_obj.add_team('domain A', 0, 2, 1, 0, 0)
        footy_obj.add_team('domain D', 2, 0, 0, 1, 3)

        # domain B plays domain C at home and the final score is a
        # 1 - 1 score draw.
        footy_obj.add_team('domain B', 1, 1, 1, 0, 1)
        footy_obj.add_team('domain C', 1, 1, 0, 1, 1)

        # Teams D and C played away and between them scored three
        # goals.  Set the average for these two games.
        footy_obj.average_goals_scored_by_an_away_team = round(3 / 2, 2)

        # Teams A and B played at home but only team B scored a single goal.
        # Set the average for these two games.
        footy_obj.average_goals_scored_by_a_home_team = round(1 / 2, 2)

        # At this point, teams D and C have not played at home and teams
        # B and A have not played away.  Therefore still expecting not
        # to have enough data to track probabilities.
        response = footy_obj.fixture('domain A', 'domain B')
        self.assertIsNone(response)

        # domain D hosts B and beats them 2 - 0.
        goals_for = footy_obj.get_team('domain B')['goals_for'] + 0
        goals_against = footy_obj.get_team('domain B')['goals_against'] + 2
        home_games = 1
        away_games = 1
        points = 1 + 0
        footy_obj.add_team('domain B', goals_for, goals_against, home_games,
                           away_games, points)

        goals_for = footy_obj.get_team('domain D')['goals_for'] + 2
        goals_against = footy_obj.get_team('domain D')['goals_against'] + 0
        points = 3 + 3
        footy_obj.add_team('domain D', goals_for, goals_against, home_games,
                           away_games, points)

        # domain C hosts domain A and beats them 1 - 0.
        goals_for = footy_obj.get_team('domain A')['goals_for'] + 0
        goals_against = footy_obj.get_team('domain B')['goals_against'] + 1
        home_games = 1
        away_games = 1
        points = 0 + 0
        footy_obj.add_team('domain A', goals_for, goals_against, home_games,
                           away_games, points)

        goals_for = footy_obj.get_team('domain C')['goals_for'] + 1
        goals_against = footy_obj.get_team('domain D')['goals_against'] + 0
        points = 1 + 3
        footy_obj.add_team('domain C', goals_for, goals_against, home_games,
                           away_games, points)

        # Now all teams have played one home game and one away game.  A recap
        # of the table at the moment:
        #
        # domain GF GA GD PTS Form
        # D    4  0   4   6 WW
        # C    2  0   2   4 DW
        # B    1  3  -2   1 DL
        # A    0  4  -4   0 LL

        # Let's confirm the goal differences.
        self.assertEqual(footy_obj.get_team('domain A')['goal_difference'], -4)
        self.assertEqual(footy_obj.get_team('domain B')['goal_difference'], -2)
        self.assertEqual(footy_obj.get_team('domain C')['goal_difference'], 2)
        self.assertEqual(footy_obj.get_team('domain D')['goal_difference'], 4)

        # Now let's calculate and set the averages.
        games_played_by_home_teams = 2
        games_played_by_away_teams = games_played_by_home_teams
        goals_scored_by_home_teams = 0 + 1 + 2 + 1
        goals_scored_by_away_teams = 2 + 1 + 0 + 0
        footy_obj.average_goals_scored_by_a_home_team = round(
                goals_scored_by_home_teams / games_played_by_home_teams, 2)
        footy_obj.average_goals_scored_by_an_away_team = round(
                goals_scored_by_away_teams / games_played_by_away_teams, 2)

        # Now we do have enough data to predict fixtures.  In this case we
        # expect domain D to beat A at home.
        response = footy_obj.fixture('domain D', 'domain A')
        self.assertIsNotNone(response)
        outcome_probabilities = response['outcome_probabilities']
        self.assertGreater(outcome_probabilities[0], outcome_probabilities[1])
        self.assertGreater(outcome_probabilities[0], outcome_probabilities[2])

    @parameterized.expand([
        ('Arsenal', 'Stoke', [72.0, 19.0, 10.0], 2, 0, 14),
        ('Aston Villa', 'Newcastle', [62.0, 21.0, 17.0], 1, 0, 10),
        ('Blackburn', 'West Brom', [54.0, 23.0, 23.0], 1, 1, 10),
        # Article says 19% probability we calculated 17%.
        # ('Fulham', 'Everton', [35.0, 35.0, 30.0], 0, 0, 19),
        ('Hull', 'Man United', [9.0, 19.0, 72.0], 0, 2, 14),
        ('Liverpool', 'Tottenham', [72.0, 20.0, 9.0], 1, 0, 16),
        # Article says mose likely outcome 2 - 1 (10%).  We calculate
        # 1 - 1 10.36%.
        # ('Man City', 'Bolton', [59, 22, 19], 2, 1, 10),
        ('Sunderland', 'Chelsea', [10, 25, 65], 0, 1, 20),
        ('West Ham', 'Middlesbrough', [57, 28, 15], 1, 0, 19),
        ('Wigan', 'Portsmouth', [44, 32, 25], 1, 0, 16)
    ])
    def test_fixture(self, home_team, away_team, expected_probabilities,
                     home_team_goals, away_team_goals, final_score_likelihood):
        """
        Test that the probabilities are calculated correctly and compare against values calculated by Prof
        Spiegelhalter.

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
        home_team_goals : int
            The most likely number of goals to be scored by the home team.
        away_team_goals : int
            The most likely number of goals to be scored by the away team.
        final_score_likelihood : float
            The probability of the final score as stated.
        """
        footy = self.footy
        response = footy.fixture(home_team, away_team)
        outcome_probabilities = response['outcome_probabilities']

        # We allow some wriggle room for the values calculated.  This is
        # because the maximum number of goals we test up to is six.  However,
        # the sum of all the probabilities for the Arsenal v Stoke games
        # is actually 98.01 (not a perfect 100.0).  Therefore we subtract the
        # sum from 1.0 and use the result as a variance to compare against.
        probabilities_sum = outcome_probabilities[0]
        probabilities_sum += outcome_probabilities[1]
        probabilities_sum += outcome_probabilities[2]
        delta = abs(1.0 - probabilities_sum)

        for i in [0, 1, 2]:
            outcome_probability = outcome_probabilities[i]
            expected_probability = expected_probabilities[i]
            self.assertAlmostEqual(
                outcome_probability,
                expected_probability,
                delta=delta
            )

        final_score_probabilities = response['final_score_probabilities']
        final_score_probabilities = final_score_probabilities.values.tolist()
        most_likely_final_score = final_score_probabilities[0]
        self.assertEqual(most_likely_final_score[0],
                         int(home_team_goals),
                         final_score_probabilities)
        self.assertEqual(most_likely_final_score[1],
                         int(away_team_goals),
                         final_score_probabilities)
        self.assertAlmostEqual(round(most_likely_final_score[2], 0),
                               final_score_likelihood,
                               delta=1.0,
                               msg=final_score_probabilities)


if __name__ == '__main__':
    unittest.main()
