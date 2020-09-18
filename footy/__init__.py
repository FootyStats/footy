"""Footy - A statistics module for football (soccer)."""
import numpy as np
import pandas as pd

from scipy.stats import poisson
from sklearn.metrics import brier_score_loss

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

    Please note that methods that accept a team name parameter that the team
    name must match exactly (including case sensitivity).  Use the
    get_teams method to get a list of valid team names.

    Examples
    --------
    >>> import footy
    >>> widget = footy.Footy()
    >>> widget.add_team('Arsenal', 64, 36, 18, 19, 69)
    >>> widget.add_team('Aston Villa', 53, 48, 18, 19, 59)
    >>> widget.add_team('Blackburn', 40, 60, 18, 19, 40)
    >>> widget.add_team('Bolton', 41, 52, 19, 18, 41)
    >>> widget.add_team('Chelsea', 65, 22, 19, 18, 80)
    >>> widget.add_team('Everton', 53, 37, 19, 18, 60)
    >>> widget.add_team('Fulham', 39, 32, 18, 19, 53)
    >>> widget.add_team('Hull', 39, 63, 18, 19, 35)
    >>> widget.add_team('Liverpool', 74, 26, 18, 19, 83)
    >>> widget.add_team('Man City', 57, 50, 18, 19, 47)
    >>> widget.add_team('Man United', 67, 24, 19, 18, 87)
    >>> widget.add_team('Middlesbrough', 27, 55, 19, 18, 32)
    >>> widget.add_team('Newcastle', 40, 58, 19, 18, 34)
    >>> widget.add_team('Portsmouth', 38, 56, 19, 18, 41)
    >>> widget.add_team('Stoke', 37, 51, 19, 18, 45)
    >>> widget.add_team('Sunderland', 32, 51, 18, 19, 36)
    >>> widget.add_team('Tottenham', 44, 42, 19, 18, 51)
    >>> widget.add_team('West Brom', 36, 67, 19, 18, 31)
    >>> widget.add_team('West Ham', 40, 44, 18, 19, 48)
    >>> widget.add_team('Wigan', 33, 45, 18, 19, 42)

    Get the data contained by the object as a Pandas dataframe (sorted by
    league position and goal difference).

    >>> widget.dataframe()

    Setting the number of average goals scored.

    >>> widget.average_goals_scored_by_a_home_team(1.36)
    >>> widget.average_goals_scored_by_an_away_team(1.06)

    Now get the prediction of game (will return None if not enough data is
    available).  For the full details of the response returned, see the
    `fixture` method.

    >>> response = widget.fixture('Arsenal', 'Stoke')

    Get a list of all the teams from the dataset.

    >>> widget.get_teams()
    """

    def __init__(self):
        """Construct a Footy object."""
        self._data = {}
        self._average_goals_scored_by_a_home_team = (-1)
        self._average_goals_scored_by_an_away_team = (-1)

    def add_team(self,
                 team_name,
                 goals_for,
                 goals_against,
                 home_games,
                 away_games,
                 points):
        """
        Add a team to the table.

        Parameters
        ----------
        team_name : str
            The name of the team to add.
        goals_for : int
            The number of goals scored by the team.
        goals_against : int
            The number of goals conceded by the team.
        home_games : int
            The number of home games played by the team.
        away_games : int
            The number of away games played by the team.
        points : int
            The number of points in the table that the team has.
        """
        data = self.data()
        team_stats = {
            'goals_for': goals_for,
            'goals_against': goals_against,
            'home_games': home_games,
            'away_games': away_games,
            'goal_difference': (goals_for - goals_against),
            'points': points
        }
        data[team_name] = team_stats
        self.data(data)

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

    def average_goals_scored_by_a_home_team(self, goals=None):
        """
        Get or set the average goals scored by a home team.

        Parameters
        ----------
        goals : float
             The average number of goals scored by any team playing at home
             over the duration of the season.

        Returns
        -------
        float
             The average number of goals scored by any team playing at home
             over the duration of the season.
        """
        if goals is not None:
            self._average_goals_scored_by_a_home_team = goals
        return self._average_goals_scored_by_a_home_team

    def average_goals_scored_by_an_away_team(self, goals=None):
        """
        Get or set the average goals scored by an away team.

        Parameters
        ----------
        goals : float
             The average number of goals scored by any team playing away
             over the duration of the season.

        Returns
        -------
        float
             The average number of goals scored by any team playing away
             over the duration of the season.
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
            What actually happened.  Should be a value for each predicted
            category (e.g. home win, score draw or away win).
        y_prob : np.array
            The predicted probability of each category.  The number of
            elements in this parameter must match the number of parameters
            given in y_true. The sum of all the values of this list cannot
            exceed 1.0.

        Returns
        -------
        float
            A value between 0.0 and 2.0 where a value closer to 0.0 indicates
            that a predicted probability was more accurate that a value
            closer to 2.0.  This result will be rounded to the nearest two
            decimal places.

        References
        ----------
        Brier, G.W. (1950): "Verification of Forecasts Expressed in Terms of
        Probability", Monthly Weather Review, volume 79, number 1.

        Examples
        --------
        >>> import footy
        >>> footy.brier_score(np.array([1, 0, 0]), np.array([1.0, 0.0, 0.0]))
        0.0
        """
        bs = brier_score_loss(y_true, y_prob)
        n = len(y_prob)
        return round(bs * n, 2)

    def data(self, data=None):
        """
        Get or set the object data.

        Parameters
        ----------
        data : dict, optional
            A new dictionary to replace the objects data.

        Returns
        -------
        dict
            The object data.
        """
        if data is not None:
            self._data = data
        return self._data

    def dataframe(self):
        """
        Return the object data as a Pandas dataframe.

        The dataframe will be sorted on the number of points and goal
        difference.

        Returns
        -------
        pandas.DataFrame
            The object data as a Pandas DataFrame.
        """
        a = []
        data = self.data()
        attack_strengths = []
        defence_factors = []

        for team_name in data.keys():
            team_dict = data[team_name]
            attack_strength = self.attack_strength(team_name)
            attack_strengths.append(attack_strength)
            defence_factor = self.defence_factor(team_name)
            defence_factors.append(defence_factor)
            team_list = [team_name]

            for value in list(team_dict.values()):
                team_list.append(value)

            a.append(team_list)

        columns = ['team_name']

        for key in list(team_dict.keys()):
            columns.append(key)

        df = pd.DataFrame(a, columns=columns)
        df['attack_strength'] = attack_strengths
        df['defence_factor'] = defence_factors
        df = df.sort_values(
            [
                'points',
                'goal_difference'
            ],
            ascending=[
                False,
                False
            ]
        )
        df = df.reset_index(drop=True)
        return df

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

    def fixture(self, home_team, away_team):
        """
        Calculate the probabilities of a fixture between two teams.

        Parameters
        ----------
        home_team : str
            The name of the home team.
        away_team : str
            The name of the away team.

        Returns
        -------
        dict
            If there is enough data for any probabilities to be calculated,
            the dictionary will contain elements called:

            outcome_probabilities: A list of three floats indicating (with
            values between 0.0 and 1.0) the probability of a home win, a
            score draw or an away win respectively.

            home_team_goals_probability: A list of seven floats indicating
            (with values between 0.0 and 1.0) the probability of the home team
            scoring between 0 and 6 goals.

            away_team_goals_probability: A list of seven floats indicating
            (with values between 0.0 and 1.0) the probability of the away team
            scoring between 0 and 6 goals.

            final_score_probabilities:  A Pandas DataFrame with each row
            containing the number of goals scored by the home team, the number
            of goals scored by the away team and the probability of that final
            score.  The table will be sorted with the most probable results
            descending.

            If there is not enough data to calculate the probabilities, the
            dictionary returned by this function will be empty.

        Raises
        ------
        KeyError
            When a team name is provided that is not in the dataset.
        """
        response = {}

        # Check that all teams have played more than zero home games.
        # If the check fails, return None as we do not have enough data
        # to calculate probabilities.
        df = self.dataframe()
        home_games = df['home_games'].values

        if 0 in home_games:
            return None

        # Check that all teams have played more than zero away games.
        # If the check fails, return None as we do not have enough data
        # to calculate probabilities.
        away_games = df['away_games'].values

        if 0 in away_games:
            return None

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
        response['final_score_probabilities'] = df

        df2 = df[df.home > df.away]
        home_win_probability = round(sum(df2.probability.values), 4)
        df2 = df[df.home == df.away]
        draw_probability = round(sum(df2.probability.values), 4)
        df2 = df[df.home < df.away]
        away_win_probability = round(sum(df2.probability.values), 4)

        response['outcome_probabilities'] = [
            home_win_probability,
            draw_probability,
            away_win_probability
        ]

        response['home_team_goals_probability'] = list(home_probability_mass)
        response['away_team_goals_probability'] = list(away_probability_mass)
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
        dict
            The elements of the returned dictionary are goals_for (the number
            of goals scored), goals_against (the number of goals conceded),
            home_games (number of games played at home), away_games (number of
            games played away).

        Examples
        --------
        Get the data specific to Arsenal.

        >>> widget.get_team('Arsenal')
        {'goals_for': 64, 'goals_against': 36, 'home_games': 18,
         'away_games': 19}
        """
        data = self.data()
        return data[team_name]

    def get_teams(self):
        """
        Get a list of the team names held in the dataset.

        Returns
        -------
        List of str
            A list of the team names.

        Examples
        --------
        Get a list of all the teams from the dataset.

        >>> widget.get_teams()
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
        """
        return list(self.data().keys())

    def goals_conceded(self, team_name=None):
        """
        Get the number of goals conceded.

        If the team name is provided then the number of goals conceded by
        that team is returned.  Otherwise the number of goals conceded by
        all teams is returned.

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
        data = self.data()

        if team_name:
            goals_conceded_by_team = data[team_name]['goals_against']
            return goals_conceded_by_team
        else:
            goals_conceded = 0

            for team_name in data.keys():
                goals_conceded += data[team_name]['goals_against']

            return int(round(goals_conceded / len(data.keys())))

    def goals_scored(self, team_name=None):
        """
        Get the number of goals scored.

        If team_name is provided, the number of goals scored by
        that team is returned.  If not, the average number of
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
        data = self.data()

        if team_name:
            goals_scored_by_team = data[team_name]['goals_for']
            return goals_scored_by_team
        else:
            goals_for = 0

            for team_name in data.keys():
                goals_for += data[team_name]['goals_for']

            return int(round(goals_for / len(data.keys())))
