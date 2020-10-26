Feature: Regression Tests for BBC Article Basis

  References
  ----------
  Spiegelhalter, D. (2009). The professor’s Premiership probabilities. [online] BBC News. Available
  at: http://news.bbc.co.uk/1/hi/programmes/more_or_less/8062277.stm [Accessed 29 Aug. 2020].

  Scenario Outline: Last Day of the EPL 2009 Season
    Given the last day of the EPL 2009
    When the home team is <home_team>
    And the away team is <away_team>
    Then expect the home team win probability to be <home_team_win_probability>
    And expect a score draw probability to be <score_draw_probability>
    And expect an away team probability to be <away_team_win_probability>
    And expect the predicted goals to be scored by the home team to be <expected_home_team_goals>
    And expect the predicted goals to be scored by the away team to be <expected_away_team_goals>
    And expect the predicted final score probability to be <final_score_probability>
    Examples:
      | home_team | away_team | home_team_win_probability | score_draw_probability | away_team_win_probability | expected_home_team_goals | expected_away_team_goals | final_score_probability |
      | Arsenal   | Stoke     | 0.72                      | 0.19                   | 10.0                      | 2                        | 0                        | 0.14                    |

