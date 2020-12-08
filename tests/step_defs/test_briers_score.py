# coding=utf-8
"""Tests for Briers Score feature tests."""

import json
import numpy as np

from footy import Footy

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

CONVERTERS = dict(
    y_true=str,
    y_prob=str,
    briers_score=float
)


@scenario('../features/briers_score.feature', 'Briers Score', example_converters=CONVERTERS)
def test_briers_score():
    """Briers Score."""


@given('y_true is <y_true>', target_fixture='test_data')
def y_true_is_y_true(y_true):
    """y_true is <y_true>."""
    s = '{ "y_true": %s }' % y_true
    return json.loads(s)


@when('y_prob is <y_prob>')
def y_prob_is_y_prob(test_data, y_prob):
    """y_prob is <y_prob>."""
    s = '{ "y_prob": %s }' % y_prob
    test_data['y_prob'] = json.loads(s)['y_prob']


@then('expect briers score to be <briers_score>')
def expect_briers_score_to_be_briers_score(test_data, briers_score):
    """expect briers score to be <briers_score>."""
    footy = Footy()
    y_prob = np.array(test_data['y_prob'])
    y_true = np.array(test_data['y_true'])
    assert briers_score == footy.brier_score(y_true, y_prob)
