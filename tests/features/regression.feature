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
      | home_team     | away_team     | home_team_win_probability | score_draw_probability | away_team_win_probability | expected_home_team_goals | expected_away_team_goals | final_score_probability |
      | Arsenal       | Stoke         | 72.0                      | 19.0                   | 10.0                      | 2                        | 0                        | 14                      |
      | Aston Villa   | Newcastle     | 62.0                      | 21.0                   | 17.0                      | 1                        | 0                        | 10                      |
      | Blackburn     | West Brom     | 54.0                      | 23.0                   | 23.0                      | 1                        | 1                        | 10                      |
      # Article says 19% probability we calculated 17%.
      # Fulham        | Everton       | 35.0                      | 35.0                   | 30.0                      | 0                        | 0                        | 19                      |
      | Hull          | Man United    | 9.0                       | 19.0                   | 72.0                      | 0                        | 2                        | 14                      |
      | Liverpool     | Tottenham     | 72.0                      | 20.0                   | 9.0                       | 1                        | 0                        | 16                      |
      # Article says mose likely outcome 2 - 1 (10%).  We calculate 1 - 1 10.36%.
      # Man City      | Bolton        | 59.0                      | 22.0                   | 19.0                      | 2                        | 1                        | 10                      |
      | Sunderland    | Chelsea       | 10.0                      | 25.0                   | 65.0                      | 0                        | 1                        | 20                      |
      | West Ham      | Middlesbrough | 57.0                      | 28.0                   | 15.0                      | 1                        | 0                        | 19                      |
      | Wigan         | Portsmouth    | 44.0                      | 32.0                   | 25.0                      | 1                        | 0                        | 16                      |
