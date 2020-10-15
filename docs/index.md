<!-- Footy documentation master file, created by
sphinx-quickstart on Sat Aug 15 19:24:36 2020.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# Welcome to Footy’s documentation!

# Footy

Footy - A statistics module for football (soccer).


### class footy.Footy()
Main class of the footy module.

Please note that methods that accept a team name parameter that the team name must match exactly (including case
sensitivity).  Use the get_teams method to get a list of valid team names.

### Examples

```python
>>> import footy
>>> widget = footy.Footy()
>>> widget.add_team(Team('Arsenal', 64, 36, 18, 19, 69))
>>> widget.add_team(Team('Aston Villa', 53, 48, 18, 19, 59))
>>> widget.add_team(Team('Blackburn', 40, 60, 18, 19, 40))
>>> widget.add_team(Team('Bolton', 41, 52, 19, 18, 41))
>>> widget.add_team(Team('Chelsea', 65, 22, 19, 18, 80))
>>> widget.add_team(Team('Everton', 53, 37, 19, 18, 60))
>>> widget.add_team(Team('Fulham', 39, 32, 18, 19, 53))
>>> widget.add_team(Team('Hull', 39, 63, 18, 19, 35))
>>> widget.add_team(Team('Liverpool', 74, 26, 18, 19, 83))
>>> widget.add_team(Team('Man City', 57, 50, 18, 19, 47))
>>> widget.add_team(Team('Man United', 67, 24, 19, 18, 87))
>>> widget.add_team(Team('Middlesbrough', 27, 55, 19, 18, 32))
>>> widget.add_team(Team('Newcastle', 40, 58, 19, 18, 34))
>>> widget.add_team(Team('Portsmouth', 38, 56, 19, 18, 41))
>>> widget.add_team(Team('Stoke', 37, 51, 19, 18, 45))
>>> widget.add_team(Team('Sunderland', 32, 51, 18, 19, 36))
>>> widget.add_team(Team('Tottenham', 44, 42, 19, 18, 51))
>>> widget.add_team(Team('West Brom', 36, 67, 19, 18, 31))
>>> widget.add_team(Team('West Ham', 40, 44, 18, 19, 48))
>>> widget.add_team(Team('Wigan', 33, 45, 18, 19, 42))
```

Get the data contained by the object as a Pandas dataframe (sorted by
league position and goal difference).

```python
>>> widget.dataframe()
```

Setting the number of average goals scored.

```python
>>> widget.average_goals_scored_by_a_home_team(1.36)
>>> widget.average_goals_scored_by_an_away_team(1.06)
```

Now get the prediction of game (will return None if not enough data is
available).  For the full details of the response returned, see the
fixture method.

```python
>>> response = widget.fixture(widget.get_team('Arsenal'), widget.get_team('Stoke'))
```

Get a list of all the teams from the dataset.

```python
>>> widget.get_team_names()
['Arsenal',
 'Aston Villa',
 'Blackburn',
 'Bolton',
 'Chelsea',
 'Everton',
 'Fulham',
 'Hull',
 'Liverpool',
 'Man City',
 'Man United',
 'Middlesbrough',
 'Newcastle',
 'Portsmouth',
 'Stoke',
 'Sunderland',
 'Tottenham',
 'West Brom',
 'West Ham',
 'Wigan']
```

Get the data specific to Arsenal.

```python
>>> team = widget.get_team('Arsenal')
```

Get a Bried Score for a result.

```python
>>> footy.brier_score(np.array([1, 0, 0]), np.array([1.0, 0.0, 0.0]))
0.0
```


#### add_team(team)
Add a team to the table.


* **Parameters**

    **team** (*footy.domain.Team.Team*) – The team to set or update (using the team name as a key) in Footy object.



#### attack_strength(team)
Get the attack strength of a team.

The attack strength is calculated by dividing the number of goals scored by the team by the average goals
scored by any team.  An attack strength higher than 1.0 indicates that the team scores more than the
average number of goals by a team in the competition.


* **Parameters**

    **team** (*footy.domain.Team.Team*) – The team to get the attack strength of.



* **Returns**

    The attack strength of the team.  If there is not enough data to
    calculate this correctly, return None.



* **Return type**

    float



* **Raises**

    **KeyError** – When a team that is provided that is not in the dataset.



#### average_goals_scored_by_a_home_team(goals=None)
Get or set the average goals scored by a home team.


* **Parameters**

    **goals** (*float**, **optional*) – The average number of goals scored by any team playing at home over the duration of the season.



* **Returns**

    The average number of goals scored by any team playing at home over the duration of the season.



* **Return type**

    float



#### average_goals_scored_by_an_away_team(goals=None)
Get or set the average goals scored by an away team.


* **Parameters**

    **goals** (*float**, **optional*) – The average number of goals scored by any team playing away over the duration of the season.



* **Returns**

    The average number of goals scored by any team playing away over the duration of the season.



* **Return type**

    float



#### brier_score(y_true, y_prob)
Return a Brier Score of the probability against the actuality.


* **Parameters**

    
    * **y_true** (*np.array*) – What actually happened.  Should be a value for each predicted category (e.g. home win, score draw or away
    win).


    * **y_prob** (*np.array*) – The predicted probability of each category.  The number of elements in this parameter must match the number
    of parameters given in y_true. The sum of all the values of this list cannot exceed 1.0.



* **Returns**

    A value between 0.0 and 2.0 where a value closer to 0.0 indicates that a predicted probability was more
    accurate that a value closer to 2.0.  This result will be rounded to the nearest two decimal places.



* **Return type**

    float


### References

Brier, G.W. (1950): “Verification of Forecasts Expressed in Terms of Probability”, Monthly Weather Review,
volume 79, number 1.


#### dataframe()
Return the object data as a Pandas dataframe.

The dataframe will be sorted on the number of points and goal difference.


* **Returns**

    The object data as a Pandas DataFrame.



* **Return type**

    pandas.DataFrame



#### defence_factor(team)
Get the defence factor for a team.

The defence factor is calculated by dividing the number of goals that the team have conceded by the average
number of goals conceded by all the teams in the competition.  A defence factor > 1.0 indicates that the
team concedes more goals that of the average team.


* **Parameters**

    **team** (*footy.domain.Team.Team*) – The team to get the defence factor for.



* **Returns**

    The defence factor for a specific team.  If there is not enough
    data to calculate correctly, return None.



* **Return type**

    float



* **Raises**

    **KeyError** – When the team provided is not in the dataset.



#### fixture(home_team, away_team)
Calculate the probabilities of a fixture between two teams.


* **Parameters**

    
    * **home_team** (*footy.domain.Team.Team*) – The home team.


    * **away_team** (*footy.domain.Team.Team*) – The away team.



* **Returns**

    A fixture containing the predicted probabilities (if available).



* **Return type**

    footy.domain.Fixture.Fixture



* **Raises**

    **KeyError** – When a team name is provided that is not in the dataset.



#### get_team(team_name)
Get the details of a specific team from the dataset.


* **Parameters**

    **team_name** (*str*) – The name of the team that the details are to be returned for.



* **Raises**

    **KeyError** – When a team name is provided that is not in the dataset.



* **Returns**

    The team referred by the team name.



* **Return type**

    footy.domain.Team.Team



#### get_team_names()
Get a list of the team names held in the dataset.


* **Returns**

    A list of the team names.



* **Return type**

    List of str



#### goals_conceded(team_name=None)
Get the number of goals conceded.

If the team name is provided then the number of goals conceded by that team is returned.  Otherwise the number
of goals conceded by all teams is returned.


* **Parameters**

    **team_name** (*footy.domain.Team.Team**, **optional*) – The name of the team to get the number of goals conceded.



* **Returns**

    The number of goals conceded by the team or the league.



* **Return type**

    int



* **Raises**

    **KeyError** – When a team name is provided that is not in the dataset.



#### goals_scored(team_name=None)
Get the number of goals scored.

If team_name is provided, the number of goals scored by that team is returned.  If not, the average number of
goals scored by all teams is returned.


* **Parameters**

    **team_name** (*str**, **optional*) – The name of the team to get the number of goals scored.



* **Returns**

    The number of goals scored by a team or in the league.



* **Return type**

    int



* **Raises**

    **KeyError** – When a team name is provided that is not in the dataset.



### footy.OUTCOME_AWAY_WIN( = [0, 0, 1])
The notation of an away outcome.


* **Type**

    List of int



### footy.OUTCOME_HOME_WIN( = [1, 0, 0])
The notation of a home win outcome.


* **Type**

    List of int



### footy.OUTCOME_SCORE_DRAW( = [0, 1, 0])
The notation of a score draw outcome.


* **Type**

    List of int


# footy.domain.Competition

Competition - Data structure for a competition/league.


### class footy.domain.Competition.Competition(code, name=None, teams=None, start_date=None, end_date=None, stage='unknown', fixtures=None)
Competition - Data structure for a competition/league.


#### add_team(team)
Add the provided team to the list of teams if an instance of that object isn’t already present.


* **Parameters**

    **team** (*Team*) – The Team to be added to Teams.



#### property code()
Getter method for property code.


* **Returns**

    The value of property code.



* **Return type**

    str



#### property end_date()
Getter method for property end_date.


* **Returns**

    The value of property end_date.



* **Return type**

    str



#### property fixtures()
Getter method for property fixtures.


* **Returns**

    The value of property fixtures.



* **Return type**

    list



#### property name()
Getter method for property name.


* **Returns**

    The value of property name.



* **Return type**

    str



#### property stage()
Getter method for property stage.


* **Returns**

    The value of property stage.



* **Return type**

    str



#### property start_date()
Getter method for property start_date.


* **Returns**

    The value of property start_date.



* **Return type**

    str



#### property teams()
Getter method for property teams.


* **Returns**

    The value of property teams.



* **Return type**

    list


# footy.domain.Result

Result - Data structure for a result.


### class footy.domain.Result.Result(status='SCHEDULED', home_team_goals_scored=0, away_team_goals_scored=0)
Result - Data structure for a result.


#### property away_team_goals_scored()
Getter method for property away_team_goals_scored.


* **Returns**

    The value of property away_team_goals_scored.



* **Return type**

    int



#### property home_team_goals_scored()
Getter method for property home_team_goals_scored.


* **Returns**

    The value of property home_team_goals_scored.



* **Return type**

    int



#### property status()
Getter method for property status.


* **Returns**

    The value of property status.



* **Return type**

    str


# footy.domain.Team

Result - Data structure for a team.


### class footy.domain.Team.Team(team_name, goals_for=0, goals_against=0, home_games=0, away_games=0, points=0)
Result - Data structure for a team.


#### property away_games()
Getter method for property away_games.


* **Returns**

    The value of property away_games.



* **Return type**

    int



#### property goal_difference()
Calculate and return the goal difference for the team.


* **Returns**

    goals_for - goals_against



* **Return type**

    int



#### property goals_against()
Getter method for property goals_against.


* **Returns**

    The value of property goals_against.



* **Return type**

    int



#### property goals_for()
Getter method for property goals_for.


* **Returns**

    The value of property goals_for.



* **Return type**

    int



#### property home_games()
Getter method for property home_games.


* **Returns**

    The value of property home_games.



* **Return type**

    int



#### property points()
Getter method for property points.


* **Returns**

    The value of property points.



* **Return type**

    int



#### property team_name()
Getter method for property team_name.


* **Returns**

    The value of property team_name.



* **Return type**

    str


# footy.domain.Fixture

Fixture - Data structure for a fixture.


### class footy.domain.Fixture.Fixture(home_team, away_team, status='SCHEDULED', utc_start='', result=None)
Fixture - Data structure for a fixture.


#### property away_team()
Getter method for property away_team.


* **Returns**

    The value of property away_team.



* **Return type**

    Team



#### away_team_goals_probability(away_team_goals_probability=None)
Get or set the away_team_goals_probability of the fixture.


* **Parameters**

    **away_team_goals_probability** (*list of float*) – A list of floats indicating (with values between 0.0 and 1.0) the probability of between zero and six
    goals being scored by the away team.



* **Returns**

    A list of floats indicating (with values between 0.0 and 1.0) the probability of between zero and six
    goals being scored by the away team.  If there is not enough data to calculate the probabilities, this
    will return None.



* **Return type**

    list of float



#### final_score_probabilities(final_score_probabilities=None)
Get or set the final_score_probabilities of the fixture.


* **Parameters**

    **final_score_probabilities** (*DataFrame*) – A Pandas DataFrame with each row containing the number of goals scored by the home team, the number of
    goals scored by the away team and the probability of that final score. The table will be sorted with the
    most probable results descending.



* **Returns**

    A Pandas DataFrame with each row containing the number of goals scored by the home team, the number of
    goals scored by the away team and the probability of that final score. The table will be sorted with the
    most probable results descending.  If there is not enough data to calculate the probabilities, this
    will return None.



* **Return type**

    DataFrame



#### property home_team()
Getter method for property home_team.


* **Returns**

    The value of property home_team.



* **Return type**

    Team



#### home_team_goals_probability(home_team_goals_probability=None)
Get or set the home_team_goals_probability of the fixture.


* **Parameters**

    **home_team_goals_probability** (*list of float*) – A list of floats indicating (with values between 0.0 and 1.0) the probability of between zero and six
    goals being scored by the home team.



* **Returns**

    A list of floats indicating (with values between 0.0 and 1.0) the probability of between zero and six
    goals being scored by the home team.  If there is not enough data to calculate the probabilities, this
    will return None.



* **Return type**

    list of float



#### outcome_probabilities(outcome_probabilities=None)
Get or set the outcome_probabilities of the fixture.


* **Parameters**

    **outcome_probabilities** (*list of float*) – A list of three floats indicating (with values between 0.0 and 1.0) the probability of a home win, a score
    draw or an away win respectively.



* **Returns**

    A list of three floats indicating (with values between 0.0 and 1.0) the probability of a home win, a score
    draw or an away win respectively.  If not enough data is available to calculate the probabilities the
    will return None.



* **Return type**

    list of float



#### property result()
Getter method for property result.


* **Returns**

    The value of property result.



* **Return type**

    Result



#### property status()
Getter method for property status.


* **Returns**

    The value of property status.



* **Return type**

    str



#### property utc_start()
Getter method for property utc_start.


* **Returns**

    The value of property utc_start.



* **Return type**

    str


# footy.engine.PredictionEngine

Prediction Engine - Engine to predict the result of future fixtures.


### class footy.engine.PredictionEngine.PredictionEngine(competition)
Prediction Engine - Engine to predict the result of future fixtures.


#### predict_results(competition)
Generate the predictions for fixtures within a competition.


* **Returns**

    Enriched competition with most recent predictions.



* **Return type**

    Competition


# footy.engine.UpdateEngine

Prediction Engine - Update the data model with the most resent fixtures and results.


### class footy.engine.UpdateEngine.UpdateEngine()
Prediction Engine - Update the data model with the most resent fixtures and results.


#### get_competition(code)
Retrieve data for the supplied competition code.


* **Returns**

    A Competition object with the most recent fixtures and results for the supplied competition code.



* **Return type**

    Competition



#### update_competition(competition)
Retrieve data and enrich the supplied competition with the most recent fixtures and results.


* **Returns**

    A Competition object with the most recent fixtures and results for the supplied competition code.



* **Return type**

    Competition
