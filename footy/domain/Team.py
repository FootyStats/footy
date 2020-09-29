
class Team:

    def __init__(self, team_name, goals_for=0, goals_against=0, home_games=0, away_games=0, points=0):
        self.__team_name = team_name
        self._goals_for = goals_for
        self._goals_against = goals_against
        self._home_games = home_games
        self._away_games = away_games
        self._points = points
        self._goal_difference = 0
        self.recalculate_goal_difference()

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items())
        )

    @property
    def team_name(self):
        return self.__team_name

    @property
    def goals_for(self):
        return self._goals_for

    @goals_for.setter
    def goals_for(self, goals_for):
        self._goals_for = goals_for

    @property
    def goals_against(self):
        return self._goals_against

    @goals_against.setter
    def goals_against(self, goals_against):
        self._goals_against = goals_against

    @property
    def home_games(self):
        return self._home_games

    @home_games.setter
    def home_games(self, home_games):
        self._home_games = home_games

    @property
    def away_games(self):
        return self._away_games

    @away_games.setter
    def away_games(self, away_games):
        self._away_games = away_games

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, points):
        self._points = points

    @property
    def goal_difference(self):
        return self.goals_for - self.goals_against

    def recalculate_goal_difference(self):
        self._goal_difference = self.goals_for - self.goals_against
