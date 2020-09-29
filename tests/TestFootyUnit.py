import unittest
import numpy as np

from parameterized import parameterized

from footy import Footy, MissingDataException
from footy.domain.Team import Team


class TestFootyUnit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.HOME_TEAM = 'Arsenal'
        cls.AWAY_TEAM = 'Stoke'
        cls.AVERAGE_GOALS_SCORED_BY_A_HOME_TEAM = 2
        cls.AVERAGE_GOALS_SCORED_BY_AN_AWAY_TEAM = 1

        cls.TEAMS = {'Everton': {'goals_for': 53,
                                 'goals_against': 37,
                                 'home_games': 19,
                                 'away_games': 18,
                                 'goal_difference': 16,
                                 'points': 60},
                     'Arsenal': {'goals_for': 64,
                                 'goals_against': 36,
                                 'home_games': 18,
                                 'away_games': 19,
                                 'goal_difference': 28,
                                 'points': 69},
                     'Stoke': {'goals_for': 37,
                               'goals_against': 51,
                               'home_games': 19,
                               'away_games': 18,
                               'goal_difference': -14,
                               'points': 45}}

        cls.EVERTON_STR_OBJ = 'Team(_Team__team_name=Everton, _goals_for=53, _goals_against=37, _home_games=19,' \
                              ' _away_games=18, _points=60)'

    def add_team_to_footy(self, team_name, footy=None):
        # helper method to add team by name from constants
        if footy is None:
            footy = Footy()

        footy.add_team(Team(team_name,
                       self.TEAMS[team_name]['goals_for'],
                       self.TEAMS[team_name]['goals_against'],
                       self.TEAMS[team_name]['home_games'],
                       self.TEAMS[team_name]['away_games'],
                       self.TEAMS[team_name]['points']))

        return footy

    def footy_under_test_producer(self):
        # helper method to produce footy under test with required
        footy = Footy()

        footy.average_goals_scored_by_a_home_team = self.AVERAGE_GOALS_SCORED_BY_A_HOME_TEAM
        footy.average_goals_scored_by_an_away_team = self.AVERAGE_GOALS_SCORED_BY_AN_AWAY_TEAM
        footy = self.add_team_to_footy(self.HOME_TEAM, footy)
        footy = self.add_team_to_footy(self.AWAY_TEAM, footy)

        return footy

    def test_returns_average_goals_scored_by_home_team(self):
        footy = Footy()
        self.assertNotEqual(footy.average_goals_scored_by_a_home_team, self.AVERAGE_GOALS_SCORED_BY_A_HOME_TEAM)
        footy.average_goals_scored_by_a_home_team = self.AVERAGE_GOALS_SCORED_BY_A_HOME_TEAM
        self.assertEqual(footy.average_goals_scored_by_a_home_team, self.AVERAGE_GOALS_SCORED_BY_A_HOME_TEAM)

    def test_returns_average_goals_scored_by_away_team(self):
        footy = Footy()
        self.assertNotEqual(footy.average_goals_scored_by_an_away_team, self.AVERAGE_GOALS_SCORED_BY_AN_AWAY_TEAM)
        footy.average_goals_scored_by_an_away_team = self.AVERAGE_GOALS_SCORED_BY_AN_AWAY_TEAM
        self.assertEqual(footy.average_goals_scored_by_an_away_team, self.AVERAGE_GOALS_SCORED_BY_AN_AWAY_TEAM)

    def test_returns_team_when_added_by_team(self):
        team_name = 'Everton'
        footy = Footy()

        footy.add_team(team_name,
                       self.TEAMS[team_name]['goals_for'],
                       self.TEAMS[team_name]['goals_against'],
                       self.TEAMS[team_name]['home_games'],
                       self.TEAMS[team_name]['away_games'],
                       self.TEAMS[team_name]['points']
                       )
        response_team = footy.get_team(team_name)
        response_teams = footy.get_teams()

        self.assertEqual(self.EVERTON_STR_OBJ, str(response_team))
        self.assertTrue(response_teams.__contains__(team_name))

    def test_returns_team_when_added_by_data(self):
        team_name = 'Everton'
        footy = Footy()

        team = Team(team_name,
                    self.TEAMS[team_name]['goals_for'],
                    self.TEAMS[team_name]['goals_against'],
                    self.TEAMS[team_name]['home_games'],
                    self.TEAMS[team_name]['away_games'],
                    self.TEAMS[team_name]['points'])
        footy.add_team(team)

        response_team = footy.get_team(team_name)
        response_teams = footy.get_teams()

        self.assertEqual(self.EVERTON_STR_OBJ, str(response_team))
        self.assertTrue(response_teams.__contains__(team_name))

    @parameterized.expand([
        ([1, 0, 0], [100.0, 0.0, 0.0], 0.0),
        ([0, 1, 0], [100.0, 0.0, 0.0], 2.0),
        ([0, 0, 1], [100.0, 0.0, 0.0], 2.0),
        ([1, 0, 0], [70.02, 18.43, 9.56], 0.13),
        ([0, 1, 0], [70.02, 18.43, 9.56], 1.16),
        ([0, 0, 1], [70.02, 18.43, 9.56], 1.34)
    ])
    def test_brier_score(self, outcome, probability, expected_answer):
        # [win, draw, loss]
        footy = self.footy_under_test_producer()
        outcome = np.array(outcome) / 100.0
        probability = np.array(probability) / 100.0
        bs = footy.brier_score(outcome, probability)
        self.assertEqual(bs, expected_answer)

    def test_fixture_returns_throws_missingdataexception_when_avg_goals_not_set(self):
        # Parameterized does not allow None input, so defining in test. This test (and assertion) needs to be cleaned up
        cases = [None, None], [1, None], [None, 1]

        for case in cases:
            footy = Footy()
            footy = self.add_team_to_footy(self.HOME_TEAM, footy)
            footy = self.add_team_to_footy(self.AWAY_TEAM, footy)

            footy.average_goals_scored_by_a_home_team = case[0]
            footy.average_goals_scored_by_an_away_team = case[1]

            try:
                response = footy.fixture(self.HOME_TEAM, self.AWAY_TEAM)
                # Expected Exception not returned
                self.assertTrue(False)
            except MissingDataException as e:
                # Expected exception returned
                self.assertTrue(str(e.args[0]).startswith('average_goals_scored_by_'))

    def test_fixture_returns_none_when_no_games_played(self):
        footy = Footy()
        footy.add_team('Team A', 0, 0, 0, 0, 0)
        footy.add_team('Team B', 0, 0, 0, 0, 0)

        result = footy.fixture('Team A', 'Team B')

        self.assertIsNone(result)

    def test_fixture(self):
        footy = self.footy_under_test_producer()
        expected_probabilities = [81.13, 10.39, 4.51]
        home_team_goals = 2
        away_team_goals = 0
        final_score_likelihood = 12
        result = footy.fixture(self.HOME_TEAM, self.AWAY_TEAM)

        outcome_probabilities = result['outcome_probabilities']
        delta = abs(1.0 - sum(outcome_probabilities))

        for i in [0, 1, 2]:
            outcome_probability = outcome_probabilities[i]
            expected_probability = expected_probabilities[i]
            self.assertAlmostEqual(outcome_probability, expected_probability, delta=delta)

        final_score_probabilities = result['final_score_probabilities'].values.tolist()[0]
        self.assertEqual(final_score_probabilities[0], home_team_goals, final_score_probabilities)
        self.assertEqual(int(final_score_probabilities[1]), away_team_goals, final_score_probabilities)
        self.assertAlmostEqual(round(final_score_probabilities[2], 0), final_score_likelihood,
                               delta=1.0, msg=final_score_probabilities)


if __name__ == '__main__':
    unittest.main()
