# bblm_app

# Running the server

- Python version 3.8.8rc1
- Create python virtual environment and activate it.
- Install dependencies `python -m pip install -r requirements.txt`
- Run `python manage.py makemigrations` & `python manage.py migrate`
- Run `python manage.py dbinit` to populate the test dbinit

# APIs
    'players/' - All players
    'players/player_id - Specific player details
    'teams/' - All teams
    'teams/team_id - Specific team
    'teams/players/team_id/' - Players in a specific team

# To-do
User login with jwt

