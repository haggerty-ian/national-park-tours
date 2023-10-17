#!/usr/bin/env bash

curl -s "https://www.recreation.gov/api/ticket/availability/facility/$1/monthlyAvailabilitySummaryView?year=2023&month=11&inventoryBucket=FIT&tourId=$2"
