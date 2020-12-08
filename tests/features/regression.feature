Feature: Last Day of the EPL 2009 Season

  References
  ----------
  Spiegelhalter, D. (2009). The professor’s Premiership probabilities. [online] BBC News. Available
  at: http://news.bbc.co.uk/1/hi/programmes/more_or_less/8062277.stm [Accessed 29 Aug. 2020].

  Spiegelhalter, D., 2009. One Game To Play! | Understanding Uncertainty. [online] Understandinguncertainty.org.
  Available at: <https://understandinguncertainty.org/node/228> [Accessed 7 December 2020].

  Background:
    Given the last day of the EPL 2009

  Scenario Outline: Attack Strength Defence Factor
    When the team name is <team_name>
    Then attack strength is <attack_strength>
    And defence factor is <defence_factor>
    Examples:
      | team_name     | attack_strength | defence_factor |
      | Aston Villa   | 1.15            | 1.04           |
      | Arsenal       | 1.39            | 0.78           |
      | Blackburn     | 0.87            | 1.30           |
      | Bolton        | 0.89            | 1.13           |
      | Chelsea       | 1.41            | 0.48           |
      | Everton       | 1.15            | 0.80           |
      | Fulham        | 0.85            | 0.70           |
      | Hull          | 0.85            | 1.37           |
      | Portsmouth    | 0.83            | 1.22           |
      | Stoke         | 0.8             | 1.11           |
      | Sunderland    | 0.70            | 1.11           |
      | Tottenham     | 0.96            | 0.91           |
      | Liverpool     | 1.61            | 0.57           |
      | Man City      | 1.24            | 1.09           |
      | Man United    | 1.46            | 0.52           |
      | Middlesbrough | 0.59            | 1.20           |
      | Newcastle     | 0.87            | 1.26           |
      | West Brom     | 0.78            | 1.46           |
      | West Ham      | 0.87            | 0.96           |
      | Wigan         | 0.72            | 0.98           |

  Scenario Outline: Expected Goals Home Team
    When the home team is <home_team>
    And the away_team is <away_team>
    And the team name is <team_name>
    Then expected goals is <expected_goals>
    And predicted goals is <predicted_goals>
    Examples:
      | home_team  | away_team  | team_name  | expected_goals | predicted_goals               |
      | Arsenal    | Stoke      | Arsenal    | 2.1            | 0.12,0.26,0.27                |
      | Hull       | Man United | Man United | 2.12           | 0.12,0.25,0.27,0.19,0.10,0.04 |
      | Hull       | Man United | Hull       | 0.6            | 0.55,0.33,0.10,0.02,0         |

  Scenario Outline: Expected Outcomes
    When the home team is <home_team>
    And the away_team is <away_team>
    Then expect the prediction to match <prediction>
    Examples:
      | home_team   | away_team     | prediction     |
      | Arsenal	    | Stoke         | 0.72,0.19,0.1  |
      | Aston Villa | Newcastle     | 0.62,0.21,0.17 |
      | Blackburn   | West Brom     | 0.54,0.23,0.23 |
      | Fulham      | Everton       | 0.35,0.35,0.3  |
      | Hull        | Man United    | 0.09,0.19,0.72 |
      | Liverpool   | Tottenham     | 0.72,0.2,0.09  |
      | Man City    | Bolton        | 0.59,0.22,0.19 |
      | Sunderland  | Chelsea       | 0.1,0.25,0.65  |
      | West Ham    | Middlesbrough | 0.57,0.28,0.15 |
      | Wigan       | Portsmouth    | 0.44,0.32,0.25 |
