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
        self._historic_briers_scores = []
        self._historic_attack_strength = []
        self._historic_defence_factor = []

    def team_name(self):
        """
        Getter method for property team_name.

        Returns
        -------
        str
            The value of property team_name.
        """
        return self._team_name

    def goals_for(self, goals_for=None):
        """
        Getter/setter for property goals_for.

        Parameters
        ----------
        goals_for : int, optional
            Set the value of property goals_for.

        Returns
        -------
        int
            The value of property goals_for.
        """
        if goals_for is not None:
            self._goals_for = goals_for

        return self._goals_for

    def goals_against(self, goals_against=None):
        """
        Getter/setter method for property goals_against.

        Parameters
        ----------
        goals_against : int, optional
            The value to set the property to.

        Returns
        -------
        int
            The value of property goals_against.
        """
        if goals_against is not None:
            self._goals_against = goals_against
        return self._goals_against

    def historic_attack_strength(self, attack_strength=None):
        """
        Append attack strength (if provided) if not, return the list.

        Parameters
        ----------
        attack_strength : float, optional
            The attack strength to be appended to the historic attack strengths.

        Returns
        -------
        list of floats
            A list of the historic attack strengths.
        """
        if attack_strength is not None:
            self._historic_attack_strength.append(attack_strength)

        return self._historic_attack_strength

    def historic_briers_score(self, briers_score=None):
        """
        Append to the Briers Score list for outcomes.

        Parameters
        ----------
        briers_score : float

        Returns
        -------
        list of float
            List of the historic outcome Briers scores.
        """
        if briers_score is not None:
            self._historic_briers_scores.append(briers_score)
        return self._historic_briers_scores

    def historic_defence_factor(self, defence_factor=None):
        """
        Append defence factor (if provided) and provide historic figures.

        Parameters
        ----------
        defence_factor : float, optional
            The defence factor to be appended to the list.

        Returns
        -------
        list of float
            The historic defence factors for this team.
        """
        if defence_factor is not None:
            self._historic_defence_factor.append(defence_factor)

        return self._historic_defence_factor

    def home_games(self, home_games=None):
        """
        Setter/getter method for property home_games.

        Parameters
        ----------
        home_games : int, optional
            The value you wish to set the home_games property to.

        Returns
        -------
        int
            The value of property home_games.
        """
        if home_games is not None:
            self._home_games = home_games
        return self._home_games

    def away_games(self, away_games=None):
        """
        Getter/setter method for property away_games.

        Parameters
        ----------
        away_games : int, optional
            The value you wish to set the away_games property to.

        Returns
        -------
        int
            The value of property away_games.
        """
        if away_games is not None:
            self._away_games = away_games
        return self._away_games

    def points(self, points=None):
        """
        Getter/setter method for property points.

        Parameters
        ----------
        points : int, optional
            The value you wish to set the points property to.

        Returns
        -------
        int
            The value of property points.
        """
        if points is not None:
            self._points = points
        return self._points

    def goal_difference(self):
        """
        Calculate and return the goal difference for the team.

        Returns
        -------
        int
            goals_for - goals_against
        """
        return self._goals_for - self._goals_against
