import unittest

from footy.domain.Result import Result


class TestResult(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.STATUS = 'COMPLETE'
        cls.HOME_TEAM_GOALS_SCORED = 2
        cls.AWAY_TEAM_GOALS_SCORED = 1

    def test_result_initializes_with_expected_values(self):
        result = Result(self.STATUS, self.HOME_TEAM_GOALS_SCORED, self.AWAY_TEAM_GOALS_SCORED)
        self.assertEqual(self.STATUS, result.status)
        self.assertEqual(self.HOME_TEAM_GOALS_SCORED, result.home_team_goals_scored)
        self.assertEqual(self.AWAY_TEAM_GOALS_SCORED, result.away_team_goals_scored)

    def test_result_initializes_with_expected_defaults(self):
        result = Result()
        self.assertEqual('SCHEDULED', result.status)
        self.assertEqual(0, result.home_team_goals_scored)
        self.assertEqual(0, result.away_team_goals_scored)

    def test_equality_true_when_result_object_same_values(self):
        result_a = Result(self.STATUS, self.HOME_TEAM_GOALS_SCORED, self.AWAY_TEAM_GOALS_SCORED)
        result_b = Result(self.STATUS, self.HOME_TEAM_GOALS_SCORED, self.AWAY_TEAM_GOALS_SCORED)
        self.assertEqual(result_a, result_b)

    def test_equality_false_when_result_object_different_values(self):
        result_a = Result(self.STATUS, self.HOME_TEAM_GOALS_SCORED, self.AWAY_TEAM_GOALS_SCORED)
        result_b = Result()
        self.assertNotEqual(result_a, result_b)


if __name__ == '__main__':
    unittest.main()
