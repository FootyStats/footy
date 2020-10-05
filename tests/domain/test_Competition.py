import unittest

from footy.domain.Competition import Competition
from footy.domain.Team import Team


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.CODE = 'Test'
        cls.NAME = 'Test League'
        cls.TEAMS = [Team('Arsenal', 64, 36, 18, 19, 69),
                     Team('Stoke', 37, 51, 19, 18, 45)]
        cls.START_DATE = '2020-09-25T15:00:00Z'
        cls.END_DATE = '2021-02-13T21:30:00Z'
        cls.STAGE = 'Group'
        cls.FIXTURES = []

    def competition_under_test_producer(self):
        return Competition(self.CODE, self.NAME, self.TEAMS, self.START_DATE, self.END_DATE,
                           self.STAGE, self.FIXTURES)

    def test_competition_initializes_with_expected_values(self):
        competition = Competition(self.CODE, self.NAME, self.TEAMS, self.START_DATE, self.END_DATE,
                                  self.STAGE, self.FIXTURES)
        self.assertEqual(self.CODE, competition.code)
        self.assertEqual(self.NAME, competition.name)
        self.assertEqual(self.TEAMS, competition.teams)
        self.assertEqual(self.START_DATE, competition.start_date)
        self.assertEqual(self.END_DATE, competition.end_date)
        self.assertEqual(self.STAGE, competition.stage)
        self.assertEqual(self.FIXTURES, competition.fixtures)

    def test_add_team_returns_new_team(self):
        team = Team('A', 1, 2, 3, 4, 5)
        competition = self.competition_under_test_producer()
        competition.add_team(team)
        self.assertTrue(team in competition.teams)

    def test_add_team_only_adds_once(self):
        team = Team('A', 1, 2, 3, 4, 5)
        competition = self.competition_under_test_producer()
        num_teams = len(competition.teams)

        competition.add_team(team)
        competition.add_team(team)

        self.assertTrue(team in competition.teams)
        self.assertEqual(num_teams + 1, len(competition.teams))


if __name__ == '__main__':
    unittest.main()
