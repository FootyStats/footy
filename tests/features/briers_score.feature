Feature: Tests for Briers Score

  Scenario Outline: Briers Score
    Given y_true is <y_true>
    When y_prob is <y_prob>
    Then expect briers score to be <briers_score>
    Examples:
      | y_true     | y_prob               | briers_score |
      | [ 1, 0, 0] | [100.0, 0.0, 0.0]    | 0.0          |
      | [ 0, 1, 0] | [100.0, 0.0, 0.0]    | 2.0          |
      | [ 0, 0, 1] | [100.0, 0.0, 0.0]    | 2.0          |
      | [ 1, 0, 0] | [70.02, 18.43, 9.56] | 0.13         |
      | [ 0, 1, 0] | [70.02, 18.43, 9.56] | 1.16         |
      | [ 0, 0, 1] | [70.02, 18.43, 9.56] | 1.34         |
