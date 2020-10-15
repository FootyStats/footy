"""Prediction Engine - Engine to predict the result of future fixtures."""
# calculate the results for fixtures
from footy.domain import Competition


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

    def predict_fixture_results(self, fixture):
        """
        Generate the predictions for the given fixture.

        Parameters
        ----------
        fixture : footy.domain.Fixture
            The fixture to predict the results of
        Return
        -------
        footy.domain.Fixture
            Enriched Fixture with most recent predictions.
        """
        return Fixture