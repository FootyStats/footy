"""Competition - Data structure for a competition/league."""


class Competition:
    """Competition - Data structure for a competition/league."""

    def __init__(self):
        """Construct a Competition object."""
        self._code = ''
        self._name = ''
        self._teams = []
        self._start_date = '2020-10-03T14:41:38Z'
        self._end_date = '2020-10-03T14:41:38Z'
        self._stage = ''
        self._fixtures = []
