import unittest

from footy.domain.Team import Team


class TestTeam(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.__TEAM_NAME = 'Everton'
        cls.__GOALS_FOR = 53
        cls.__GOALS_AGAINST = 37
        cls.__HOME_GAMES = 19
        cls.__AWAY_GAMES = 18
        cls.__POINTS = 60
        cls.__GOAL_DIFFERENCE = 16

    def test_team_initializes_with_expected_values(self):
        team = Team(self.__TEAM_NAME, self.__GOALS_FOR, self.__GOALS_AGAINST,
                    self.__HOME_GAMES, self.__AWAY_GAMES, self.__POINTS)

        self.assertEqual(team.team_name, self.__TEAM_NAME)
        self.assertEqual(team.goals_for, self.__GOALS_FOR)
        self.assertEqual(team.goals_against, self.__GOALS_AGAINST)
        self.assertEqual(team.home_games, self.__HOME_GAMES)
        self.assertEqual(team.away_games, self.__AWAY_GAMES)
        self.assertEqual(team.points, self.__POINTS)

    def test_goal_difference_calculates_correctly(self):
        team = Team(self.__TEAM_NAME, self.__GOALS_FOR, self.__GOALS_AGAINST,
                    self.__HOME_GAMES, self.__AWAY_GAMES, self.__POINTS)
        self.assertEqual(team.goal_difference, self.__GOAL_DIFFERENCE)

    def test_goal_difference_updates_when_goals_for_change(self):
        team = Team(self.__TEAM_NAME, self.__GOALS_FOR, self.__GOALS_AGAINST,
                    self.__HOME_GAMES, self.__AWAY_GAMES, self.__POINTS)
        self.assertEqual(team.goal_difference, self.__GOAL_DIFFERENCE)

        team.goals_for += 10
        self.assertEqual(team.goal_difference, self.__GOAL_DIFFERENCE + 10)

    def test_goal_difference_updates_when_goals_against_change(self):
        team = Team(self.__TEAM_NAME, self.__GOALS_FOR, self.__GOALS_AGAINST,
                    self.__HOME_GAMES, self.__AWAY_GAMES, self.__POINTS)
        self.assertEqual(team.goal_difference, self.__GOAL_DIFFERENCE)

        team.goals_against += 10
        self.assertEqual(team.goal_difference, self.__GOAL_DIFFERENCE - 10)

if __name__ == '__main__':
    unittest.main()
