"""Competition - Data structure for a competition/league."""


class Competition:
    """Competition - Data structure for a competition/league."""

    def __init__(self, code, name=None, teams=None, start_date=None, end_date=None, stage='unknown', fixtures=None):
        """
        Construct a Competition object.

        Parameters
        ----------
        code : str
            The code for the competition.
        name : str, optional
            The name of the competition.
        teams : list, optional
            The teams who are part of the competition. Defaults to an empty list.
        start_date : str, optional
            UTC date/time when the competition starts.
        start_date : str, optional
            UTC date/time when the competition ends.
        stage : str, optional
            What stage of the competition is currently underway. Defaults to 'unknown'.
        teams : list, optional
            Fixtures for the competition. Defaults to an empty list.
        """
        self._code = code
        self._name = name
        self._teams = teams or []
        self._start_date = start_date
        self._end_date = end_date
        self._stage = stage
        self._fixtures = fixtures or []

    @property
    def code(self):
        """
        Getter method for property code.

        Returns
        -------
        str
            The value of property code.
        """
        return self._code

    @property
    def name(self):
        """
        Getter method for property name.

        Returns
        -------
        str
            The value of property name.
        """
        return self.name

    @name.setter
    def name(self, name):
        """
        Getter method for property name.

        Parameters
        ----------
        name : str
            The value you wish to set the name property to.
        """
        self._name = name

    @property
    def teams(self):
        """
        Getter method for property teams.

        Returns
        -------
        list
            The value of property teams.
        """
        return self.teams

    @teams.setter
    def teams(self, teams):
        """
        Getter method for property teams.

        Parameters
        ----------
        teams : list
            The value you wish to set the teams property to.
        """
        self._teams = teams

    @property
    def start_date(self):
        """
        Getter method for property start_date.

        Returns
        -------
        str
            The value of property start_date.
        """
        return self.start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Getter method for property start_date.

        Parameters
        ----------
        start_date : str
            The value you wish to set the start_date property to.
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """
        Getter method for property end_date.

        Returns
        -------
        str
            The value of property end_date.
        """
        return self.end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Getter method for property end_date.

        Parameters
        ----------
        end_date : str
            The value you wish to set the end_date property to.
        """
        self._end_date = end_date

    @property
    def stage(self):
        """
        Getter method for property stage.

        Returns
        -------
        str
            The value of property stage.
        """
        return self.stage

    @stage.setter
    def stage(self, stage):
        """
        Getter method for property stage.

        Parameters
        ----------
        stage : str
            The value you wish to set the stage property to.
        """
        self._stage = stage

    @property
    def fixtures(self):
        """
        Getter method for property fixtures.

        Returns
        -------
        list
            The value of property fixtures.
        """
        return self.fixtures

    @fixtures.setter
    def fixtures(self, fixtures):
        """
        Getter method for property fixtures.

        Parameters
        ----------
        fixtures : list
            The value you wish to set the fixtures property to.
        """
        self._fixtures = fixtures
