#!/usr/bin/env bash

curl "https://www.recreation.gov/api/search?exact=false&size=500&fq=-entity_type:(tour%20OR%20timedentry_tour)&fq=entity_type:ticketfacility&fq=entity_type:timedentry" | jq -r '.results[].parent_id'
