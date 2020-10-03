import unittest

from footy.footy.domain.Team import Team


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.TEAM_NAME = 'Everton'
        cls.GOALS_FOR = 53
        cls.GOALS_AGAINST = 37
        cls.HOME_GAMES = 19
        cls.AWAY_GAMES = 18
        cls.POINTS = 60

    def test_team_initializes_with_expected_values(self):
        team = Team(self.TEAM_NAME, self.GOALS_FOR, self.GOALS_AGAINST,
                    self.HOME_GAMES, self.AWAY_GAMES, self.POINTS)

        self.assertEqual(self.TEAM_NAME, team.team_name)
        self.assertEqual(self.GOALS_FOR, team.goals_for)
        self.assertEqual(self.GOALS_AGAINST, team.goals_against)
        self.assertEqual(self.HOME_GAMES, team.home_games)
        self.assertEqual(self.AWAY_GAMES, team.away_games)
        self.assertEqual(self.POINTS, team.points)

    def test_goal_difference_calculates_correctly(self):
        team = Team(self.TEAM_NAME, self.GOALS_FOR, self.GOALS_AGAINST,
                    self.HOME_GAMES, self.AWAY_GAMES, self.POINTS)
        self.assertEqual(self.GOALS_FOR - self.GOALS_AGAINST, team.goal_difference)

    def test_goal_difference_updates_when_goals_for_change(self):
        team = Team(self.TEAM_NAME, self.GOALS_FOR, self.GOALS_AGAINST,
                    self.HOME_GAMES, self.AWAY_GAMES, self.POINTS)
        self.assertEqual(self.GOALS_FOR - self.GOALS_AGAINST, team.goal_difference)

        team.goals_for += 10
        self.assertEqual((self.GOALS_FOR - self.GOALS_AGAINST) + 10, team.goal_difference)

    def test_goal_difference_updates_when_goals_against_change(self):
        team = Team(self.TEAM_NAME, self.GOALS_FOR, self.GOALS_AGAINST,
                    self.HOME_GAMES, self.AWAY_GAMES, self.POINTS)
        self.assertEqual(self.GOALS_FOR - self.GOALS_AGAINST, team.goal_difference)

        team.goals_against += 10
        self.assertEqual((self.GOALS_FOR - self.GOALS_AGAINST) - 10, team.goal_difference)


if __name__ == '__main__':
    unittest.main()
