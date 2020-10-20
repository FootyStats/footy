"""Result - Data structure for a team."""


class Team:
    """Result - Data structure for a team."""

    def __init__(self, team_name, goals_for=0, goals_against=0, home_games=0, away_games=0, points=0):
        """Construct a Team object."""
        self._team_name = team_name
        self._goals_for = goals_for
        self._goals_against = goals_against
        self._home_games = home_games
        self._away_games = away_games
        self._points = points

    def __eq__(self, other):
        """
        Override the __eq__ method for the Team class to allow for object value comparison.

        Parameters
        ----------
        other : footy.domain.Team.Team
            The team object to compare to.

        Returns
        -------
        bool
            True/False if the values in the two objects are equal.
        """
        return (
                self.__class__ == other.__class__ and
                self._team_name == other._team_name and
                self._goals_for == other._goals_for and
                self._goals_against == other._goals_against and
                self._home_games == other._home_games and
                self._away_games == other._away_games and
                self._points == other._points
        )

    @property
    def team_name(self):
        """
        Getter method for property team_name.

        Returns
        -------
        str
            The value of property team_name.
        """
        return self._team_name

    @property
    def goals_for(self):
        """
        Getter method for property goals_for.

        Returns
        -------
        int
            The value of property goals_for.
        """
        return self._goals_for

    @goals_for.setter
    def goals_for(self, goals_for):
        """
        Getter method for property goals_for.

        Parameters
        ----------
        goals_for : int
            The value you wish to set the goals_for property to.
        """
        self._goals_for = goals_for

    @property
    def goals_against(self):
        """
        Getter method for property goals_against.

        Returns
        -------
        int
            The value of property goals_against.
        """
        return self._goals_against

    @goals_against.setter
    def goals_against(self, goals_against):
        """
        Setter method for property goals_against.

        Parameters
        ----------
        goals_against : int
            The value you wish to set the goals_against property to.
        """
        self._goals_against = goals_against

    @property
    def home_games(self):
        """
        Getter method for property home_games.

        Returns
        -------
        int
            The value of property home_games.
        """
        return self._home_games

    @home_games.setter
    def home_games(self, home_games):
        """
        Setter method for property home_games.

        Parameters
        ----------
        home_games : int
            The value you wish to set the home_games property to.
        """
        self._home_games = home_games

    @property
    def away_games(self):
        """
        Getter method for property away_games.

        Returns
        -------
        int
            The value of property away_games.
        """
        return self._away_games

    @away_games.setter
    def away_games(self, away_games):
        """
        Setter method for property away_games.

        Parameters
        ----------
        away_games : int
            The value you wish to set the away_games property to.
        """
        self._away_games = away_games

    @property
    def points(self):
        """
        Getter method for property points.

        Returns
        -------
        int
            The value of property points.
        """
        return self._points

    @points.setter
    def points(self, points):
        """
        Setter method for property points.

        Parameters
        ----------
        points : int
            The value you wish to set the points property to.
        """
        self._points = points

    @property
    def goal_difference(self):
        """
        Calculate and return the goal difference for the team.

        Returns
        -------
        int
            goals_for - goals_against
        """
        return self._goals_for - self._goals_against
