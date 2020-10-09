"""Footy - A statistics module for football (soccer)."""
import numpy as np
import pandas as pd

from scipy.stats import poisson
from sklearn.metrics import brier_score_loss

from footy.domain.Fixture import Fixture

# Set match outcome constants.
OUTCOME_HOME_WIN = [1, 0, 0]
"""List of int : The notation of a home win outcome."""
OUTCOME_SCORE_DRAW = [0, 1, 0]
"""List of int : The notation of a score draw outcome."""
OUTCOME_AWAY_WIN = [0, 0, 1]
"""List of int : The notation of an away outcome."""


class Footy:
    """
    Main class of the footy module.

    Please note that methods that accept a team name parameter that the team name must match exactly (including case
    sensitivity).  Use the get_teams method to get a list of valid team names.

    Examples
    --------
    >>> import footy
    >>> widget = footy.Footy()
    >>> widget.add_team(Team('Arsenal', 64, 36, 18, 19, 69))
    >>> widget.add_team(Team('Aston Villa', 53, 48, 18, 19, 59))
    >>> widget.add_team(Team('Blackburn', 40, 60, 18, 19, 40))
    >>> widget.add_team(Team('Bolton', 41, 52, 19, 18, 41))
    >>> widget.add_team(Team('Chelsea', 65, 22, 19, 18, 80))
    >>> widget.add_team(Team('Everton', 53, 37, 19, 18, 60))
    >>> widget.add_team(Team('Fulham', 39, 32, 18, 19, 53))
    >>> widget.add_team(Team('Hull', 39, 63, 18, 19, 35))
    >>> widget.add_team(Team('Liverpool', 74, 26, 18, 19, 83))
    >>> widget.add_team(Team('Man City', 57, 50, 18, 19, 47))
    >>> widget.add_team(Team('Man United', 67, 24, 19, 18, 87))
    >>> widget.add_team(Team('Middlesbrough', 27, 55, 19, 18, 32))
    >>> widget.add_team(Team('Newcastle', 40, 58, 19, 18, 34))
    >>> widget.add_team(Team('Portsmouth', 38, 56, 19, 18, 41))
    >>> widget.add_team(Team('Stoke', 37, 51, 19, 18, 45))
    >>> widget.add_team(Team('Sunderland', 32, 51, 18, 19, 36))
    >>> widget.add_team(Team('Tottenham', 44, 42, 19, 18, 51))
    >>> widget.add_team(Team('West Brom', 36, 67, 19, 18, 31))
    >>> widget.add_team(Team('West Ham', 40, 44, 18, 19, 48))
    >>> widget.add_team(Team('Wigan', 33, 45, 18, 19, 42))

    Get the data contained by the object as a Pandas dataframe (sorted by
    league position and goal difference).

    >>> widget.dataframe()

    Setting the number of average goals scored.

    >>> widget.average_goals_scored_by_a_home_team(1.36)
    >>> widget.average_goals_scored_by_an_away_team(1.06)

    Now get the prediction of game (will return None if not enough data is
    available).  For the full details of the response returned, see the
    `fixture` method.

    >>> response = widget.fixture(widget.get_team('Arsenal'), widget.get_team('Stoke'))

    Get a list of all the teams from the dataset.

    >>> widget.get_team_names()
    ['Arsenal',
     'Aston Villa',
     'Blackburn',
     'Bolton',
     'Chelsea',
     'Everton',
     'Fulham',
     'Hull',
     'Liverpool',
     'Man City',
     'Man United',
     'Middlesbrough',
     'Newcastle',
     'Portsmouth',
     'Stoke',
     'Sunderland',
     'Tottenham',
     'West Brom',
     'West Ham',
     'Wigan']

    Get the data specific to Arsenal.

    >>> team = widget.get_team('Arsenal')

    Get a Bried Score for a result.

    >>> footy.brier_score(np.array([1, 0, 0]), np.array([1.0, 0.0, 0.0]))
    0.0
    """

    def __init__(self):
        """Construct a Footy object."""
        self._data = {}
        self._average_goals_scored_by_a_home_team = (-1)
        self._average_goals_scored_by_an_away_team = (-1)

    def add_team(self, team):
        """
        Add a team to the table.

        Parameters
        ----------
        team : footy.domain.Team.Team
            The team to set or update (using the team name as a key) in Footy object.
        """
        self._data[team.team_name] = team

    def attack_strength(self, team):
        """
        Get the attack strength of a team.

        The attack strength is calculated by dividing the number of goals scored by the team by the average goals
        scored by any team.  An attack strength higher than 1.0 indicates that the team scores more than the
        average number of goals by a team in the competition.

        Parameters
        ----------
        team : footy.domain.Team.Team
            The team to get the attack strength of.

        Returns
        -------
        float
            The attack strength of the team.  If there is not enough data to
            calculate this correctly, return None.

        Raises
        ------
        KeyError
            When a team that is provided that is not in the dataset.
        """
        try:
            league_average_goals_scored = self.goals_scored()
            attack_strength = team.goals_for / league_average_goals_scored
        except ZeroDivisionError:
            return None

        return round(attack_strength, 2)

    def average_goals_scored_by_a_home_team(self, goals=None):
        """
        Get or set the average goals scored by a home team.

        Parameters
        ----------
        goals : float, optional
             The average number of goals scored by any team playing at home over the duration of the season.

        Returns
        -------
        float
             The average number of goals scored by any team playing at home over the duration of the season.
        """
        if goals is not None:
            self._average_goals_scored_by_a_home_team = goals
        return self._average_goals_scored_by_a_home_team

    def average_goals_scored_by_an_away_team(self, goals=None):
        """
        Get or set the average goals scored by an away team.

        Parameters
        ----------
        goals : float, optional
             The average number of goals scored by any team playing away over the duration of the season.

        Returns
        -------
        float
             The average number of goals scored by any team playing away over the duration of the season.
        """
        if goals is not None:
            self._average_goals_scored_by_an_away_team = goals
        return self._average_goals_scored_by_an_away_team

    def brier_score(self, y_true, y_prob):
        """
        Return a Brier Score of the probability against the actuality.

        Parameters
        ----------
        y_true : np.array
            What actually happened.  Should be a value for each predicted category (e.g. home win, score draw or away
            win).
        y_prob : np.array
            The predicted probability of each category.  The number of elements in this parameter must match the number
            of parameters given in y_true. The sum of all the values of this list cannot exceed 1.0.

        Returns
        -------
        float
            A value between 0.0 and 2.0 where a value closer to 0.0 indicates that a predicted probability was more
            accurate that a value closer to 2.0.  This result will be rounded to the nearest two decimal places.

        References
        ----------
        Brier, G.W. (1950): "Verification of Forecasts Expressed in Terms of Probability", Monthly Weather Review,
        volume 79, number 1.
        """
        bs = brier_score_loss(y_true, y_prob)
        n = len(y_prob)
        return round(bs * n, 2)

    def dataframe(self):
        """
        Return the object data as a Pandas dataframe.

        The dataframe will be sorted on the number of points and goal difference.

        Returns
        -------
        pandas.DataFrame
            The object data as a Pandas DataFrame.
        """
        a = []
        attack_strengths = []
        defence_factors = []
        team_names = self.get_team_names()

        for team_name in team_names:
            team = self.get_team(team_name)
            attack_strength = self.attack_strength(team)
            attack_strengths.append(attack_strength)
            defence_factor = self.defence_factor(team)
            defence_factors.append(defence_factor)
            team_list = [
                team_name,
                team.goals_for,
                team.goals_against,
                team.home_games,
                team.away_games,
                team.goal_difference,
                team.points
            ]
            a.append(team_list)

        columns = [
            'team_name',
            'goals_for',
            'goals_against',
            'home_games',
            'away_games',
            'goal_difference',
            'points'
        ]

        df = pd.DataFrame(a, columns=columns)
        df['attack_strength'] = attack_strengths
        df['defence_factor'] = defence_factors
        df = df.sort_values(
            [
                'points',
                'goal_difference',
                'goals_for',
                'goals_against'
            ],
            ascending=[
                False,
                False,
                False,
                True
            ]
        )
        df = df.reset_index(drop=True)
        return df

    def defence_factor(self, team):
        """
        Get the defence factor for a team.

        The defence factor is calculated by dividing the number of goals that the team have conceded by the average
        number of goals conceded by all the teams in the competition.  A defence factor > 1.0 indicates that the
        team concedes more goals that of the average team.

        Parameters
        ----------
        team : footy.domain.Team.Team
            The team to get the defence factor for.

        Returns
        -------
        float
            The defence factor for a specific team.  If there is not enough
            data to calculate correctly, return None.

        Raises
        ------
        KeyError
            When the team provided is not in the dataset.
        """
        try:
            league_average_goals_conceded = self.goals_conceded()
            defence_factor = team.goals_against / league_average_goals_conceded
        except ZeroDivisionError:
            return None

        return round(defence_factor, 2)

    def fixture(self, home_team, away_team):
        """
        Calculate the probabilities of a fixture between two teams.

        Parameters
        ----------
        home_team : footy.domain.Team.Team
            The home team.
        away_team : footy.domain.Team.Team
            The away team.

        Returns
        -------
        footy.domain.Fixture.Fixture
            A fixture containing the predicted probabilities (if available).

        Raises
        ------
        KeyError
            When a team name is provided that is not in the dataset.
        """
        response = Fixture(home_team, away_team)

        # Check that all teams have played more than zero home games.
        # If the check fails, return None as we do not have enough data
        # to calculate probabilities.
        df = self.dataframe()
        home_games = df['home_games'].values

        if 0 in home_games:
            return response

        # Check that all teams have played more than zero away games.
        # If the check fails, return None as we do not have enough data
        # to calculate probabilities.
        away_games = df['away_games'].values

        if 0 in away_games:
            return response

        home_expected_goals = self.average_goals_scored_by_a_home_team()
        away_expected_goals = self.average_goals_scored_by_an_away_team()
        home_expected_goals *= self.attack_strength(home_team)
        home_expected_goals *= self.defence_factor(away_team)
        home_expected_goals = round(home_expected_goals, 2)
        goals = [0, 1, 2, 3, 4, 5, 6]
        probability_mass = poisson.pmf(goals, home_expected_goals)
        home_probability_mass = np.round(probability_mass, 2)
        away_expected_goals *= self.attack_strength(away_team)
        away_expected_goals *= self.defence_factor(home_team)
        away_expected_goals = round(away_expected_goals, 2)
        probability_mass = poisson.pmf(goals, away_expected_goals)
        away_probability_mass = np.round(probability_mass, 2)

        probabilities = []

        for home_team_goal in range(len(goals)):
            for away_team_goal in range(len(goals)):
                probability = home_probability_mass[home_team_goal]
                probability *= away_probability_mass[away_team_goal]
                probability = round(probability * 100.0, 2)
                probabilities.append([home_team_goal, away_team_goal,
                                      probability])

        df = pd.DataFrame(probabilities, columns=['home',
                                                  'away',
                                                  'probability'])
        df = df[df.probability != 0]
        df = df.sort_values('probability', ascending=False)
        df = df.reset_index(drop=True)
        response.final_score_probabilities(df)

        df2 = df[df.home > df.away]
        home_win_probability = round(sum(df2.probability.values), 4)
        df2 = df[df.home == df.away]
        draw_probability = round(sum(df2.probability.values), 4)
        df2 = df[df.home < df.away]
        away_win_probability = round(sum(df2.probability.values), 4)

        response.outcome_probabilities([
            home_win_probability,
            draw_probability,
            away_win_probability
        ])

        response.home_team_goals_probability(list(home_probability_mass))
        response.away_team_goals_probability(list(away_probability_mass))
        return response

    def get_team(self, team_name):
        """
        Get the details of a specific team from the dataset.

        Parameters
        ----------
        team_name : str
            The name of the team that the details are to be returned for.

        Raises
        ------
        KeyError
            When a team name is provided that is not in the dataset.

        Returns
        -------
        footy.domain.Team.Team
            The team referred by the team name.
        """
        return self._data[team_name]

    def get_team_names(self):
        """
        Get a list of the team names held in the dataset.

        Returns
        -------
        List of str
            A list of the team names.
        """
        team_names = self._data.keys()
        return sorted(team_names)

    def goals_conceded(self, team_name=None):
        """
        Get the number of goals conceded.

        If the team name is provided then the number of goals conceded by that team is returned.  Otherwise the number
        of goals conceded by all teams is returned.

        Parameters
        ----------
        team_name : footy.domain.Team.Team, optional
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
        if team_name:
            team = self.get_team(team_name)
            return team.goals_against
        else:
            goals_conceded = 0
            team_names = self.get_team_names()

            for team_name in team_names:
                team = self.get_team(team_name)
                goals_conceded += team.goals_against

            return int(round(goals_conceded / len(team_names)))

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
        if team_name:
            return self.get_team(team_name).goals_for
        else:
            goals_for = 0
            team_names = self.get_team_names()

            for team_name in team_names:
                team = self.get_team(team_name)
                goals_for += team.goals_for

            return int(round(goals_for / len(team_names)))
