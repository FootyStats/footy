import unittest

from footy.domain.Result import Result


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.STATUS = 'COMPLETE'
        cls.HOME_TEAM_GOALS_SCORED = 2
        cls.AWAY_TEAM_GOALS_SCORED = 1

    def test_competition_initializes_with_expected_values(self):
        result = Result(self.STATUS, self.HOME_TEAM_GOALS_SCORED, self.AWAY_TEAM_GOALS_SCORED)
        self.assertEqual(self.STATUS, result.status)
        self.assertEqual(self.HOME_TEAM_GOALS_SCORED, result.home_team_goals_scored)
        self.assertEqual(self.AWAY_TEAM_GOALS_SCORED, result.away_team_goals_scored)

    def test_competition_initializes_with_expected_defaults(self):
        result = Result()
        self.assertEqual('SCHEDULED', result.status)
        self.assertEqual(0, result.home_team_goals_scored)
        self.assertEqual(0, result.away_team_goals_scored)


if __name__ == '__main__':
    unittest.main()
