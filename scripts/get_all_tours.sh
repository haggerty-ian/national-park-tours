#!/usr/bin/env bash

mkdir -p tours

while read p; do
  ./get_tours_for_facility.sh $p | jq -r '.[].tour_id' > tours/$p.tours
done <$1
