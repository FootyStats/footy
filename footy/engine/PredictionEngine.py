
# calculate the results for fixtures
from footy.footy.domain.Competition import Competition


class PredictionEngine:

    def __init__(self, competition):
        self._competition = competition
        self._results = {}

    def predict_results(self, competition):
        return Competition
