# coding=utf-8
"""Regression Tests for BBC Article Basis feature tests."""

from footy import Footy
from footy.domain.Team import Team

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario(
    '../features/regression.feature',
    'Last Day of the EPL 2009 Season',
    example_converters=dict(
        home_team=str,
        away_team=str,
        home_team_win_probability=float,
        score_draw_probability=float,
        away_team_win_probability=float,
        expected_home_team_goals=int,
        expected_away_team_goals=int,
        final_score_probability=float
    )
)
def test_last_day_of_the_epl_2009_season():
    """Last Day of the EPL 2009 Season."""


@given('the last day of the EPL 2009', target_fixture='test_data')
def the_last_day_of_the_epl_2009():
    """the last day of the EPL 2009."""
    footy = Footy()

    footy.add_team(Team('Arsenal', 64, 36, 18, 19, 69))
    footy.add_team(Team('Aston Villa', 53, 48, 18, 19, 59))
    footy.add_team(Team('Blackburn', 40, 60, 18, 19, 40))
    footy.add_team(Team('Bolton', 41, 52, 19, 18, 41))
    footy.add_team(Team('Chelsea', 65, 22, 19, 18, 80))
    footy.add_team(Team('Everton', 53, 37, 19, 18, 60))
    footy.add_team(Team('Fulham', 39, 32, 18, 19, 53))
    footy.add_team(Team('Hull', 39, 63, 18, 19, 35))
    footy.add_team(Team('Liverpool', 74, 26, 18, 19, 83))
    footy.add_team(Team('Man City', 57, 50, 18, 19, 47))
    footy.add_team(Team('Man United', 67, 24, 19, 18, 87))
    footy.add_team(Team('Middlesbrough', 27, 55, 19, 18, 32))
    footy.add_team(Team('Newcastle', 40, 58, 19, 18, 34))
    footy.add_team(Team('Portsmouth', 38, 56, 19, 18, 41))
    footy.add_team(Team('Stoke', 37, 51, 19, 18, 45))
    footy.add_team(Team('Sunderland', 32, 51, 18, 19, 36))
    footy.add_team(Team('Tottenham', 44, 42, 19, 18, 51))
    footy.add_team(Team('West Brom', 36, 67, 19, 18, 31))
    footy.add_team(Team('West Ham', 40, 44, 18, 19, 48))
    footy.add_team(Team('Wigan', 33, 45, 18, 19, 42))
    footy.average_goals_scored_by_a_home_team(1.36)
    footy.average_goals_scored_by_an_away_team(1.06)

    return {
        'footy': footy
    }


@when('the away team is <away_team>')
def the_away_team_is_away_team(test_data, away_team):
    """the away team is <away_team>."""
    test_data['away_team_name'] = away_team
    footy = test_data['footy']

    response = footy.fixture(
        footy.get_team(test_data['home_team_name']),
        footy.get_team(test_data['away_team_name'])
    )

    outcome_probabilities = response.outcome_probabilities()

    # We allow some wriggle room for the values calculated.  This is
    # because the maximum number of goals we test up to is six.  However,
    # the sum of all the probabilities for the Arsenal v Stoke games
    # is actually 98.01 (not a perfect 100.0).  Therefore we subtract the
    # sum from 1.0 and use the result as a variance to compare against.
    probabilities_sum = outcome_probabilities[0]
    probabilities_sum += outcome_probabilities[1]
    probabilities_sum += outcome_probabilities[2]
    delta = abs(1.0 - probabilities_sum)
    test_data['home_team_win_probability'] = outcome_probabilities[0]
    test_data['score_draw_probability'] = outcome_probabilities[1]
    test_data['away_team_win_probability'] = outcome_probabilities[2]
    test_data['delta'] = delta


@when('the home team is <home_team>')
def the_home_team_is_home_team(test_data, home_team):
    """then home team is <home_team>."""
    test_data['home_team_name'] = home_team


@then('expect a score draw probability to be <score_draw_probability>')
def expect_a_score_draw_probability_to_be_score_draw_probability():
    """expect a score draw probability to be <score_draw_probability>."""
    raise NotImplementedError


@then('expect an away team probability to be <away_team_win_probability>')
def expect_an_away_team_probability_to_be_away_team_win_probability():
    """expect an away team probability to be <away_team_win_probability>."""
    raise NotImplementedError


@then('expect the home team win probability to be <home_team_win_probability>')
def expect_the_home_team_win_probability_to_be_home_team_win_probability(test_data, home_team_win_probability):
    """expect the home team win probability to be <home_team_win_probability>."""
    raise NotImplementedError


@then('expect the predicted final score probability to be <final_score_probability>')
def expect_the_predicted_final_score_probability_to_be_final_score_probability():
    """expect the predicted final score probability to be <final_score_probability>."""
    raise NotImplementedError


@then('expect the predicted goals to be scored by the away team to be <expected_away_team_goals>')
def expect_the_predicted_goals_to_be_scored_by_the_away_team_to_be_expected_away_team_goals():
    """expect the predicted goals to be scored by the away team to be <expected_away_team_goals>."""
    raise NotImplementedError


@then('expect the predicted goals to be scored by the home team to be <expected_home_team_goals>')
def expect_the_predicted_goals_to_be_scored_by_the_home_team_to_be_expected_home_team_goals():
    """expect the predicted goals to be scored by the home team to be <expected_home_team_goals>."""
    raise NotImplementedError
