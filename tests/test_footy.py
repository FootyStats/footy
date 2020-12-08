import numpy as np
import unittest

from parameterized import parameterized

from footy import Footy
from footy.domain.Team import Team


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

    def footy_under_test_producer(self):
        footy = Footy()

        footy.add_team(Team('Arsenal', 64, 36, 18, 19, 69))
        footy.add_team(Team('Aston Villa', 53, 48, 18, 19, 59))
        footy.add_team(Team('Blackburn', 40, 60, 18, 19, 40))
        footy.add_team(Team('Bolton', 41, 52, 19, 18, 41))
        footy.add_team(Team('Chelsea', 65, 22, 19, 18, 80))
        footy.add_team(Team('Everton', 53, 37, 19, 18, 60))
        footy.add_team(Team('Fulham', 39, 32, 18, 19, 53))
        footy.add_team(Team('Hull', 39, 63, 18, 19, 35))
        footy.add_team(Team('Liverpool', 74, 26, 18, 19, 83))
        footy.add_team(Team('Man City', 57, 50, 18, 19, 47))
        footy.add_team(Team('Man United', 67, 24, 19, 18, 87))
        footy.add_team(Team('Middlesbrough', 27, 55, 19, 18, 32))
        footy.add_team(Team('Newcastle', 40, 58, 19, 18, 34))
        footy.add_team(Team('Portsmouth', 38, 56, 19, 18, 41))
        footy.add_team(Team('Stoke', 37, 51, 19, 18, 45))
        footy.add_team(Team('Sunderland', 32, 51, 18, 19, 36))
        footy.add_team(Team('Tottenham', 44, 42, 19, 18, 51))
        footy.add_team(Team('West Brom', 36, 67, 19, 18, 31))
        footy.add_team(Team('West Ham', 40, 44, 18, 19, 48))
        footy.add_team(Team('Wigan', 33, 45, 18, 19, 42))
        footy.average_goals_scored_by_a_home_team(1.36)
        footy.average_goals_scored_by_an_away_team(1.06)

        return footy

    @parameterized.expand([
        ([1, 0, 0], [100.0, 0.0, 0.0], 0.0),
        ([0, 1, 0], [100.0, 0.0, 0.0], 2.0),
        ([0, 0, 1], [100.0, 0.0, 0.0], 2.0),
        ([1, 0, 0], [70.02, 18.43, 9.56], 0.13),
        ([0, 1, 0], [70.02, 18.43, 9.56], 1.16),
        ([0, 0, 1], [70.02, 18.43, 9.56], 1.34)
    ])
    def test_brier_score(self, y_true, y_prob, expected_answer):
        footy = self.footy_under_test_producer()
        y_true = np.array(y_true) / 100.0
        y_prob = np.array(y_prob) / 100.0
        bs = footy.brier_score(y_true, y_prob)
        self.assertEqual(bs, expected_answer)

    def test_dummy_league(self):
        """Test a dummy league through various stages of progression."""
        footy_obj = Footy()

        # The league has not yet started so zero values (the default).
        team_a = Team('Team A')
        team_b = Team('Team B')
        team_c = Team('Team C')
        team_d = Team('Team D')

        for team in [team_a, team_b, team_c, team_d]:
            footy_obj.add_team(team)

        footy_obj.average_goals_scored_by_a_home_team(0)
        footy_obj.average_goals_scored_by_an_away_team(0)

        # Our micro league should contain four teams.
        self.assertEqual(len(footy_obj.get_team_names()), 4)

        # No games played, so we don't expect any probability data to
        # be available.
        response = footy_obj.fixture(team_a, team_b)
        self.assertIsNone(response.outcome_probabilities())

        # Team D beats A 2 - 0 away.
        footy_obj.add_team(Team('Team A', 0, 2, 1, 0, 0))
        footy_obj.add_team(Team('Team D', 2, 0, 0, 1, 3))

        # Team B plays Team C at home and the final score is a
        # 1 - 1 score draw.
        footy_obj.add_team(Team('Team B', 1, 1, 1, 0, 1))
        footy_obj.add_team(Team('Team C', 1, 1, 0, 1, 1))

        # Teams D and C played away and between them scored three
        # goals.  Set the average for these two games.
        footy_obj.average_goals_scored_by_an_away_team(round(3 / 2, 2))

        # Teams A and B played at home but only team B scored a single goal.
        # Set the average for these two games.
        footy_obj.average_goals_scored_by_a_home_team(round(1 / 2, 2))

        # At this point, teams D and C have not played at home and teams
        # B and A have not played away.  Therefore still expecting not
        # to have enough data to track probabilities.
        response = footy_obj.fixture(footy_obj.get_team('Team A'), footy_obj.get_team('Team B'))
        self.assertIsNone(response.outcome_probabilities())

        # Team D hosts B and beats them 2 - 0.
        goals_for = footy_obj.get_team('Team B').goals_for()
        goals_against = footy_obj.get_team('Team B').goals_against() + 2
        home_games = 1
        away_games = 1
        points = 1 + 0
        footy_obj.add_team(Team('Team B', goals_for, goals_against, home_games,
                           away_games, points))

        goals_for = footy_obj.get_team('Team D').goals_for() + 2
        goals_against = footy_obj.get_team('Team D').goals_against() + 0
        points = 3 + 3
        footy_obj.add_team(Team('Team D', goals_for, goals_against, home_games,
                           away_games, points))

        # Team C hosts Team A and beats them 1 - 0.
        goals_for = footy_obj.get_team('Team A').goals_for() + 0
        goals_against = footy_obj.get_team('Team B').goals_against() + 1
        home_games = 1
        away_games = 1
        points = 0 + 0
        footy_obj.add_team(Team('Team A', goals_for, goals_against, home_games,
                           away_games, points))

        goals_for = footy_obj.get_team('Team C').goals_for() + 1
        goals_against = footy_obj.get_team('Team D').goals_against() + 0
        points = 1 + 3
        footy_obj.add_team(Team('Team C', goals_for, goals_against, home_games,
                           away_games, points))

        # Now all teams have played one home game and one away game.  A recap
        # of the table at the moment:
        #
        # Team GF GA GD PTS Form
        # D    4  0   4   6 WW
        # C    2  0   2   4 DW
        # B    1  3  -2   1 DL
        # A    0  4  -4   0 LL

        # Let's confirm the goal differences.
        self.assertEqual(footy_obj.get_team('Team A').goal_difference(), -4)
        self.assertEqual(footy_obj.get_team('Team B').goal_difference(), -2)
        self.assertEqual(footy_obj.get_team('Team C').goal_difference(), 2)
        self.assertEqual(footy_obj.get_team('Team D').goal_difference(), 4)

        # Now let's calculate and set the averages.
        games_played_by_home_teams = 2
        games_played_by_away_teams = games_played_by_home_teams
        goals_scored_by_home_teams = 0 + 1 + 2 + 1
        goals_scored_by_away_teams = 2 + 1 + 0 + 0
        footy_obj.average_goals_scored_by_a_home_team(
            round(
                goals_scored_by_home_teams / games_played_by_home_teams,
                2
            )
        )
        footy_obj.average_goals_scored_by_an_away_team(
            round(
                goals_scored_by_away_teams / games_played_by_away_teams,
                2
            )
        )

        # Now we do have enough data to predict fixtures.  In this case we
        # expect Team D to beat A at home.
        response = footy_obj.fixture(footy_obj.get_team('Team D'), footy_obj.get_team('Team A'))
        self.assertIsNotNone(response.outcome_probabilities())
        outcome_probabilities = response.outcome_probabilities()
        self.assertGreater(outcome_probabilities[0], outcome_probabilities[1])
        self.assertGreater(outcome_probabilities[0], outcome_probabilities[2])


if __name__ == '__main__':
    unittest.main()
