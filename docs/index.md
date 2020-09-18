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
>>> widget.add_team('Arsenal', 64, 36, 18, 19, 69)
>>> widget.add_team('Aston Villa', 53, 48, 18, 19, 59)
>>> widget.add_team('Blackburn', 40, 60, 18, 19, 40)
>>> widget.add_team('Bolton', 41, 52, 19, 18, 41)
>>> widget.add_team('Chelsea', 65, 22, 19, 18, 80)
>>> widget.add_team('Everton', 53, 37, 19, 18, 60)
>>> widget.add_team('Fulham', 39, 32, 18, 19, 53)
>>> widget.add_team('Hull', 39, 63, 18, 19, 35)
>>> widget.add_team('Liverpool', 74, 26, 18, 19, 83)
>>> widget.add_team('Man City', 57, 50, 18, 19, 47)
>>> widget.add_team('Man United', 67, 24, 19, 18, 87)
>>> widget.add_team('Middlesbrough', 27, 55, 19, 18, 32)
>>> widget.add_team('Newcastle', 40, 58, 19, 18, 34)
>>> widget.add_team('Portsmouth', 38, 56, 19, 18, 41)
>>> widget.add_team('Stoke', 37, 51, 19, 18, 45)
>>> widget.add_team('Sunderland', 32, 51, 18, 19, 36)
>>> widget.add_team('Tottenham', 44, 42, 19, 18, 51)
>>> widget.add_team('West Brom', 36, 67, 19, 18, 31)
>>> widget.add_team('West Ham', 40, 44, 18, 19, 48)
>>> widget.add_team('Wigan', 33, 45, 18, 19, 42)
```

Get the data contained by the object as a Pandas dataframe.

```python
>>> widget.dataframe()
```

Setting the number of average goals scored.

```python
>>> widget.average_goals_scored_by_a_home_team(1.36)
>>> widget.average_goals_scored_by_an_away_team(1.06)
>>> widget.score_probability('Arsenal', 'Stoke').head()
```

Plot the outcome probability

```python
>>> widget.outcome_probability('Arsenal', 'Stoke')
```

Get a list of all the teams from the dataset.

```python
>>> widget.get_teams()
```


#### add_team(team_name, goals_for, goals_against, home_games, away_games, points)
Add a team to the table.


* **Parameters**

    
    * **team_name** (*str*) – The name of the team to add.


    * **goals_for** (*int*) – The number of goals scored by the team.


    * **goals_against** (*int*) – The number of goals conceded by the team.


    * **home_games** (*int*) – The number of home games played by the team.


    * **away_games** (*int*) – The number of away games played by the team.


    * **points** (*int*) – The number of points in the table that the team has.



#### attack_strength(team_name)
Get the attack strength of a team.


* **Parameters**

    **team_name** (*str*) – The name of the team to get the attack strength of.



* **Returns**

    The attack strength of the team.



* **Return type**

    float



* **Raises**

    **KeyError** – When a team name is provided that is not in the dataset.



#### average_goals_scored_by_a_home_team(goals=None)
Get or set the average goals scored by a home team.


* **Parameters**

    **goals** (*float*) – The average number of goals scored by any team playing at home over the duration of the season.



* **Returns**

    The average number of goals scored by any team playing at home over the duration of the season.



* **Return type**

    float



#### average_goals_scored_by_an_away_team(goals=None)
Get or set the average goals scored by an away team.


* **Parameters**

    **goals** (*float*) – The average number of goals scored by any team playing away over the duration of the season.



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

### Examples

```python
>>> import footy
>>> footy.brier_score(np.array([1, 0, 0]), np.array([1.0, 0.0, 0.0]))
0.0
```


#### data(data=None)
Get or set the object data.


* **Parameters**

    **data** (*dict**, **optional*) – A new dictionary to replace the objects data.



* **Returns**

    The object data.



* **Return type**

    dict



#### dataframe()
Return the object data as a Pandas dataframe.

The dataframe will be sorted on the number of points and goal difference.


* **Returns**

    The object data as a Pandas DataFrame.



* **Return type**

    pandas.DataFrame



#### defence_factor(team_name)
Get the defence factor for a team.


* **Parameters**

    **team_name** (*str*) – The name of the team to get the defence factor for.



* **Returns**

    The defence factor for a specific team.



* **Return type**

    float



* **Raises**

    **KeyError** – When a team name is provided that is not in the dataset.



#### get_team(team_name)
Get the details of a specific team from the dataset.


* **Parameters**

    **team_name** (*str*) – The name of the team that the details are to be returned for.



* **Raises**

    **KeyError** – When a team name is provided that is not in the dataset.



* **Returns**

    The elements of the returned dictionary are goals_for (the number of goals scored), goals_against (the
    number of goals conceded), home_games (number of games played at home), away_games (number of games played
    away).



* **Return type**

    dict


### Examples

Get the data specific to Arsenal.

```python
>>> widget.get_team('Arsenal')
{'goals_for': 64, 'goals_against': 36, 'home_games': 18, 'away_games': 19}
```


#### get_teams()
Get a list of the team names held in the dataset.


* **Returns**

    A list of the team names.



* **Return type**

    List of str


### Examples

Get a list of all the teams from the dataset.

```python
>>> widget.get_teams()
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


#### goals_conceded(team_name=None)
Get the number of goals conceded.

If the team name is provided then the number of goals conceded by that team is returned.  Otherwise the number
of goals conceded by all teams is returned.


* **Parameters**

    **team_name** (*str**, **optional*) – The name of the team to get the number of goals conceded.



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



#### outcome_probability(home_team, away_team, show_plot=True)
Return the probability of a home win, a draw or an away win.


* **Parameters**

    
    * **home_team** (*str*) – The name of the home team.


    * **away_team** (*str*) – The name of the away team.


    * **show_plot** (*bool**, **optional*) – Should a plot be shown (default is true).



* **Returns**

    (home win probability, draw probability, away win probability).



* **Return type**

    tuple



* **Raises**

    **KeyError** – When a team name is provided that is not in the dataset.



#### score_probability(home_team, away_team, show_plots=True)
Return a dataframe of the score probability.


* **Parameters**

    
    * **home_team** (*str*) – The name of the home team.


    * **away_team** (*str*) – The name of the away team.


    * **show_plots** (*bool**, **optional*) – Should the probability be plotted (default True).



* **Returns**

    The probability of the games score.



* **Return type**

    pandas.DataFrame



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
