"""Result - Data structure for a team."""


class Team:
    """Result - Data structure for a team."""

    def __init__(self):
        """Construct a Team object."""
        self.__team_name = ''
        self._goals_for = 0
        self._goals_against = 0
        self._home_games = 0
        self._away_games = 0
        self._points = 0
