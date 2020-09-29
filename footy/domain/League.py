from footy import MissingDataException


class League:

    def __init__(self, league_name, teams=None, average_goals_scored_by_a_home_team=0,
                 average_goals_scored_by_an_away_team=0):
        self.__league_name = league_name
        self._teams = teams
        self._average_goals_scored_by_a_home_team = average_goals_scored_by_a_home_team
        self._average_goals_scored_by_an_away_team = average_goals_scored_by_an_away_team

    # TODO: Add methods for add_team and get_team

    @property
    def league_name(self):
        return self.__league_name

    @property
    def teams(self):
        return self._teams

    @teams.setter
    def teams(self, teams):
        self._teams = teams

    @property
    def average_goals_scored_by_a_home_team(self):
        # This should be calculated based on match history
        return self._average_goals_scored_by_a_home_team

    @average_goals_scored_by_a_home_team.setter
    def average_goals_scored_by_a_home_team(self, average_goals_scored_by_a_home_team):
        self._average_goals_scored_by_a_home_team = average_goals_scored_by_a_home_team

    @property
    def average_goals_scored_by_an_away_team(self):
        # This should be calculated based on match history
        return self._average_goals_scored_by_an_away_team

    @average_goals_scored_by_an_away_team.setter
    def average_goals_scored_by_an_away_team(self, average_goals_scored_by_an_away_team):
        self._average_goals_scored_by_an_away_team = average_goals_scored_by_an_away_team

    def goals_conceded(self, team_name=None):
        """
        Get the number of goals conceded.

        If the team name is provided then the number of goals conceded by that team is returned.  Otherwise the number
        of goals conceded by all teams is returned.

        Parameters
        ----------
        team_name : str, optional
            The name of the team to get the number of goals conceded.

        Returns
        -------
        int
            The number of goals conceded by the team or the league.

        Raises
        ------
        KeyError
            When a team name is provided that is not in the dataset.
        """
        if self._teams is None or len(self._teams) == 0:
            raise MissingDataException("No teams have been configured for this league: " + self.__league_name)

        if team_name:
            goals_conceded_by_team = self._teams[team_name].goals_against
            return goals_conceded_by_team
        else:
            return int(round(sum(team.goals_against for team in self._teams.values()) / len(self._teams.keys())))

    def goals_scored(self, team_name=None):
        """
        Get the number of goals scored.

        If team_name is provided, the number of goals scored by that team is returned.  If not, the average number of
        goals scored by all teams is returned.

        Parameters
        ----------
        team_name : str, optional
            The name of the team to get the number of goals scored.

        Returns
        -------
        int
            The number of goals scored by a team or in the league.

        Raises
        ------
        KeyError
            When a team name is provided that is not in the dataset.
        """
        if self._teams is None or len(self._teams) == 0:
            raise MissingDataException("No teams have been configured for this league: " + self.__league_name)

        if team_name:
            goals_scored_by_team = self._teams[team_name].goals_for
            return goals_scored_by_team
        else:
            return int(round(sum(team.goals_for for team in self._teams.values()) / len(self._teams.keys())))

    def defence_factor(self, team_name):
        """
        Get the defence factor for a team.

        Parameters
        ----------
        team_name : str
            The name of the team to get the defence factor for.

        Returns
        -------
        float
            The defence factor for a specific team.  If there is not enough
            data to calculate correctly, return None.

        Raises
        ------
        KeyError
            When a team name is provided that is not in the dataset.
        """
        try:
            team_average_goals_conceded = self.goals_conceded(team_name)
            league_average_goals_conceded = self.goals_conceded()
            defence_factor = team_average_goals_conceded
            defence_factor /= league_average_goals_conceded
        except ZeroDivisionError:
            return None

        return round(defence_factor, 2)

    def attack_strength(self, team_name):
        """
        Get the attack strength of a team.

        Parameters
        ----------
        team_name : str
            The name of the team to get the attack strength of.

        Returns
        -------
        float
            The attack strength of the team.  If there is not enough data to
            calculate this correctly, return None.

        Raises
        ------
        KeyError
            When a team name is provided that is not in the dataset.
        """
        try:
            team_average_goals_scored = self.goals_scored(team_name)
            league_average_goals_scored = self.goals_scored()
            attack_strength = team_average_goals_scored
            attack_strength /= league_average_goals_scored
        except ZeroDivisionError:
            return None

        return round(attack_strength, 2)