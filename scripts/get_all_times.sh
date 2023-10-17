#!/usr/bin/env bash

for facility in $1/*.tours; do
  filename=$(basename "$facility")
  facility_id="${filename%.*}"
  while read p; do
    mkdir -p tours/$facility_id
    ./get_times_for_tour.sh $facility_id $p > tours/$facility_id/$p.times
  done <$facility
done
