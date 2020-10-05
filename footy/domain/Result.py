"""Result - Data structure for a result."""
# Is prediction before game is played, then actual once game ahs been played
# Return the outcome Briers score, home/away goals scored, Predictions if available, and actual
# result if game has been played


class Result:
    """Result - Data structure for a result."""

    def __init__(self, status='SCHEDULED', home_team_goals_scored=0, away_team_goals_scored=0):
        """
        Construct a Result object.

        Parameters
        ----------
        status : str, optional
            The status of the result of the fixture. SCHEDULED or FINISHED. Defaults to SCHEDULED
        home_team_goals_scored : int, optional
            The number of goals scored by the home team. Defaults to 0.
        away_team_goals_scored : int, optional
            The number of goals scored by the away team. Defaults to 0.
        """
        self._status = status  # TODO: Can we use an enum?
        self._home_team_goals_scored = home_team_goals_scored
        self._away_team_goals_scored = away_team_goals_scored

    @property
    def status(self):
        """
        Getter method for property status.

        Returns
        -------
        str
            The value of property status.
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Getter method for property status.

        Parameters
        ----------
        status : str
            The value you wish to set the status property to.
        """
        self._status = status

    @property
    def home_team_goals_scored(self):
        """
        Getter method for property home_team_goals_scored.

        Returns
        -------
        int
            The value of property home_team_goals_scored.
        """
        return self._home_team_goals_scored

    @home_team_goals_scored.setter
    def home_team_goals_scored(self, home_team_goals_scored):
        """
        Getter method for property home_team_goals_scored.

        Parameters
        ----------
        home_team_goals_scored : int
            The value you wish to set the home_team_goals_scored property to.
        """
        self._home_team_goals_scored = home_team_goals_scored

    @property
    def away_team_goals_scored(self):
        """
        Getter method for property away_team_goals_scored.

        Returns
        -------
        int
            The value of property away_team_goals_scored.
        """
        return self._away_team_goals_scored

    @away_team_goals_scored.setter
    def away_team_goals_scored(self, away_team_goals_scored):
        """
        Getter method for property away_team_goals_scored.

        Parameters
        ----------
        away_team_goals_scored : int
            The value you wish to set the away_team_goals_scored property to.
        """
        self._away_team_goals_scored = away_team_goals_scored
