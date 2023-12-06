# README
## Running Scripts
This project defines some custom commands that can be run using Django's manage.py.
```
python3 manage.py fetchfacilities
```

## Getting Started
To get your SQLite database up to speed, run:
```
python3 manage.py migrate emailserver
```

To fetch relevant data, run the custom commands `fetchfacilities` and `fetchtours`

Then, the project should be ready to run with
```
python3 manage.py runserver
```