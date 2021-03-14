import unittest

from footy.domain.Competition import Competition
from footy.domain.Fixture import Fixture
from footy.domain.Team import Team


class TestCompetition(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # only use for assertions and when the values of competition will not change
        cls.EXPECTED_COMPETITION = Competition('Test', 'Test Competition', [Team('Arsenal', 64, 36, 18, 19, 69),
                                                                            Team('Stoke', 37, 51, 19, 18, 45)],
                                               '2020-09-25T15:00:00Z', '2021-02-13T21:30:00Z', 'Group', [])

    def competition_under_test_producer(self):
        return Competition('Test', 'Test Competition', [Team('Arsenal', 64, 36, 18, 19, 69),
                                                        Team('Stoke', 37, 51, 19, 18, 45)],
                           '2020-09-25T15:00:00Z', '2021-02-13T21:30:00Z', 'Group', [])

    def test_competition_initializes_with_expected_values(self):
        competition = Competition(self.EXPECTED_COMPETITION.code(), self.EXPECTED_COMPETITION.name,
                                  self.EXPECTED_COMPETITION.teams, self.EXPECTED_COMPETITION.start_date,
                                  self.EXPECTED_COMPETITION.end_date, self.EXPECTED_COMPETITION.stage,
                                  self.EXPECTED_COMPETITION.fixtures)
        self.assertEqual(self.EXPECTED_COMPETITION.code(), competition.code())
        self.assertEqual(self.EXPECTED_COMPETITION.name, competition.name)
        self.assertEqual(self.EXPECTED_COMPETITION.teams, competition.teams)
        self.assertEqual(self.EXPECTED_COMPETITION.start_date, competition.start_date)
        self.assertEqual(self.EXPECTED_COMPETITION.end_date, competition.end_date)
        self.assertEqual(self.EXPECTED_COMPETITION.stage, competition.stage)
        self.assertEqual(self.EXPECTED_COMPETITION.fixtures, competition.fixtures)

    def test_add_team_adds_new_team(self):
        team = Team('A', 1, 2, 3, 4, 5)
        competition = self.competition_under_test_producer()
        competition.add_team(team)
        self.assertTrue(team in competition.teams)

    def test_add_team_does_not_add_duplicates(self):
        team = Team('A', 1, 2, 3, 4, 5)
        competition = self.competition_under_test_producer()
        num_teams = len(competition.teams)

        competition.add_team(team)
        competition.add_team(team)

        self.assertTrue(team in competition.teams)
        self.assertEqual(num_teams + 1, len(competition.teams))

    def test_add_fixture_adds_new_fixture(self):
        competition = self.competition_under_test_producer()
        fixture = Fixture(self.EXPECTED_COMPETITION.teams[0], self.EXPECTED_COMPETITION.teams[1])

        self.assertTrue(fixture not in competition.fixtures)

        competition.add_fixture(fixture)
        self.assertTrue(fixture in competition.fixtures)

    def test_add_fixture_does_not_add_duplicates(self):
        competition = self.competition_under_test_producer()
        fixture = Fixture(self.EXPECTED_COMPETITION.teams[0], self.EXPECTED_COMPETITION.teams[1])

        self.assertTrue(fixture not in competition.fixtures)

        competition.add_fixture(fixture)
        competition.add_fixture(fixture)

        self.assertEqual(1, len(competition.fixtures))
        self.assertTrue(fixture in competition.fixtures)


if __name__ == '__main__':
    unittest.main()
