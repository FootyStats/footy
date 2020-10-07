import unittest

from footy.domain.Fixture import Fixture
from footy.domain.Result import Result
from footy.domain.Team import Team


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.HOME_TEAM = Team('Arsenal', 64, 36, 18, 19, 69)
        cls.AWAY_TEAM = Team('Stoke', 37, 51, 19, 18, 45)
        cls.STATUS = "SCHEDULED"
        cls.UTC_START = '2021-02-13T21:30:00Z'
        cls.RESULT = Result()

    def test_fixture_initializes_with_expected_values(self):
        fixture = Fixture(self.HOME_TEAM, self.AWAY_TEAM, self.STATUS, self.UTC_START, self.RESULT)
        self.assertEqual(self.HOME_TEAM, fixture.home_team)
        self.assertEqual(self.AWAY_TEAM, fixture.away_team)
        self.assertEqual(self.STATUS, fixture.status)
        self.assertEqual(self.UTC_START, fixture.utc_start)
        self.assertEqual(self.RESULT, fixture.result)

    def test_fixture_initializes_with_expected_defaults(self):
        fixture = Fixture(self.HOME_TEAM, self.AWAY_TEAM)
        self.assertEqual(self.HOME_TEAM, fixture.home_team)
        self.assertEqual(self.AWAY_TEAM, fixture.away_team)
        self.assertEqual('SCHEDULED', fixture.status)
        self.assertEqual('', fixture.utc_start)
        self.assertEqual(Result(), fixture.result)


if __name__ == '__main__':
    unittest.main()
