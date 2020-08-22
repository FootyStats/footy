"""Footy - A statistics module for football (soccer)."""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from scipy.stats import poisson


class Footy:
    """
    Main class of the footy module.

    Examples
    --------
    >>> import footy
    >>> widget = footy.Footy()
    >>> widget.add_team('Arsenal', 64, 36, 18, 19)
    >>> widget.add_team('Aston Villa', 53, 48, 18, 19)
    >>> widget.add_team('Blackburn', 40, 60, 18, 19)
    >>> widget.add_team('Bolton', 41, 52, 19, 18)
    >>> widget.add_team('Chelsea', 65, 22, 19, 18)
    >>> widget.add_team('Everton', 53, 37, 19, 18)
    >>> widget.add_team('Fulham', 39, 32, 18, 19)
    >>> widget.add_team('Hull', 39, 63, 18, 19)
    >>> widget.add_team('Liverpool', 74, 26, 18, 19)
    >>> widget.add_team('Man City', 57, 50, 18, 19)
    >>> widget.add_team('Man United', 67, 24, 19, 18)
    >>> widget.add_team('Middlesbrough', 27, 55, 19, 18)
    >>> widget.add_team('Newcastle', 40, 58, 19, 18)
    >>> widget.add_team('Portsmouth', 38, 56, 19, 18)
    >>> widget.add_team('Stoke', 37, 51, 19, 18)
    >>> widget.add_team('Sunderland', 32, 51, 18, 19)
    >>> widget.add_team('Tottenham', 44, 42, 19, 18)
    >>> widget.add_team('West Brom', 36, 67, 19, 18)
    >>> widget.add_team('West Ham', 40, 44, 18, 19)
    >>> widget.add_team('Wigan', 33, 45, 18, 19)

    Get the data contained by the object as a Pandas dataframe.

    >>> widget.dataframe()

    Setting the number of average goals scored.

    >>> widget.average_goals_scored((1.36, 1.06))
    >>> widget.score_probability('Arsenal', 'Stoke').head()

    Plot the outcome probability

    >>> widget.outcome_probability('Arsenal', 'Stoke')

    Get a list of all the teams from the dataset.

    >>> widget.get_teams()
    """

    def __init__(self):
        """Construct a Footy object."""
        self._data = {}
        self._average_goals_scored = (-1)

    def add_team(self,
                 team_name,
                 goals_for,
                 goals_against,
                 home_games,
                 away_games):
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
        """
        data = self.data()
        team_stats = {
            'goals_for': goals_for,
            'goals_against': goals_against,
            'home_games': home_games,
            'away_games': away_games
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
            The attack strength of the team.
        """
        team_average_goals_scored = self.goals_scored(team_name)
        league_average_goals_scored = self.goals_scored()
        attack_strength = team_average_goals_scored
        attack_strength /= league_average_goals_scored
        return round(attack_strength, 2)

    def average_goals_scored(self, average_goals_scored=None):
        """
        Get or set the average goals scored by home and away teams.

        Parameters
        ----------
        average_goals_scored : Tuple of two floats, optional
            The average goals scored by a home team and the average goals
            scored by an away team.

        Returns
        -------
        Tuple of two floats
            The average goals scored by a home team and the average goals
            scored by an away team.
        """
        if average_goals_scored is not None:
            self._average_goals_scored = average_goals_scored
        return self._average_goals_scored

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

        Returns
        -------
        pandas.DataFrame
            The object datq as a Pandas datafrome.
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
            The defence factor for a specific team.
        """
        team_average_goals_conceded = self.goals_conceded(team_name)
        league_average_goals_conceded = self.goals_conceded()
        defence_factor = team_average_goals_conceded
        defence_factor /= league_average_goals_conceded
        return round(defence_factor, 2)

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

    def outcome_probability(self, home_team, away_team, show_plot=True):
        """
        Return the probability of a home win, a draw or an away win.

        Parameters
        ----------
        home_team : str
            The name of the home team.
        away_team : str
            The name of the away team.
        show_plot : bool, optional
            Should a plot be shown (default is true).

        Returns
        -------
        tuple
            (home win probability, draw probability, away win probability).
        """
        df = self.score_probability(home_team, away_team, False)
        df = df[df.home > df.away]
        home_win_probability = round(sum(df.probability.values), 2)
        df = self.score_probability(home_team, away_team, False)
        df = df[df.home == df.away]
        draw_probability = round(sum(df.probability.values), 2)
        df = self.score_probability(home_team, away_team, False)
        df = df[df.home < df.away]
        away_win_probability = round(sum(df.probability.values), 2)

        if show_plot:
            labels = [f'{home_team} Win', 'Draw', f'{away_team} Win']
            sizes = [home_win_probability, draw_probability,
                     away_win_probability]

            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            # Equal aspect ratio ensures that pie is drawn as a circle.
            ax1.axis('equal')

            plt.show()

        return (home_win_probability, draw_probability, away_win_probability)

    def plot_goal_probability(self, goals, probability_mass, title):
        """
        Plot the probability of goals being scored by a team.

        Parameters
        ----------
        goals : List of int
            Number of goals from 0 to 6.
        probability_mass : List of float
            The probability of the team, scoring a number of goals.
        title : str
            The title of the plot.
        """
        plt.bar(goals, probability_mass * 100.0)
        plt.title(title)
        plt.xlabel('Probable Goals')
        plt.ylabel('Percentage (%)')
        plt.show()

    def score_probability(self, home_team, away_team, show_plots=True):
        """
        Return a dataframe of the score probability.

        Parameters
        ----------
        home_team : str
            The name of the home team.
        away_team : str
            The name of the away team.
        show_plots: bool, optional
            Should the probability be plotted (default True).

        Returns
        -------
        pandas.DataFrame
            The probability of the games score.
        """
        (home_expected_goals,
         away_expected_goals) = self.average_goals_scored()
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

        if show_plots:
            self.plot_goal_probability(goals,
                                       home_probability_mass,
                                       f"{home_team} Goal Probability")
            self.plot_goal_probability(goals,
                                       away_probability_mass,
                                       f"{away_team} Goal Probability")

        df = pd.DataFrame(probabilities, columns=['home',
                                                  'away',
                                                  'probability'])
        df = df[df.probability != 0]
        df = df.sort_values('probability', ascending=False)
        df = df.reset_index(drop=True)
        return df
