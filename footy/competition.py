"""competition.py:  The Competition class of the footy package."""
import numpy as np

import footy


class Competition:
    """
    The competition class.

    Examples
    --------
    >>> import football_data_api
    >>>
    >>> football_data = football_data_api.CompetitionData()
    >>> football_data.competition = 'premier league'
    >>> competition = Competition(football_data)
    """

    def __init__(self, football_data_api):
        """
        Construct a Competition object.

        Parameters
        ----------
        football_data_api : football_data_api.data_fetchers.CompetitionData
            As returned by football_data_api.CompetitionData()
        """
        self._raw_matches_data = football_data_api.get_info('matches')
        footy_obj = footy.Footy()
        team_names = []

        for match in self._raw_matches_data['matches']:
            home_team_name = match['homeTeam']['name']
            away_team_name = match['awayTeam']['name']

            if home_team_name not in team_names:
                team_names.append(home_team_name)

            if away_team_name not in team_names:
                team_names.append(away_team_name)

        teams_data = {}

        for team_name in sorted(team_names):
            footy_obj.add_team(team_name, 0, 0, 0, 0, 0)
            teams_data[team_name] = {
                'attack_strengths': [],
                'briers_scores': {
                    'outcomes': [],
                    'outcomes_away': [],
                    'outcomes_home': [],
                    'goals_scored': [],
                    'goals_scored_away': [],
                    'goals_scored_home': []
                },
                'defence_factors': []
            }

        self._teams_data = teams_data
        self._footy = footy_obj
        current_match_day = self._raw_matches_data['matches'][0]['season']['currentMatchday']
        self._current_match_day = current_match_day
        total_games_played = 0
        total_goals_scored_by_home_team = 0
        total_goals_scored_by_away_team = 0

        for match_day in range(1, current_match_day):
            for match in self._raw_matches_data['matches']:
                if match['matchday'] != match_day:
                    # Skip this match iteration if not for the relevant match day.
                    continue

                home_team_name = match['homeTeam']['name']
                away_team_name = match['awayTeam']['name']
                full_time = match['score']['fullTime']
                home_team_goals = full_time['homeTeam']
                away_team_goals = full_time['awayTeam']

                if home_team_goals is None or away_team_goals is None:
                    # Skip if the data feed has not been updated for a game yet.
                    continue

                self.set_result(home_team_name, home_team_goals, away_team_name, away_team_goals)
                total_games_played += 1
                total_goals_scored_by_home_team += home_team_goals
                total_goals_scored_by_away_team += away_team_goals

            footy_obj.average_goals_scored_by_a_home_team(
                round(total_goals_scored_by_home_team / total_games_played, 2)
            )
            footy_obj.average_goals_scored_by_an_away_team(
                round(total_goals_scored_by_away_team / total_games_played, 2)
            )

            for team_name in footy_obj.get_teams():
                attack_strength = footy_obj.attack_strength(team_name)

                if attack_strength is not None:
                    teams_data[team_name]['attack_strengths'].append(attack_strength)

                defence_factor = footy_obj.defence_factor(team_name)

                if defence_factor is not None:
                    teams_data[team_name]['defence_factors'].append(defence_factor)

    def get_model_data(self):
        """
        Return the modelled data as a dictionary.

        Returns
        -------
        dict

        The data.
        """
        teams = {}
        footy_obj = self._footy

        model_data = {
            'table': footy_obj.dataframe(),
            'upcoming_fixtures': self.upcoming_fixtures()
        }

        for team_name in footy_obj.get_teams():
            team_data = footy_obj.get_team(team_name)
            team_data['briers_scores'] = self._teams_data[team_name]['briers_scores']
            team_data['attack_strengths'] = self._teams_data[team_name]['attack_strengths']
            team_data['defence_factors'] = self._teams_data[team_name]['defence_factors']
            teams[team_name] = team_data

        model_data['teams'] = teams
        return model_data

    def set_result(self, home_team_name, home_team_goals, away_team_name, away_team_goals):
        """
        Post result processing to aggregate Briers scores.

        Parameters
        ----------
        home_team_name : str
            The name of the home team.
        home_team_goals : int
            The number of goals scored by the home team.
        away_team_name : str
            The name of the away team.
        away_team_goals
            The number of goals scored by the away team.
        """
        footy_obj = self._footy
        home_team = footy_obj.get_team(home_team_name)
        away_team = footy_obj.get_team(away_team_name)
        fixture_data = footy_obj.fixture(home_team_name, away_team_name)

        if home_team_goals > away_team_goals:
            result_outcome = footy.OUTCOME_HOME_WIN
            home_team_points = 3
            away_team_points = 0
        elif home_team_goals == away_team_goals:
            result_outcome = footy.OUTCOME_SCORE_DRAW
            home_team_points = 1
            away_team_points = 1
        else:
            result_outcome = footy.OUTCOME_AWAY_WIN
            home_team_points = 0
            away_team_points = 3

        footy_obj.add_team(home_team_name,
                           home_team['goals_for'] + home_team_goals,
                           home_team['goals_against'] + away_team_goals,
                           home_team['home_games'] + 1,
                           home_team['away_games'],
                           home_team['points'] + home_team_points
                           )
        footy_obj.add_team(away_team_name,
                           away_team['goals_for'] + away_team_goals,
                           away_team['goals_against'] + home_team_goals,
                           away_team['home_games'],
                           away_team['away_games'] + 1,
                           away_team['points'] + away_team_points
                           )

        if fixture_data is None:
            return

        y_prob = np.array(fixture_data['outcome_probabilities'])
        y_prob = y_prob / 100
        briers_score_outcome = footy_obj.brier_score(result_outcome, y_prob)
        home_team_goals_probability = fixture_data['home_team_goals_probability']
        y_true = [0] * len(home_team_goals_probability)
        y_true[home_team_goals] = 1
        briers_score_home_goals_scored = footy_obj.brier_score(y_true, home_team_goals_probability)

        away_team_goals_probability = fixture_data['away_team_goals_probability']
        y_true = [0] * len(away_team_goals_probability)
        y_true[away_team_goals] = 1
        briers_score_away_goals_scored = footy_obj.brier_score(y_true, away_team_goals_probability)

        teams_data = self._teams_data
        teams_data[home_team_name]['briers_scores']['outcomes'].append(briers_score_outcome)
        teams_data[home_team_name]['briers_scores']['outcomes_home'].append(briers_score_outcome)
        teams_data[home_team_name]['briers_scores']['goals_scored'].append(briers_score_home_goals_scored)
        teams_data[home_team_name]['briers_scores']['goals_scored_home'].append(briers_score_home_goals_scored)

        teams_data[away_team_name]['briers_scores']['outcomes'].append(briers_score_outcome)
        teams_data[away_team_name]['briers_scores']['outcomes_away'].append(briers_score_outcome)
        teams_data[away_team_name]['briers_scores']['goals_scored'].append(briers_score_away_goals_scored)
        teams_data[away_team_name]['briers_scores']['goals_scored_away'].append(briers_score_away_goals_scored)
        self._teams_data = teams_data

    def upcoming_fixtures(self):
        """
        Return the upcoming fixtures for this competition.

        The plan is to ensure that at least each team in the upcoming games in the league are returned with
        the data (if available) on the game probabilities.

        Returns
        -------
        List of dict
            The details of the fixture (home_team_name, away_team_name, utc_timestamp) and if available (depending
            on if enough games have been played) the details from the footy.fixture method.
        """
        fixtures = []
        footy_obj = self._footy
        matches = self._raw_matches_data['matches']
        teams = self._footy.get_teams()

        for match in matches:
            if match['status'] == 'FINISHED':
                continue

            utc_timestamp = match['utcDate']
            home_team = match['homeTeam']['name']
            away_team = match['awayTeam']['name']
            fixture = footy_obj.fixture(home_team, away_team)

            if fixture is None:
                fixture = {}

            fixture['home_team'] = home_team
            fixture['away_team'] = away_team
            fixture['utc_timestamp'] = utc_timestamp
            fixtures.append(fixture)

            if home_team in teams:
                teams.remove(home_team)

            if away_team in teams:
                teams.remove(away_team)

            if not len(teams):
                break

        return fixtures
