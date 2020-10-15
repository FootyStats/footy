"""Prediction Engine - Engine to predict the result of future fixtures."""
# calculate the results for fixtures
from footy.domain import Competition
from footy.domain.Fixture import Fixture


class PredictionEngine:
    """Prediction Engine - Engine to predict the result of future fixtures."""

    def __init__(self, competition):
        """Construct a competition object."""
        self._competition = competition
        self._results = {}

    def predict_results(self, competition):
        """
        Generate the predictions for fixtures within a competition.

        Return
        -------
        Competition
            Enriched competition with most recent predictions.
        """
        return Competition
