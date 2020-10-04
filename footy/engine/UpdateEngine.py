"""Prediction Engine - Update the data model with the most resent fixtures and results."""

from footy.footy.domain import Competition


class UpdateEngine:
    """Prediction Engine - Update the data model with the most resent fixtures and results."""

    def __init__(self):
        """Construct a UpdateEngine object."""

    def get_competition(self, code):
        """
        Retrieve data for the supplied competition code.

        Returns
        -------
        Competition
            A Competition object with the most recent fixtures and results for the supplied competition code.
        """
        # return Competition
        return Competition

    def update_competition(self, competition):
        """
        Retrieve data and enrich the supplied competition with the most recent fixtures and results.

        Returns
        -------
        Competition
            A Competition object with the most recent fixtures and results for the supplied competition code.
        """
        return Competition
