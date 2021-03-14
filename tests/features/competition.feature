Feature: Test the Competition Class

  This is basically a rehash of the test_footy.py, but checking the figures when they are wrapped in the
  Competition class.

  Scenario Outline: Outcome Predicted Only With Enough Data
    Given the Dummy League
    When the match day is <match_day>
    Then ensure outcome_probabilities <is_none>
    Examples:
      | match_day | is_none |
      | 0         | True    |
      | 1         | False   |
      | 2         | True    |
