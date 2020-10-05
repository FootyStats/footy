"""Fixture - Data structure for a fixture."""

from footy.domain import Result
from footy.domain import Team


class Fixture:
    """Fixture - Data structure for a fixture."""

    def __init__(self):
        """Construct a Fixture object."""
        self._status = ''
        self._home_team = Team
        self._away_team = Team
        self._utc_start = '2020-10-03T14:41:38Z'
        self._result = Result
