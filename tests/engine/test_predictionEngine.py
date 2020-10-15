import unittest

from footy.domain.Competition import Competition
from footy.domain.Team import Team


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Competition
        cls.CODE = 'Test'
        cls.NAME = 'Test League'
        cls.TEAMS = [Team('Arsenal', 64, 36, 18, 19, 69),
                     Team('Stoke', 37, 51, 19, 18, 45)]
        cls.START_DATE = '2020-09-25T15:00:00Z'
        cls.END_DATE = '2021-02-13T21:30:00Z'
        cls.STAGE = 'Group'
        cls.FIXTURES = []

        # Fixture
        cls.HOME_TEAM = 'Arsenal'
        cls.AWAY_TEAM = 'Stoke'
        cls.STATUS = "SCHEDULED"
        cls.UTC_START = '2020-10-13T21:30:00Z'

    def competition_under_test_producer(self):
        return Competition(self.CODE, self.NAME, self.TEAMS, self.START_DATE, self.END_DATE,
                           self.STAGE, self.FIXTURES)

    def predict_fixture_results_returns_with_enriched_results(self):
        competition = self.competition_under_test_producer()


if __name__ == '__main__':
    unittest.main()