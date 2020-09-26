#!/usr/bin/env python
"""
Take snapshots from the different competitions from
https://www.football-data.org/ and store the data.

To be able to use this, one must have the FOOTBALL_DATA_API environment
variable set.

Once the data has been downloaded and saved, please run the following
command:

>>> bzip -v --best tests/resources/data/*.json

Example:

>>> tests/resources/scripts/get_competition_snapshot.py
"""
import json
import logging
import time
import yaml

from football_data_api import data_fetchers

logging.basicConfig(level=logging.INFO)
logging.info('Reading configuration from from footy.yml.')

with open('footy.yml') as stream:
    config_data = yaml.safe_load(stream)

competition_count = len(config_data['competitions'].keys())
sleep_time = 20

for competition_code in config_data['competitions'].keys():
    competition_detail = config_data['competitions'][competition_code]
    competition_name = competition_detail['competition_name']
    logging.info(f'Processing {competition_code} ({competition_name})')
    competition = data_fetchers.CompetitionData(competition_name)
    matches_data = competition.get_info('matches')
    last_update = matches_data['competition']['lastUpdated']
    last_update_date = last_update.split('T')[0]
    contents = json.dumps(matches_data, indent=4, sort_keys=True)
    file_name = 'tests/resources/data/'
    file_name += f'{competition_code}-{last_update_date}.json'

    with open(file_name, 'w') as stream:
        stream.write(contents)

    competition_count -= 1

    if competition_count > 0:
        # We need to sleep between each call to the API so as not to exceed
        # the transaction rate in the EULA.
        logging.info(f'Sleeping {sleep_time}s.')
        time.sleep(sleep_time)
