"""Fixture - Data structure for a fixture."""


from footy.domain.Result import Result


class Fixture:
    """Fixture - Data structure for a fixture."""

    def __init__(self, home_team, away_team, status='SCHEDULED', utc_start='', result=None):
        """
        Construct a Fixture object.

        Parameters
        ----------
        home_team : Team
            The home team playing in this fixture.
        away_team : Team
            The home team playing in this fixture.
        status : str, optional
            The status of this fixture. Defaults to 'SCHEDULED'.
        utc_start : str, optional
            UTC date/time when the fixture is scheduled to start. Defaults to empty string.
        result : Result, optional
            The result of the fixture; defaults to new Result object.
        """
        self._home_team = home_team
        self._away_team = away_team
        self._status = status
        self._utc_start = utc_start
        self._result = result or Result()

    @property
    def home_team(self):
        """
        Getter method for property home_team.

        Returns
        -------
        Team
            The value of property home_team.
        """
        return self._home_team

    @home_team.setter
    def home_team(self, home_team):
        """
        Getter method for property home_team.

        Parameters
        ----------
        home_team : Team
            The value you wish to set the home_team property to.
        """
        self._home_team = home_team

    @property
    def away_team(self):
        """
        Getter method for property away_team.

        Returns
        -------
        Team
            The value of property away_team.
        """
        return self._away_team

    @away_team.setter
    def away_team(self, away_team):
        """
        Getter method for property away_team.

        Parameters
        ----------
        away_team : Team
            The value you wish to set the away_team property to.
        """
        self._away_team = away_team

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
    def utc_start(self):
        """
        Getter method for property utc_start.

        Returns
        -------
        str
            The value of property utc_start.
        """
        return self._utc_start

    @utc_start.setter
    def utc_start(self, utc_start):
        """
        Getter method for property utc_start.

        Parameters
        ----------
        utc_start : str
            The value you wish to set the utc_start property to.
        """
        self._utc_start = utc_start

    @property
    def result(self):
        """
        Getter method for property result.

        Returns
        -------
        Result
            The value of property result.
        """
        return self._result

    @result.setter
    def result(self, result):
        """
        Getter method for property result.

        Parameters
        ----------
        result : Result
            The value you wish to set the result property to.
        """
        self._result = result
