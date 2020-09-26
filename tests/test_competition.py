import json
import unittest

from parameterized import parameterized

from footy import Competition


class MockFootballData:
    def __init__(self, data_file_name):
        full_data_file_name = f'tests/resources/data/{data_file_name}'

        with open(full_data_file_name) as stream:
            matches_data = stream.read()
            matches_data = json.loads(matches_data)
            self.data = {
                'matches': matches_data
            }

    def get_info(self, info_name):
        return self.data[info_name]


class TestCompetitionClassFromSnapshots(unittest.TestCase):

    @parameterized.expand([
        (
            'PL-2020-07-27.json',
            20
        )
    ])
    def test_mocked_data(self,
                         data_file_name,
                         team_count):
        football_data_api = MockFootballData(data_file_name)
        comp_obj = Competition(football_data_api)
        df = comp_obj.table()
        self.assertEquals(len(df), team_count)
