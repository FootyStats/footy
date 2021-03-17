Feature: Tests for Briers Score

  The final test is to check against figures given in the article mentioned below
  http://www.pinnacle.com/en/betting-articles/Soccer/brier-score-method-to-measure-surprises-in-premier-league/9BE2PL9DK4UM54FY

  Scenario Outline: Briers Score
    Given y_true is <y_true>
    When y_prob is <y_prob>
    Then expect briers score to be <briers_score>
    Examples:
      | y_true     | y_prob                | briers_score |
      | [ 1, 0, 0] | [1.0, 0.0, 0.0]       | 0.0          |
      | [ 0, 1, 0] | [1.0, 0.0, 0.0]       | 2.0          |
      | [ 0, 0, 1] | [1.0, 0.0, 0.0]       | 2.0          |
      | [ 0, 0, 1] | [0.583, 0.245, 0.171] | 1.09         |
