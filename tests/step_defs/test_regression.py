# coding=utf-8
"""Last Day of the EPL 2009 Season feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from footy import Footy
from footy.domain.Team import Team


@scenario('../features/regression.feature',
          'Attack Strength Defence Factor',
          example_converters=dict(
              team_name=str,
              attack_strength=float,
              defence_factor=float
          ))
def test_attack_strength_defence_factor():
    """Attack Strength Defence Factor."""


@scenario('../features/regression.feature',
          'Expected Goals Home Team',
          example_converters=dict(
              home_team=str,
              away_team=str,
              team_name=str,
              expected_goals=float,
              predicted_goals=str
          ))
def test_expected_goals_home_team():
    """Expected Goals Home Team."""


@scenario('../features/regression.feature',
          'Expected Outcomes',
          example_converters=dict(
              home_team=str,
              away_team=str,
              prediction=str
          ))
def test_expected_outcomes():
    """Expected Outcomes."""


@given('the last day of the EPL 2009', target_fixture='last_day_of_the_season')
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


@when('the away_team is <away_team>')
def the_away_team_is_away_team(last_day_of_the_season, away_team):
    """the away_team is <away_team>."""
    footy = last_day_of_the_season['footy']
    last_day_of_the_season['away_team'] = footy.get_team(away_team)


@when('the home team is <home_team>')
def the_home_team_is_home_team(last_day_of_the_season, home_team):
    """the home team is <home_team>."""
    footy = last_day_of_the_season['footy']
    last_day_of_the_season['home_team'] = footy.get_team(home_team)


@when('the team name is <team_name>')
def the_team_name_is_team_name(last_day_of_the_season, team_name):
    """the team name is <team_name>."""
    footy = last_day_of_the_season['footy']
    last_day_of_the_season['team'] = footy.get_team(team_name)


@then('attack strength is <attack_strength>')
def attack_strength_is_attack_strength(last_day_of_the_season, attack_strength):
    """attack strength is <attack_strength>."""
    footy = last_day_of_the_season['footy']
    team = last_day_of_the_season['team']
    assert footy.attack_strength(team) == attack_strength, 'Incorrect attack strength.'


@then('defence factor is <defence_factor>')
def defence_factor_is_defence_factor(last_day_of_the_season, defence_factor):
    """defence factor is <defence_factor>."""
    footy = last_day_of_the_season['footy']
    team = last_day_of_the_season['team']
    assert footy.defence_factor(team) == defence_factor, 'Incorrect defence factor.'


@then('expected goals is <expected_goals>')
def expected_goals_is_expected_goals(last_day_of_the_season, expected_goals):
    """expected goals is <expected_goals>."""
    footy = last_day_of_the_season['footy']
    team = last_day_of_the_season['team']
    away_team = last_day_of_the_season['away_team']
    home_team = last_day_of_the_season['home_team']

    if team.team_name() == away_team.team_name():
        calculated_goals = footy.average_goals_scored_by_an_away_team()
        calculated_goals *= footy.attack_strength(away_team)
        calculated_goals *= footy.defence_factor(home_team)
    else:
        calculated_goals = footy.average_goals_scored_by_a_home_team()
        calculated_goals *= footy.attack_strength(home_team)
        calculated_goals *= footy.defence_factor(away_team)

    calculated_goals = round(calculated_goals, 2)
    assert calculated_goals == expected_goals, 'Incorrect expected goals.'


@then('predicted goals is <predicted_goals>')
def predicted_goals_is_predicted_goals(last_day_of_the_season, predicted_goals):
    """predicted goals is <predicted_goals>."""
    footy = last_day_of_the_season['footy']
    away_team = last_day_of_the_season['away_team']
    home_team = last_day_of_the_season['home_team']
    team = last_day_of_the_season['team']
    fixture = footy.fixture(home_team, away_team)

    if team.team_name() == away_team.team_name():
        calculated_goals = fixture.away_team_goals_probability()
    else:
        calculated_goals = fixture.home_team_goals_probability()

    calculated_goals = [round(elem, 2) for elem in calculated_goals]
    calculated_goals = calculated_goals[0:len(predicted_goals)]
    predicted_goals = predicted_goals.split(',')
    predicted_goals = [float(elem) for elem in predicted_goals]
    calculated_goals = calculated_goals[0:len(predicted_goals)]
    assert calculated_goals == predicted_goals


@then('expect the prediction to match <prediction>')
def expect_the_prediction_to_match_prediction(last_day_of_the_season, prediction):
    """expect the prediction to match <prediction>."""
    away_team = last_day_of_the_season['away_team']
    footy = last_day_of_the_season['footy']
    home_team = last_day_of_the_season['home_team']
    prediction = prediction.split(',')
    prediction = [float(elem) for elem in prediction]
    fixture = footy.fixture(home_team, away_team)
    outcome_probabilities = fixture.outcome_probabilities()
    outcome_probabilities = [round(elem, 2) for elem in outcome_probabilities]

    labels = [
        'home win',
        'score draw',
        'away win'
    ]

    for i in range(3):
        # Allow tolerance of 2% for rounding errors.
        min = outcome_probabilities[i] - 0.02
        max = outcome_probabilities[i] + 0.02
        message = f'Outcome prediction ({labels[i]})'
        message += f' {outcome_probabilities[i]} != {prediction[i]}'
        assert min <= prediction[i] <= max, message
