"""Result - Data structure for a result."""
# Is prediction before game is played, then actual once game ahs been played
# Return the outcome Briers score, home/away goals scored, Predictions if available, and actual
# result if game has been played


class Result:
    """Result - Data structure for a result."""

    def __init__(self):
        """Construct a Result object."""
        self._home_team_goals_scored = 0
        self._away_team_goals_scored = 0
        # 'SCHEDULED' or 'FINISHED'   TODO: Can we use an enum?
        self._status = ''
