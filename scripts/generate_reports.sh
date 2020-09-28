#!/bin/sh

ISO_8601_TIMESTAMP=$( date -u +'%Y-%m-%dT%H%M' )
mkdir -p html

for code in BL1 BSA FL1 PD PL PPL SA; do
  FOOTBALL_DATA_API_COMPETITION_CODE=$code jupyter-nbconvert \
    competition.ipynb --execute \
    --output="${code}-${ISO_8601_TIMESTAMP}" \
    --output-dir=html
  sleep 10
done
