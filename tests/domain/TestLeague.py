import unittest

from footy.domain.League import League
from footy.domain.Team import Team


class TestLeague(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.__LEAGUE_NAME = 'Test League'
        cls.__TEAMS = {'Arsenal': Team('Arsenal', 64, 36, 18, 19, 69),
                       'Stoke': Team('Stoke', 37, 51, 19, 18, 45)}

        cls.__AVERAGE_GOALS_SCORED_BY_A_HOME_TEAM = 1.36
        cls.__AVERAGE_GOALS_SCORED_BY_AN_AWAY_TEAM = 1.06

    def league_under_test_producer(self):
        return League(self.__LEAGUE_NAME, self.__TEAMS, self.__AVERAGE_GOALS_SCORED_BY_A_HOME_TEAM,
                      self.__AVERAGE_GOALS_SCORED_BY_AN_AWAY_TEAM)

    def test_league_initializes_with_expected_values(self):
        league = League(self.__LEAGUE_NAME, self.__TEAMS, self.__AVERAGE_GOALS_SCORED_BY_A_HOME_TEAM,
                        self.__AVERAGE_GOALS_SCORED_BY_AN_AWAY_TEAM)

        self.assertEqual(league.league_name, self.__LEAGUE_NAME)
        self.assertEqual(league.teams, self.__TEAMS)
        self.assertEqual(league.average_goals_scored_by_a_home_team, self.__AVERAGE_GOALS_SCORED_BY_A_HOME_TEAM)
        self.assertEqual(league.average_goals_scored_by_an_away_team, self.__AVERAGE_GOALS_SCORED_BY_AN_AWAY_TEAM)

    def test_replacing_teams(self):
        teams = {'A': Team('A', 1, 2, 3, 4, 5)}
        league = self.league_under_test_producer()
        league.teams = teams

        self.assertEqual(league.teams, teams)

    def test_goals_conceded_for_team(self):
        team = 'Arsenal'
        league = self.league_under_test_producer()
        result = league.goals_conceded(team)

        self.assertEqual(result, self.__TEAMS[team].goals_against)

    def test_goals_conceded_for_league(self):
        league = self.league_under_test_producer()
        result = league.goals_conceded()
        expected = int(round(sum(team.goals_against for team in self.__TEAMS.values()) / len(self.__TEAMS.keys())))

        self.assertEqual(expected, result)

    def test_goals_scored_for_team(self):
        team = 'Arsenal'
        league = self.league_under_test_producer()
        result = league.goals_scored(team)

        self.assertEqual(result, self.__TEAMS[team].goals_for)

    def test_goals_conceded_goals_scored_for_league(self):
        league = self.league_under_test_producer()
        result = league.goals_scored()
        expected = int(round(sum(team.goals_for for team in self.__TEAMS.values()) / len(self.__TEAMS.keys())))

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
