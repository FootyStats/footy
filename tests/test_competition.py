import bz2
import json
import unittest

from parameterized import parameterized

from footy.competition import Competition


class MockFootballData:
    def __init__(self, data_set_name):
        data_file_name = f'tests/resources/data/{data_set_name}.json.bz2'

        with bz2.open(data_file_name) as stream:
            matches_data = json.loads(stream.read())
            self.data = {
                'matches': matches_data
            }

    def get_info(self, info_name):
        return self.data[info_name]


class TestCompetitionClassFromSnapshots(unittest.TestCase):

    @parameterized.expand([
        (
            'PL-2020-07-27', 7, 0, 0, 0
        ),
        (
            'PL-2020-09-25', 2, 2, 4, 6
        )
    ])
    def test_mocked_data_against_everton(self,
                                         data_set_name,
                                         expected_position,
                                         expected_games_played,
                                         expected_goal_difference,
                                         expected_points
                                         ):
        """
        Check the position and stats of Everton FC.

        This isn't just because one of the authors supports Everton!  The PL-2020-09-25
        dataset needs the league positions to be sorted correctly and Everton at that time
        had the same number of points as 5 over teams and in the case of Arsenal, the same
        goal difference.  This is to prove that the league position is applied correctly
        (and yes, Everton were 2nd after gaining maximum points from their games).

        Parameters
        ----------
        data_set_name
        expected_position
        expected_games_played
        expected_goal_difference
        expected_points
        """
        team_name = 'Everton FC'
        football_data_api = MockFootballData(data_set_name)
        comp_obj = Competition(football_data_api)
        model_data = comp_obj.get_model_data()
        df = model_data['table']
        team_data = model_data['teams'][team_name]

        home_games = team_data['home_games']
        away_games = team_data['away_games']
        games_played = home_games + away_games
        self.assertEqual(games_played, expected_games_played, 'Incorrect Number of Games Played')

        goal_difference = team_data['goal_difference']
        self.assertEqual(goal_difference, expected_goal_difference)

        points = team_data['points']
        self.assertEqual(points, expected_points)

        # Find which row in the data table Everton is and increment by one to get
        # the league position.
        position = df[df['team_name'] == team_name].index[0] + 1
        self.assertEqual(position, expected_position)

    @parameterized.expand([
        ('PL-2020-07-27', False),
        ('PL-2020-09-25', False),
        ('BSA-2020-09-26', True)
    ])
    def test_mocked_data_fixtures(self, data_set_name, expecting_predictions_in_fixtures):
        football_data_api = MockFootballData(data_set_name)
        comp_obj = Competition(football_data_api)
        model_data = comp_obj.get_model_data()
        upcoming_fixtures = model_data['upcoming_fixtures']

        for fixture in upcoming_fixtures:
            if not expecting_predictions_in_fixtures:
                self.assertNotIn('final_score_probabilities', fixture)
                continue

            self.assertIn('final_score_probabilities', fixture)
