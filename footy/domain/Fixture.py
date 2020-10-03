from footy.footy.domain import Result
from footy.footy.domain.Team import Team


class Fixture:

    def __init__(self):
        self._status = ''
        self._home_team = Team
        self._away_team = Team
        self._utc_start = '2020-10-03T14:41:38Z'
        self._result = Result
