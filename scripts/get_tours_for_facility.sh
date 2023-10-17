#!/usr/bin/env bash

echo $(curl -s "https://www.recreation.gov/api/ticket/gateway/$1/tour")
